#!/bin/bash

bids_root_dir="/media/Data02/MeMoSlap/fmriprep/bids"
cpus=16 # NOTE: single subject run is recommended and more than 16 cpus do not increase performance
allsbjs=$(find ${bids_root_dir}/sub* -maxdepth 0 -exec basename {} \;)

sbjs=()

for sbj in $allsbjs; do
    
    if [ ! -d $bids_root_dir/derivatives/fmriprep/$sbj ]; then
        sbjs+=("${sbj}");
    fi
    
done

echo "${sbjs[@]}"

for sbj in "${sbjs[@]}"; do
    
    mkdir "$bids_root_dir/derivatives/fmriprep/$sbj"
    
    fmriprep-docker $bids_root_dir "$bids_root_dir/derivatives/fmriprep/$sbj" \
    participant --participant-label "$sbj" \
    --n_cpus $cpus \
    --no-submm-recon # BUG: otherwise recon all error,
    # NOTE: Instead of the --no-submm-recon flag we could also crop the FOV
    
done
