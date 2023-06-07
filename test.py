import kivy
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        button = Button(text="Hello Kivy!", size_hint=(.5, .5), pos_hint={'center_x':.5, 'center_y' : .5})
        button.bind(on_press=self.on_button_press)
        return button


    def on_button_press(self, instance):
        print("Button Pressed!")

if __name__ == '__main__':
    MyApp().run()
