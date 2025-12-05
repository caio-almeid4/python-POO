from abc import ABC, abstractmethod


class Device(ABC):
    
    
    @abstractmethod
    def turn_on():
        ...
        

class motorola(Device):
    
    def turn_on(self):
        print('Hello, Moto!')
        
    @abstractmethod
    def turn_off(self):
        print('Turning off')
        
    @staticmethod
    def teste(a, b):
        print(f'teste: {a+b}')