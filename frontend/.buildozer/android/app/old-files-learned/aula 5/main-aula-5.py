from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Tarefas(BoxLayout):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs) # para a herança funcionar 
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa, font_size=30))



class FrontAdmin(App):
    def build(self):
        return Tarefas(['Fazer Compras', 'Buscar Filho', 'Molhar a Calçada'], orientation='horizontal')
    
        
FrontAdmin().run()
