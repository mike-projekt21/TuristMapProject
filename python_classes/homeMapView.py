from kivy_garden.mapview import MapView
from kivy_garden.mapview import MapMarkerPopup
from kivy.clock import Clock
from kivymd.app import MDApp
from python_classes.attractionMarker import AttractionMarker
import sqlite3

class HomeMapView(MapView):
    getting_markers_timer = None
    attraction_markers = []
    """
    def start_getting_markers(self):
        # After one second, place markers in the fild of view
        try:
            self.getting_markers_timer.cancel()
        except:
            pass
        self.getting_markers_timer = Clock.schedule_once(self.get_markers, 1)
    """
    def get_markers(self, *args):
        #Get reference to main app and database
        app = MDApp.get_running_app()
        sql_statement = """SELECT * FROM attractions 
                        WHERE x > ? AND y > ? AND x < ? AND y < ?"""
        app.cursor.execute(sql_statement, self.get_bbox())
        attractions = app.cursor.fetchall()
        for attraction in attractions:
                self.add_attraction(attraction)

    def add_attraction(self, attraction):
        # Create the marker
        lat, lon = attraction[3], attraction[4]
        marker = AttractionMarker(lat = lat, lon = lon)
        marker.attraction_data = attraction
        # Add marker to the map
        self.add_widget(marker)
        # Keep track
        self.attraction_markers.append(marker)

    def clean_all_markers(self):
        for marker in self.attraction_markers:
            self.remove_marker(marker)