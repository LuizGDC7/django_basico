activate:
	. venv/bin/activate

runserver:
	python manage.py runserver

updateVenvRequirements:
	pip freeze > requirements.txt