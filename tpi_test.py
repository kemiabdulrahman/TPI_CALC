import kivy
from kivy.core import window
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.textinput import TextInput, Window
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

Window.clearcolor = (1,1,1,1)
Window.size = (360, 600)

class Tpi_Calc(Widget):
    pass

    def btn(self):
        pass


class Tpi(App):
    def build(self):
        return Tpi_Calc()

if __name__ == "__main__":
    Tpi().run()
