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
    try:
        my_dict = dict(**request.get_json())
        if type(my_dict["nome"]) != str or type(my_dict["email"]) != str:
            return {"msg": "invalid type"}, HTTPStatus.BAD_REQUEST
        else:
            data = Person(**my_dict)
        Person.create_id(data, path_route)
        return data.create_file(path_route), HTTPStatus.CREATED
    except EmailVerifyError:
        return {"msg": 'invalid insert value for email'}, HTTPStatus.CONFLICT
        
    

