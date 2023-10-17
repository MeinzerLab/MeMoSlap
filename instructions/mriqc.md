# MRIQC with docker

- have docker installed [details here](docker.md)
- be sure your data are in BIDS format
- in the script [mriqc.sh](../Greifswald/mriqc.sh)  chang root path directory to subject folder with DICOMs in BIDS format 
- run the script [mriqc.sh](../Greifswald/mriqc.sh) to start mriqc via docker

```bash
bash mriqc.sh
```

or as shell script

```bash
./mriqc.sh
```
