## Prerequisits

1. Complete the [Docker-Setup](./docker.md)

## Setup

```bash
docker pull bids/validator
```

## Usage (directly from [github](https://github.com/bids-standard/bids-validator#docker-image))

To use bids validator with [docker](https://www.docker.com/), you simply need to [install docker](https://docs.docker.com/install/) on your system.

And then from a terminal run:

* `docker run -ti --rm bids/validator --version` to print the version of the docker image
* `docker run -ti --rm bids/validator --help` to print the help
* `docker run -ti --rm -v /path/to/data:/data:ro bids/validator /data`to validate the dataset `/path/to/data` on your host machine

See here for a brief explanation of the commands:

* `docker run` is the command to tell docker to run a certain docker image, usually taking the form `docker run <IMAGENAME> <COMMAND>`
* the `-ti` flag means the inputs are accepted and outputs are printed to the terminal
* the `--rm` flag means that the state of the docker container is not saved after it has run
* the `-v` flag is adding your local data to the docker container ([bind-mounts](https://docs.docker.com/storage/bind-mounts/)). Importantly, the input after the `-v` flag consists of three fields separated colons: `:`
  * the first field is the path to the directory on the host machine: `/path/to/data`
  * the second field is the path where the directory is mounted in the container
  * the third field is optional. In our case, we use `ro` to specify that the mounted data is *read only*
