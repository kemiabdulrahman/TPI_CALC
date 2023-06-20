import kivy
from kivy.core import text
from kivy.core.text import layout_text
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image


Window.size = (360, 600)
Window.clearcolor = (1,1,1,1)



class MainApp(App):
    def build(self):
        
        layout = BoxLayout(orientation='vertical', spacing=100, padding=80)

        """
        button1 = Button(text="Button 1")
        button2 = Button(text="Button 2")
        button3 = Button(text="Button 3")
        button4 = Button(text="Button 4")          

        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)      
        """
        btn = Button(text="Login", size_hint=(None, None), pos_hint={'center_x': 0.5}, height=50, width=100)
        img = Image(source="aeroplane.jpeg")
        layout.add_widget(img)
        layout.add_widget(btn)
        return layout

MainApp().run()
