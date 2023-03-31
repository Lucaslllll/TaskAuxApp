from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class Tarefas(ScrollView):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs) # para a herança funcionar 
        for tarefa in tarefas:
            self.ids.box.add_widget(Label(text=tarefa, font_size=30, size_hint_y=None, height=200))



class FrontAdmin(App):
    def build(self):
        return Tarefas(['Fazer Compras', 'Buscar Filho', 'Molhar a Calçada', 'iu', 'viva', 'alegria'])

        
FrontAdmin().run()
