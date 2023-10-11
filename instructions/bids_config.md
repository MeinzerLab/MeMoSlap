## Prerequisits

1. [Docker-Setup](./docker.md)
2. [BIDS-Validator-Setup](./bids_validator.md)
3. Dcm2Bids version 3.0.1 (e.g., [via Docker](https://hub.docker.com/r/unfmontreal/dcm2bids) or in a python environment )
4. The local Greifswald files: [../Greifswald/BIDS_config.json](../Greifswald/BIDS_config.json) & [../Greifswald/dicomtoBIDS3.py](../Greifswald/dicomtoBIDS3.py)

## Tools

1. [BIDS-examples Github](https://github.com/bids-standard/bids-examples)
2. [BIDS documentation](https://bids-specification.readthedocs.io/en/stable/)

## Creating a BIDS-config

The Greifswald Config should be a good start, when working with dcm2bids version 3.0.1.  If installed via python the Greifswald conversion [script](../Greifswald/dicomtoBIDS3.py) my be used after adjusting the paths used in the script. It is best to start with just 2 or 3 subjects and validate the bids configuration before running all subjects. After running these first subjects use the [bids-validator](../bids_validator.md) to check the bids config:

```bash
docker run -ti --rm -v /path/to/data:/data:ro bids/validator /data
```

## Troubleshooting

If the bids-validator throws any errors:

1. check [BIDS documentation](https://bids-specification.readthedocs.io/en/stable/) if files were specified correctly: e.g., `fmap` does not include the `task` handle relationship with `dwi` or `func` data is provided via `intendedFor`.
2. Sometimes it can be valuable to check the [BIDS-examples Github](https://github.com/bids-standard/bids-examples) if the documentation does not provide any insights.
3. Run dcm2bids & bids-validator again. Check if errors are resolved.
