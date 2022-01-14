from flask import Flask, jsonify, request
import os
from http import HTTPStatus
from app.models.person import Person


from app.services.json_manipulation import load_json_file, write_json_file
from excecoes.email_verify_error import EmailVerifyError
app = Flask(__name__)

FOLDER_DIRECTORY = os.getenv('FOLDER_DIRECTORY')
FILENAME = os.getenv('FILENAME')
path_route = FOLDER_DIRECTORY+"/"+FILENAME

if not os.path.isdir(FOLDER_DIRECTORY):
    os.mkdir(FOLDER_DIRECTORY)

@app.get('/user')
def load_user():
    return jsonify(Person.get_persons(path_route)), HTTPStatus.OK



@app.post('/user')
def create_user():
    data = Person(**request.get_json())
    print(data)
    Person.create_id(data, path_route)
    return data.create_file(path_route), HTTPStatus.CREATED
    

