from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Incrementador(BoxLayout):
    pass

class FrontAdmin(App):
    def build(self):
        return Incrementador()
    
        
FrontAdmin().run()
