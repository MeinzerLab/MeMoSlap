bids_path="/media/Data02/MeMoSlap/fmriprep/bids"

docker run -ti --rm -v $bids_path:/data:ro bids/validator /data
