from kivy.app import App
from kivy.uix.boxlayout import BoxLayout



class Tarefas(BoxLayout):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs) # para a herança funcionar 
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))

    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.texto.text = ""


class Tarefa(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text


class FrontAdmin(App):
    def build(self):
        return Tarefas(['Fazer Compras', 'Buscar Filho', 'Molhar a Calçada', 'iu', 'viva', 'alegria'])

        
FrontAdmin().run()
