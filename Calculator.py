from os import name
import kivy
from kivy.uix.gridlayout import GridLayout, ObjectProperty
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget




class MyGrid(Widget):
    pass
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def pressed(self):
        print(f"Name: {self.name.text} Email:{self.email.text}")
        self.name.text = ""
        self.email.text = ""



class Calc(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    Calc().run()



