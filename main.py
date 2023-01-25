from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

Window.size = (375, 750)

class HomeScreen(Screen):
    pass

class MainApp(MDApp):

    def build(self):
        return HomeScreen()

    def on_start(self):
        pass

if __name__ == "__main__":
    MainApp().run()
