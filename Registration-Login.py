
from sys import audit
import kivy
from kivy.core import text
from kivy.core import window
from kivy.core.text import layout_text
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex

Window.size = (300, 600)
Window.clearcolor = (208/255, 212/255,217.255, 0.5)


class OuterBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(OuterBoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        innerboxlayout = InnerBoxLayout()

        gridboxlayout  = GridBoxLayout()



        proceed_btn = Button(text="Proceed", size_hint=(0.3, 0.2), pos_hint={'center_x':0.3, 'center_y':0.16}, background_color=get_color_from_hex('#334191'))
        submit_btn = Button(text="Submit", size_hint=(0.3, 0.2), pos_hint={'center_x':0.3,'center_y':0.16} ,background_color=get_color_from_hex('#2cfc03'))
        textinput = TextInput(multiline=True, password=True, hint_text="Type here", font_size=20, size_hint=(1, None), height=40, halign='center', font_name='Arial', foreground_color=get_color_from_hex('#524129'))

        innerboxlayout.add_widget(proceed_btn)
        innerboxlayout.add_widget(submit_btn)

        self.add_widget(textinput)
       # self.add_widget(gridboxlayout)
        self.add_widget(innerboxlayout) 
        

class InnerBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(InnerBoxLayout, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.padding = 20
        self.spacing = 10
       
"""
class GridBoxLayout(GridLayout):
    def __init__(self, **kwargs):
        super(GridBoxLayout, self).__init__(**kwargs)
        self.cols = 2
        self.spacing = 10
        self.padding = (20, 20, 30, 20)


        
        nameLabel = Label(text="NAME: ", font_size=24, color=(0.5, 0.5, 1, 1))
        nameInput = TextInput(hint_text="Enter your name ", input_type='text', font_size=24, color=(0.5, 0.5, 1, 1))
        univLabel = Label(text="UNIVERSITY: ", valign='middle', bold=True, font_size=24, color=(0.5, 0.5, 1, 1))
        univInput = TextInput(multiline=True, font_size=24)


"""


class MainApp(App):

    def build(self):
        return OuterBoxLayout()

if __name__ == '__main__':
    MainApp().run()

