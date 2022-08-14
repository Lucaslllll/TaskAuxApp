from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.core.audio import SoundLoader

import json



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
    def on_pre_enter(self):
        Window.bind(on_request_close=self.confirmacao)

    def on_pre_leave(self, *args):
        # self.ids.box.clear_widgets()
        pass

    def confirmacao(self, *args, **kwargs):
        box = BoxLayout(orientation="vertical", padding=10, spacing=10)
        botoes = BoxLayout(padding=10, spacing=10)
        
        pop = Popup(title="Deseja mesmo sair", content=box, size_hint=(None, None),
                    size=(150,150)
            )


        sim = Botao(text="Sim", on_release=App.get_running_app().stop)
        nao = Botao(text="Não", on_release=pop.dismiss)

        botoes.add_widget(sim)
        botoes.add_widget(nao)


        atencao = Image(source="exclamation.png")


        box.add_widget(atencao)
        box.add_widget(botoes)

        # se eu quiser uma animações paralelas inves de combina-las
        # com + posso usar &
        animText = Animation(color=(0,0,0,1)) + Animation(color=(1,1,1,1))
        animText.repeat = True
        animText.start(sim)        
      
        anim = Animation(size=(300, 180), duration=0.2, t="out_back")
        anim.start(pop)

        pop.open()



        return True 



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
    tarefas = []
    path = ''

    # esse metodo é executado antes de entrar na tela
    def on_pre_enter(self):
        self.path = App.get_running_app().user_data_dir+"/"
        self.loadData()

        Window.bind(on_keyboard=self.voltar)
        for tarefa in self.tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))
        

    def voltar(self, window, key, *args):
        # esc tem o codigo 27
        if key == 27:
            App.get_running_app().root.current = "menu_name"
            return True

        return False

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)


    def loadData(self, *args):
        # antes de carregar qualquer coisa, certamente
        # tenho que limpar o lixo de quando a tela 
        # foi carregada anteriormente
        self.ids.box.clear_widgets()

        try:
            with open(self.path+"data.json", 'r') as data:
                self.tarefas = json.load(data)
        except FileNotFoundError:
            pass


    def saveData(self, *args):
        with open(self.path+"data.json", 'w') as data:
            json.dump(self.tarefas, data)

    def removeWidget(self, tarefa):
        texto = tarefa.ids.label.text
        self.ids.box.remove_widget(tarefa)
        self.tarefas.remove(texto)
        self.saveData(self.tarefas)

    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.texto.text = ""
        self.tarefas.append(texto)
        self.saveData()

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