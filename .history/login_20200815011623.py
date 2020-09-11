import sqlite3
import PySimpleGUI as sg

class User(object):
    
    def __init__(self):
        self.register = [
            [sg.Text('Register user')],
            [sg.Text('User name'),sg.Input('')],
            [sg.Text('Password'),sg.Input()],
            [sg.Button('Submit'),sg.Exit()]
        ]

        self.login = [
            [sg.Text('Login System')],
            [sg.Text('User'),sg.Input()],
            [sg.Text('password'),sg.Input()],
            [sg.Button('Login'),sg.Button('Register')],
            [sg.Exit()]
        ]


    def start(self):

        

        self.window = sg.Window('Login System', layout=login)

        self.event, self.values = self.window.Read()

        if self.event == 'Register':
            pass
        elif self.event == 'Logn':
            pass


    def _register(self):    



user = User()
user.start()