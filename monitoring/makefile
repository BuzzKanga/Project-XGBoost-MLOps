setup_monitoring:
	mkdir monitoring
	cd monitoring
	pipenv install -r requirements.txt
	mkdir config
	docker-compose up --build

	conda create -n p11 python=3.11
	conda update -n base -c defaults conda

	conda activate p11
	conda deactivate

	