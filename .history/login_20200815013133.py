import sqlite3
import PySimpleGUI as sg

class User(object):
    
    def __init__(self):
        self.register = [
            [sg.Text('Register user')],
            [sg.Text('User name'),sg.InputText('')],
            [sg.Text('Password'),sg.Input('',key='Password', password_char='*')],
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

        self._scream_login()

        if self.event == 'Register':
            self._scream_register()
            if self.event == 'Submit':
                self._register()
            elif self.event == 'Back':
                self._scream_login()

        elif self.event == 'Login':
            self._login()


    def _register(self):    
        pass

    def _login(self):
        pass

    def _scream_register(self):
        self.window = sg.Window('Login System', layout=self.register)
        self.event, self.values = self.window.Read()

    
    def _scream_login(self):
        self.window = sg.Window('Login System', layout=self.login)
        self.event, self.values = self.window.Read()


user = User()
user.start()