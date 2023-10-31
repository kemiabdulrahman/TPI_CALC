from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (310, 580)

class MyRoot(FloatLayout):
    def button_value(self, number):
        prev_number = self.ids.calc_field.text
        if prev_number == '0':
            self.ids.calc_field.text = f"{number}"
        else:
            self.ids.calc_field.text = f"{prev_number}{number}"

    def clear(self):
        self.ids.calc_field.text = "0"

    def signs(self, sign):
        prev_number = self.ids.calc_field.text
        self.ids.calc_field.text = f"{prev_number}{sign}"

    def remove_last(self):
        prev_number = self.ids.calc_field.text
        prev_number = prev_number[:-1]  # Fix to remove last character
        self.ids.calc_field.text = prev_number

    def display_result(self):
        prev_number = self.ids.calc_field.text
        try:
            result = eval(prev_number)
            self.ids.calc_field.text = str(result)
        except:
            self.ids.calc_field.text = "Undefined"

    def positive_negative(self):
        prev_number = self.ids.calc_field.text
        if '-' in prev_number:
            self.ids.calc_field.text = prev_number.replace('-', '')
        else:
            self.ids.calc_field.text = f"-{prev_number}"

    def dot(self):
        prev_number = self.ids.calc_field.text
        if '.' not in prev_number:  # Avoid adding multiple dots
            self.ids.calc_field.text = f"{prev_number}."


class MyApp(App):
    def build(self):
        return MyRoot()

if __name__ == "__main__":
    MyApp().run()

