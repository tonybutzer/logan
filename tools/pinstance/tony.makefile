build: pre
	sudo pip3 install -e .

build2:
	pip install -e .

pip3:
	sudo apt-get install python3-pip

pre:	
	mkdir -p ~/.aws
	echo "[default]" > ~/.aws/config
	echo "region = us-west-2" >> ~/.aws/config

install:
	sudo yum install python36-pip -y
