

""" ABSTRACTION"""
" Hiding implementaion details and showing  essential features"

from abc import ABC, abstractmethod

class Editor(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def debug(self):
        pass

class Vscode(Editor):

    def start(self):
        print("start")

    def stop(self):
        print("stop")
        
    def debug(self):
        print("debug")

vscode_instance = Vscode()

vscode_instance.start()
        


    

