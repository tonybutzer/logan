#! /bin/bash

sudo mkdir -p /mnt/eco-w1
sudo chown ubuntu:ubuntu /mnt/eco-w1
REGION=us-west-2

sudo s3fs -o allow_other -o iam_role="EcoAI-Ec2_Role" \
-o use_cache=/tmp \
-o url="https://s3-$REGION.amazonaws.com" \
-o umask=0227,uid=1000 \
-o nonempty     \
        eco-w1 /mnt/eco-w1


