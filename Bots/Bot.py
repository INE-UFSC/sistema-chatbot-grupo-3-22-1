from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome: str, comandos: dict):
        self.__nome = nome
        self.__comandos = comandos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    def mostra_comandos(self):
        string_retorno = ""
        for key, value in self.__comandos.items():
            string_retorno += f"{key} - {value}\n"
    
        return string_retorno

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass