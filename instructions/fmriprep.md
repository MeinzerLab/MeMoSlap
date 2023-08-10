## Prerequisits

1. Complete the [Docker-Setup](./docker.md)
2. Complete the [BIDS-Config-Setup](./bids_config.md)

## Setup command-line

```bash
docker pull nipreps/fmriprep:23.1.3
python -m pip install --user --upgrade fmriprep-docker
```

## Usage

Now you should be able to run fmriprep using the python wrapper. Usually the command should look something like this.

```bash
fmriprep-docker <input-dir> <output-directory> \
    participant --participant-label <participant-label within input-dir> \
    --n_cpus 16 \ # no performance increase with more than 16 cores
    --no-submm-recon # BUG: otherwise recon all error, 
    # NOTE: Instead of the --no-submm-recon flag we could also crop the FOV
```

- There is an example Script in [.Greifswald/fmriprep.sh](./Greifswald/fmriprep.sh)

## Troubleshooting

fmriprep depends on freesurfer [freesurfer install](https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall)

- if your terminal doesn't show the right freesurfer path look at your `.bashr`

```bash
nano ~/.bashrc
```

- add the following lines to the end of the script
  
```bash
export FREESURFER_HOME="/usr/local/freesurfer/7.4.1"
source $FREESURFER_HOME/SetUpFreeSurfer.sh
export FS_LICENSE=$FREESURFER_HOME/license.txt
```
