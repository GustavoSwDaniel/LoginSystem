import sqlite3
import PySimpleGUI as sg

class User(object):
    
    def __init__(self):
        self.__user = ''
        self.__passaword = ''

    def iniciar(self):

        layout = [
            [sg.Text('Register user')],
            [sg.Input('')],
            [sg.Text('Password')],
            [sg.Input()]
            [sg.Button('Submit'),sg.Exit()]
        ]