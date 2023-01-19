## Pre-requisites
Docker
Python 3.10

## Local Installation
python -m venv env
. env/bin/activate (mac)
or
.\\env\\Scripts\\activate (windows)
pip install -r requirements.txt
python -m app.main

See docs at http://127.0.0.1:8000/docs
See users endpoint at http://127.0.0.1:8000/api/v1/users/{int:id}

## Docker Installation
Note: I've been unable to get Docker working on Windows due to Docker limitations on my hardware :/ Instructions work theoretically but are untested

docker image build --tag fastapi-app-image .
docker container run --publish 80:80 --name fastapi-app-container fastapi-app-image

See docs at http://localhost:80/docs
See users endpoint at http://localhost:80/api/v1/users/{int:id}

## Tests
Activate virtualenv
pip install pytest
pytest
