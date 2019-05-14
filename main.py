import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()

'''
from kivy.app import App
from kivy.uix.widget import Widget


class DenGame(Widget):
    pass


class DenApp(App):
    def build(self):
        return DenGame()


if __name__ == '__main__':
    DenApp().run()
'''
