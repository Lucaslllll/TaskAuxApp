from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.properties import ListProperty




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


# fazer um botão sem ser no .kv
class Botao(ButtonBehavior, Label):
    cor = ListProperty([0.1, 0.5, 0.7, 1])
    cor2 = ListProperty([0.1, 1, 0.2, 1])

    def __init__(self, **kwargs):
        # herdará de buttonbehavior e label
        super(Botao, self).__init__(**kwargs)
        self.atualizar()


    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()


    def on_press(self, *args):
        # atribuição simutânea
        self.cor, self.cor2 = self.cor2, self.cor

    def on_release(self, *args):
        self.cor = self.cor2

    # no momento que eu crio uma variavel ela tambem ganha sua função de evento
    def on_cor(self, *args):
        self.atualizar()

    def atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.cor)
            Ellipse(size=(self.height, self.height),
                    pos=(self.pos)
                )
            Ellipse(size=(self.height, self.height),
                    pos=(self.x+self.width-self.height, self.y)
                )
            Rectangle(size=(self.width-self.height, self.height),
                      pos=(self.x+self.height/2.0, self.y)
                )



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




# <Botao@ButtonBehavior+Label>:
#     canvas.before:
#         Color:
#             rgba: 0.2, 0.6, 0.3, 1
#         Ellipse:
#             pos: self.pos
#             size: self.height, self.height
#         Ellipse:
#             pos: self.x+self.width-self.height, self.y
#             size: self.height, self.height
#         Rectangle:
#             pos: self.x + self.height/2.0, self.y
#             size: self.width-self.height, self.height