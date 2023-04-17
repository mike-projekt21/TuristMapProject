from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import sqlite3

from python_classes.homeMapView import HomeMapView

Window.size = (375, 750)

class SearchScreen(Screen):
    def search_by_input(self, input_info):
        app = MDApp.get_running_app()
        app.cursor.execute("""SELECT * FROM attractions WHERE address LIKE ? or name LIKE ?""", (f"%{input_info}%", f"%{input_info}%"))
        coordinations = app.cursor.fetchall()
        app.change_screen("home","left")
        for attraction in coordinations:
            app.root.ids.home_screen.ids.map_view.add_attraction(attraction)

    def search_by_group(self, group_info):
        app = MDApp.get_running_app()
        app.cursor.execute(f"""SELECT * FROM attractions WHERE group_of_attraction == ?""", group_info)
        coordinations = app.cursor.fetchall()
        app.change_screen("home", "left")
        for attraction in coordinations:
            app.root.ids.home_screen.ids.map_view.add_attraction(attraction)

class ProfileScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class MainApp(MDApp):
    db = None
    cursor = None
    def on_start(self):
        #Connect to database
        self.db = sqlite3.connect("TouristMap.db")
        self.cursor = self.db.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS attractions (
                                id INTEGER PRIMARY KEY AUTOINCREMENT ,
                                name TEXT,
                                address TEXT,
                                x REAL,
                                y REAL,
                                image_name TEXT,
                                information TEXT,
                                group_of_attraction TEXT
                    );""")
        self.db.commit()
    def build(self):
        return Builder.load_file('markup_files/main.kv')

    def change_screen(self, screen, direction):
        self.root.ids.home_screen.ids.map_view.clean_all_markers()
        screen_manager = self.root.ids.screen_manager
        screen_manager.current = screen
        screen_manager.transition.direction = direction

if __name__ == "__main__":
    MainApp().run()
