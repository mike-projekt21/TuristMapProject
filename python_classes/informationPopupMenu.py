from kivy.uix.gridlayout import GridLayout
from kivymd.uix.dialog import MDDialog
from kivy.uix.image import Image
from kivymd.uix.button import MDIconButton
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout

class Content(ScrollView):
    def __init__(self, attraction_data, **kwargs):
        super().__init__(**kwargs)
        gl_out = GridLayout(cols = 1, spacing = 10, padding = 10)
        image = Image(source = attraction_data[2], size_hint = (.9,.4))
        bl_title = MDBoxLayout(orientation = "horizontal", spacing = 10, size_hint = (.9,.2))
        like_button = MDIconButton(icon = "heart-plus")
        title = Label(text = attraction_data[1], bold = True, color = "black", size_hint = (.7,.1))
        info_text = Label(text = attraction_data[3], color = "black", size_hint = (.9,.4))

        bl_title.add_widget(title, like_button)
        gl_out.add_widget(image, bl_title, info_text)
        self.add_widget(gl_out)

class InformationPopupMenu(MDDialog):
    def __init__(self, attraction_data, **kwargs):
        super().__init__(**kwargs)
        self.name = attraction_data[1]
        self.address = attraction_data[2]
        self.image_source = "resources/" + attraction_data[5]
        self.info = attraction_data[6]

        self.title = self.name
        self.text = self.info
#        self.type = "custom"
#        self.content_cls = Content((self.name,self.address,self.image_source,self.info))
        """
        scroll = ScrollView()
        gl_out = GridLayout(cols = 1, spacing = 10, padding = 10)
        image = Image(source = self.image_source, size_hint = (.9,.4))
        bl_title = MDBoxLayout(orientation = "horizontal", spacing = 10, size_hint = (.9,.2))
        like_button = MDIconButton(icon = "heart-plus")
        title = Label(text = self.name, bold = True, color = "black", size_hint = (.7,.1))
        info_text = Label(text = self.info, color = "black", size_hint = (.9,.4))

        bl_title.add_widget(title, like_button)
        gl_out.add_widget(image, bl_title, info_text)
        scroll.add_widget(gl_out)
        """

