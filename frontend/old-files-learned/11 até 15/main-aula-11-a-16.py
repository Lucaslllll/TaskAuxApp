from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class Gerenciador(ScreenManager):
    pass


class Ajuda(Screen):



    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = "menu_name"
            return True

        return False

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)        


class Menu(Screen):
    pass



class Tarefas(Screen):
    def __init__(self, tarefas=[], **kwargs):
        super().__init__(**kwargs) # para a herança funcionar 
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))


    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        # esc tem o codigo 27
        if key == 27:
            App.get_running_app().root.current = "menu_name"
            return True

        return False

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)




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
        return Gerenciador()



FrontAdmin().run()
