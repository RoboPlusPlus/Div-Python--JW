from kivy.app import App
from kivy.uix.label import Label # En Label kan også fungere som en knapp eller lignende
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

import kivy
"""
Login screen


"""

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.col_default_width = 100
        self.cols = 2
        self.rows = 5
        #self.rows =2
        self.add_widget(Label(text="Username: "))
        self.username = TextInput(multiline =False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Password: "))
        self.password = TextInput(multiline =False, password= True) #Gjør at skrevet text blir usynelig
        self.add_widget(self.password)

        self.add_widget(Label(text="Two factor auth: "))
        self.twoFactAuth = TextInput(multiline =False, password= True) #Gjør at skrevet text blir usynelig
        self.add_widget(self.twoFactAuth)


class SimpleKivy(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    SimpleKivy().run()


