#!/bin/bash

# if you got any errors have a look in the instructions/fmriprep.md for help

bids_root_dir="/media/MeinzerMRI/Studien/MeMoSLAP/01_DICOMS"  # change to root dir
allsbjs=$(find ${bids_root_dir}/sub* -maxdepth 0 -exec basename {} \;)

sbjs=()

for sbj in $allsbjs; do
    
    if [ ! -d $bids_root_dir/derivatives/fmriprep/$sbj ]; then
        sbjs+=("${sbj}");
    fi
    
done

echo "${sbjs[@]}"

for sbj in "${sbjs[@]}"; do

    docker run -it --rm -v $bids_root_dir:/input:ro -v $bids_root_dir/derivatives/mriqc:/output nipreps/mriqc /input /output participant --participant-label sub-$sbj
    
done
