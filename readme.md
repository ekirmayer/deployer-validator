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
