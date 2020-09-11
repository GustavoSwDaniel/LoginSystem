import sqlite3
import PySimpleGUI as sg

class User(object):
    
    def __init__(self):
        self.__user = ''
        self.__password = ''

    def iniciar(self):

        register = [
            [sg.Text('Register user')],
            [sg.Text('User name'),sg.Input('')],
            [sg.Text('Password'),sg.Input()],
            [sg.Button('Submit'),sg.Exit()]
        ]

        login = [
            [sg.Text('Login')],
            [sg.Text('User'),sg.Input()]
            [sg.Text('password'),sg.Input()]
        ]