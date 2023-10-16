# Prerequisits

1. Complete the [Docker-Setup](./docker.md)
2. Complete the [BIDS-Config-Setup](./bids_config.md)

## Setup command-line

### Setup fmriprep:23.02 for ICA-AROMA feature

- [best practice using aroma](https://neurostars.org/t/best-practices-for-aroma-and-fmriprep/1619)
- [other tools for denoising](https://github.com/arielletambini/denoiser)

```bash
docker pull nipreps/fmriprep:23.0
python -m pip install --user --upgrade fmriprep-docker
```

### Setup fmriprep:> 23.02 no functional ICA-AROMA (Date: 11.10.2023)

- [check newest version of fmriprep](https://fmriprep.org/en/23.1.3/changes.html)
  
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
    --use-aroma \
    --no-submm-recon # BUG: otherwise recon all error, 
    # NOTE: Instead of the --no-submm-recon flag we could also crop the FOV
```

- There is an example Script in [Greifswald/fmriprep.sh](../Greifswald/fmriprep.sh)

## fmriprep output help

### slice time correction

- [slice time correction](https://reproducibility.stanford.edu/slice-timing-correction-in-fmriprep-and-linear-modeling/)

### for resting state (run fmriprep with AROMA)


## Errors after fmriprep

### Image look more distorted after fmriprep then before

- [might be due to fieldmaps](https://neurostars.org/t/fmriprep-more-distorted-images-after-fmap-correction/23315/13)
- try to run fmriprep without fieldmap by adding --use-syn-sdc to the [Greifswald/fmriprep.sh](../Greifswald/fmriprep.sh)

## Troubleshooting

### freesurfer

fmriprep depends on freesurfer [freesurfer install](https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall)

- if your terminal doesn't show the right freesurfer path look at your `.bashrc`

```bash
nano ~/.bashrc
```

- add the following lines to the end of the script
  
```bash
export FREESURFER_HOME="/usr/local/freesurfer/7.4.1"
source $FREESURFER_HOME/SetUpFreeSurfer.sh
export FS_LICENSE=$FREESURFER_HOME/license.txt
```

### permission rights

#### docker

[docker permission rights in general](https://phoenixnap.com/kb/docker-permission-denied)

### anaconda virtuel environment

- if you use anaconda environment and get an error like this

```bash
mkdir(name, mode)
"Permission denied ..."
```

- you might chose the [wrong path and tried to make a directory in root](https://stackoverflow.com/questions/70468784/how-to-change-write-permissions-os-makedirs-for-conda)

```txt
use 
~/path/to/BIDS/structure
not
/path/to/BIDS/structure
```

### change owner and permission of folder

- change owner of folder

```{bash}
chown -R user folder
```

- change permission of files and folder recursively

```{bash}
sudo chmod -R 777 folder
```

### bash or shell script

- run bash script uses bash interpreter

```bash
bash *.sh
```

- run shell script (change permission of shell script chmod a+x *.sh)

```bash
./*.sh 
```

## specific errors

### 'dataset_description.json' is missing from project root

- if dataset_description.json is in root but not found by fmriprep-docker

- if a function is not found, (include it in bashrc)[https://neurostars.org/t/fmriprep-docker-command/4105/7]

```bash
pip uninstall fmriprep-docker
pip install --upgrade --user -v fmriprep-docker
```

- or try to install with sudo

```bash
pip uninstall fmriprep-docker
sudo pip install --upgrade --user -v fmriprep-docker
```

- to get location of the function, say fmriprep-docker

```bash
which fmriprep-docker
```

```bash
nano ~/.bashrc
```

```txt
export PATH= (OUTPUT OF "which fmriprep-docker" without brackets):$PATH"
```

- change permission of docker (need sudo right for that) (not recommende to change to 777 use 755, but sometimes only 777 works)

```bash
sudo chmod 777 (OUTPUT OF "which fmriprep-docker" without brackets)
```
