from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2)

        for i in range(3):
            column_layout = BoxLayout(orientation='vertical')
            label1 = Label(text=f"column {i+1} Label 1")
            label2 = Label(text=f"column {i+2} Label 2")
            column_layout.add_widget(label1)
            column_layout.add_widget(label2)
            layout.add_widget(column_layout)
        return layout
if __name__ == "__main__":
    MyApp().run()
