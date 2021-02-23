https://github.com/pangeo-data/pangeo-docker-images/blob/8fefc4ba9fa99b630ba6d70dede0a1da3a67fdc9/base-image/Dockerfile


# mamba

> Mamba is a reimplementation of the conda package manager in C++. parallel downloading of repository data and package files using multi-threading

- conda install -y -c conda-forge mamba




# test gdal

## issue
EnvironmentNotWritableError: The current user does not have write permissions to the target environment.
  environment location: /opt/tljh/user
  uid: 1002
  gid: 1004

## Solution - look a TLJH environment and start it with ubuntu account

- https://tljh.jupyter.org/en/latest/howto/env/user-environment.html

# sudo -E conda install -y -c conda-forge gdal=3.1.4


```
jupyter-ubuntu@ip-10-12-69-188:~$ conda list | grep -i gdal
gdal                      3.1.4            py37h2ec2946_6    conda-forge
libgdal                   3.1.4                hbde00c8_6    conda-forge
```


echo $CONDA_DEFAULT_ENV
