# Deployment Validator

This project implements a pre-deployer validator utility.

## Requirements

### Environment: 

- Ubuntu 18.04.05 
- Python 3.6.9

### Target audience: 

- Deployment Engineers

## Develop

When working on MacOS:

```shell
docker build -t workspace -f Dockerfile-dev .
docker run -it --rm -v $(pwd):/app bash
```

```shell
pip install setuptools
python3.6 setup.py develop
```

Building the package:

```shell
python3.6 -m pip install --upgrade build
python3.6 -m build
```

## Running the tool

```shell
# Get help
python3.6 -m deployer_validator -h

# Run the validation
sudo python3.6 -m deployer_validator -v

# Pass the CORSIGHT_ID environment variable
sudo python3.6 -m deployer_validator -v --CORSIGHT_ID=5
```


## TODO:

- Add a logger:
  - Output persistent file
  - Output to central location
- Allow verbosity
- Exit code per error
- Testing
- Allow running from container