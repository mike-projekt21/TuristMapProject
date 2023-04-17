from kivy_garden.mapview import MapMarkerPopup
from python_classes.informationPopupMenu import InformationPopupMenu
class AttractionMarker(MapMarkerPopup):
    attraction_data = []

    def on_release(self, *args):
        menu = InformationPopupMenu(self.attraction_data)
        menu.size_hint = [.8,.7]
        menu.background_color = "white"
        menu.open()