import os
from unicodedata import numeric

from app.services.json_manipulation import load_json_file, write_json_file




class Person:
    def __init__(self, nome:str, email:str) -> None:
        self.nome = nome.capitalize()
        self.email = email.lower()
        
    @staticmethod
    def get_persons(filepath:str) -> list[dict]:
       return load_json_file(filepath)

    def create_file(self, filepath: str):
        return write_json_file(filepath, self.__dict__)
    @staticmethod
    def generate_id(id:int):
        ...