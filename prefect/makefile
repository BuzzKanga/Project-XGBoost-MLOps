install:
	pipenv shell

	# install prefect
	pipenv install -U prefect

	# intsall flask
	pipenv install flask

	# install gunicorn
	pipenv install gunicorn
	gunicorn --bind=0.0.0.0:9696 xgb_predict:app
