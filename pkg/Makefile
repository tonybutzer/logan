cmds:
	sudo apt update
	sudo apt install make
	sudoapt install python3-pip


tf:
	mkdir -p ./bin
	(cd ./bin ; wget https://releases.hashicorp.com/terraform/0.12.24/terraform_0.12.24_linux_amd64.zip)
	(cd ./bin; unzip *.zip)


docker:
	sudo apt-get -y update
	sudo apt-get -y install docker.io
	sudo apt-get -y install docker-compose
	sudo docker run hello-world

dgroup:
	 sudo usermod -aG docker ubuntu


eco-bucket:
	aws s3 mb s3://eco-w1
	echo eco bucket >> Readme.md
	aws s3 cp Readme.md s3://eco-w1

install-s3fs:
	sudo apt install s3fs
