# -*- coding: utf-8 -*-

import os
import os.path as op
import pickle
import shutil
from datetime import datetime as dt
from glob import glob
from pathlib import Path

import notificator as nftcr
from dcm2bids.dcm2bids_gen import Dcm2BidsGen

root_dir = "/media/Data02/MeMoSlap/fmriprep"

src = op.join(root_dir, "dicom")
dest = op.join(root_dir, "bids")
code_dir = op.join(root_dir, "bids", "code")
cfg = op.join(code_dir, "BIDS_config.json")
log = "converted_final.pckl"
textlog = op.join(code_dir, "SUBJECTS_BIDS_LOG.txt")

old = []
todo = os.listdir(src)

if op.isfile(log):
    with open(log, "rb") as f:
        old = pickle.load(f)

# doItAgain = ["001_base","001p1_1","pilot01_p11"]
# NOTE: add participants to run again
doItAgain = [
    "055_base",
    "pilot01_p11",
    "pilot02_p31",
]
notify = False
# ########
for sub in todo:
    if sub in old and sub not in doItAgain:
        continue
    sub_path = op.join(src, sub)
    session = os.listdir(sub_path)
    for s in session:
        subID, subSes = sub.split("_")
        ######
        try:
            print(f"OK, converting: {sub}")
            mke = Dcm2BidsGen(
                dicom_dir=sub_path,
                participant=subID,
                config=cfg,
                output_dir=Path(dest),
                session=subSes,
                clobber=False,
                forceDcm2niix=False,
                log_level="DEBUG",
            )

            mke.run()

            session_path = op.join(dest, f"sub-{subID}", f"ses-{subSes}")
            sbref_bvecs = glob(op.join(session_path, "dwi", "*sbref.bvec"))
            sbref_bvals = glob(op.join(session_path, "dwi", "*sbref.bval"))
            epi_bvecs = glob(op.join(session_path, "fmap", "*epi.bvec"))
            epi_bvals = glob(op.join(session_path, "fmap", "*epi.bval"))

            try:
                for file in sbref_bvals + sbref_bvecs + epi_bvecs + epi_bvals:
                    os.remove(file)

            except OSError as e:
                print(f"Error: {e.filename} - {e.strerror}")

            d = dt.now()
            time = d.strftime("%D:%H:%M:%S")

            with open(textlog, "a") as f:
                f.write(f"{time};sub-{subID};ses-{subSes}\n")

        except OSError as e:
            print(f"Error: {e.filename} - {e.strerror}.")

            #######

with open(log, "wb") as f:
    pickle.dump(todo, f)

# rm bids-temp-dir
tmpdir = op.join(dest, "tmp_dcm2bids")
# Try to remove the tree; if it fails, throw an error using try...except.
try:
    shutil.rmtree(tmpdir)
except OSError as e:
    print(f"Error: {e.filename} - {e.strerror}.")


###############################################################################
# Args:
#    dicom_dir (str or list): A list of folder with dicoms to convert
#    participant (str): Label of your participant
#    config (path): Path to a dcm2bids configuration file
#    output_dir (path): Path to the BIDS base folder
#    session (str): Optional label of a session
#    clobber (boolean): Overwrite file if already in BIDS folder
#    forceDcm2niix (boolean): Forces a cleaning of a previous execution of
#                             dcm2niix
#    log_level (str): logging level
