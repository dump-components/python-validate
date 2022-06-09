import sys

from .validation import validation_type, valid_keys_content
from .content.keys import keys

class TaskValidation:
    
    def __init__(self, content) -> None:
        self.__content = content
        self.is_valid_keys()
        self.__token = self.__valid("token")
        self.__id = self.__valid("id")
        self.__type = self.__valid("type")
        self.__data = self.__data_task()


    def __valid(self, key):
        return validation_type(str, self.__content.get(key, "não foi possivel encontrar no conteudo da tarefa"))

    @property
    def get(self):
        return self.__data
    
    def __data_task(self):
        return {
            "token": self.__token,
            "id": self.__id,
            "type": self.__type,
        }

    def __defined_files(self, name_file, files_data):
        if name_file in files_data[0].values():
            return (files_data[0], files_data[1])
        return (files_data[1], files_data[0])
    
    def __insert_keys_content_in_list(self):
        keys = []
        for key in self.__content.keys():
            keys.append(key)
        return keys
            
    def is_valid_keys(self):
        keys_to_valid = self.__insert_keys_content_in_list()
        if valid_keys_content(keys_to_valid, keys):
            return True
        sys.exit(f"não existe a chave {keys_to_valid} vinda no payload")