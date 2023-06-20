from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton




class MainApp(MDApp):

    def build(self):
        button = MDFlatButton(text="FlatButton")
        label = MDLabel(text='hello World',halign='center', theme_text_color='Error', valign='top', font_style='H6', bold=True)

        return  button

if __name__ == '__main__':
    MainApp().run()

