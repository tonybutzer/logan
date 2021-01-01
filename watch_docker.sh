#! /bin/bash

for con in `docker ps -q`; do echo $con ; docker exec -i $con ls -l --block-size=10m   TIF; done

