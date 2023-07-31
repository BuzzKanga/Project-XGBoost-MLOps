setup:
	# download and install Anaconda
	wget https://repo.anaconda.com/archive/Anaconda3-2023.07-1-Linux-x86_64.sh
	bash Anaconda3-2023.07-1-Linux-x86_64.sh -b

	# update and upgrade
	sudo apt update
	sudo apt upgrade -y

	# install docker
	sudo apt install docker.io -y
	sudo usermod -aG docker $USER 	# reboot using the AWS console for this to take effect

	# create software specific directory
	mkdir soft
	cd soft

	# install docker-compose
	wget https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-linux-x86_64 -O docker-compose
	chmod +x docker-compose	    # make it an executable

	export PATH="${PATH}:${HOME}/soft"	# note to make this persist, it needs to be added to end of .bashrc file
	cd ..

	# install pip
	sudo apt install python3-pip

	# install notebooks
	pip install ipykernel

	# install pipenv
	pip install pipenv --user
	pip install --user --upgrade pipenv

	# create project specific directory
	mkdir project
	cd project

	# clone repo
	git clone https://github.com/BuzzKanga/Project-XGBoost-MLOps.git

"	cd Project-XGBoost-MLOps


