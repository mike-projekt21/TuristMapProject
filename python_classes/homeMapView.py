from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivymd.app import MDApp
import sqlite3

class HomeMapView(MapView):
    getting_markers_timer = None

    def start_getting_markers(self):
        # After one second, place markers in the fild of view
        try:
            self.getting_markers_timer.cancel()
        except:
            pass
        self.getting_markers_timer = Clock.schedule_once(self.get_markers, 1)

    def get_markers(self, *args):
        #Get reference to main app and database
        app = MDApp.get_running_app()
        sql_statement = """SELECT * FROM attractions 
                        WHERE x > ? AND x < ? AND y > ? AND y < ?"""
        app.cursor.execute(sql_statement, self.get_bbox())
        attractions = app.cursor.fetchall()
        print(attractions)
