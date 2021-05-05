FROM python

RUN  apt-get update \
        && apt-get install -y  software-properties-common

ENV CONDA_VERSION=4.9.2-5 \
    CONDA_DIR=/srv/conda 

ENV PATH=${CONDA_DIR}/bin:${PATH}
RUN echo "Installing Miniforge..." \
    && URL="https://github.com/conda-forge/miniforge/releases/download/${CONDA_VERSION}/Miniforge3-${CONDA_VERSION}-Linux-x86_64.sh" \
    && wget --quiet ${URL} -O miniconda.sh \
    && /bin/bash miniconda.sh -u -b -p ${CONDA_DIR} \
    && rm miniconda.sh 

#RUN /srv/conda/bin/conda install -y -c conda-forge mamba

RUN echo $PATH && /srv/conda/bin/conda install -y -c conda-forge gdal=3.1.4
