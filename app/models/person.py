import os
from http import HTTPStatus
from app.services.json_manipulation import load_json_file, write_json_file
from app.services.person_service import check_email_exist
from excecoes.email_verify_error import EmailVerifyError




class Person:

    def __init__(self, nome:str, email:str) -> None:
        self.nome = nome.capitalize()
        self.email = email.lower()
                
    @staticmethod
    def get_persons(filepath:str) -> list[dict]:
       return load_json_file(filepath)

    def create_file(self, filepath: str):
        person = self.__dict__

        if check_email_exist(filepath, person["email"]):
            raise EmailVerifyError

        return write_json_file(filepath, self.__dict__)

    def create_id(self,filepath:str, id:int = 1):
        person_list = load_json_file(filepath)
        self.id = id
        for person in person_list:
            self.id += 1

