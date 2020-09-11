import sqlite3
import PySimpleGUI as sg

class User(object):
    
    def __init__(self):
        self.register = [
            [sg.Text('Register user')],
            [sg.Text('User name')],
            [sg.Text('Password'),sg.Input('',sg.InputText('',key='Password', password_char='*'))],
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

        self.window = sg.Window('Login System', layout=self.register)

        self.event, self.values = self.window.Read()

        if self.event == 'Register':
            self._register()
        elif self.event == 'Logn':
            self._login()


    def _register(self):    
        pass

    def _login(self):
        pass


user = User()
user.start()