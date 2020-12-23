FROM tbutzer/et-base-python

ENV VERS=1.1

RUN apt-get update && \
	apt-get install -y vim

# What do we really need here - should prune this Greg
RUN \
	pip install --no-cache rio-cogeo && \
	pip install --no-cache xarray && \
	pip install --no-cache rioxarray 
	


ENV TONY_VERS=1.9
RUN mkdir -p /home/eco \
	&& mkdir -p /home/eco/api

COPY loganLib /home/eco/loganLib
COPY api_etm /home/etm/api_etm

RUN (cd /home/eco/loganLib; make)

# Certificate Hell Fix!
RUN apt-get install ca-certificates && mkdir -p /etc/pki/tls/certs && \
	cp /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt

WORKDIR /home/eco/api
