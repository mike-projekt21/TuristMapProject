from kivy_garden.mapview import MapView
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (375, 750)

class SearchScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class MainApp(MDApp):

    def build(self):
        return Builder.load_file('markup_files/main.kv')

    def change_screen(self, screen, direction):
        screen_manager = self.root.ids.screen_manager
        screen_manager.current = screen
        screen_manager.transition.direction = direction

if __name__ == "__main__":
    MainApp().run()
