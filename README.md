# API and UI Integration demo

### Python3 installation
* Download and install Python3 from [here](https://www.python.org/downloads/)

### FastAPI
* About fastapi [link](https://fastapi.tiangolo.com/)
* pip install fastapi

### Run the uvicorn server
* python3 server.py

## Curl commands
### POST method
* curl --header 'Content-Type: application/json' --request POST --data '{"name": "satish", "surname": "manpuri"}' http://0.0.0.0:9000/user -v

### GET method
* curl --header 'Content-Type: application/json' --request GET http://0.0.0.0:9000/users -v | json_pp

### DELETE method
* curl --header "Content-Type: application/json" --request DELETE http://localhost:9000/users/satish -v

## Postman
* Postman installation [link](https://learning.postman.com/docs/getting-started/installation-and-updates/)