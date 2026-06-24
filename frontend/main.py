from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from kivy.factory import Factory
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, NumericProperty

# para poder fazer o teclado subir com textinput
Window.softinput_mode = 'below_target'
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemandmulti')


import json
import threading


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


class Categorias(Screen):
    pass


class Menu(Screen):
    pendentes = NumericProperty(0)
    feitas = NumericProperty(0)
    progress = NumericProperty(0)

    def on_pre_enter(self):
        Window.bind(on_request_close=self.confirmacao)
        self.atualizarResumo()

    def on_pre_leave(self, *args):
        Window.unbind(on_request_close=self.confirmacao)

    def atualizarResumo(self):
        # le os dados salvos e mostra um resumo de progresso no menu
        path = App.get_running_app().user_data_dir + "/data.json"
        dados = []
        try:
            with open(path, 'r') as f:
                dados = json.load(f)
        except (FileNotFoundError, ValueError):
            dados = []

        feitas = sum(1 for item in dados
                     if isinstance(item, dict) and item.get("feito"))
        total = len(dados)
        self.feitas = feitas
        self.pendentes = total - feitas
        self.progress = (feitas / total) if total else 0

    def confirmacao(self, *args, **kwargs):
        content = Factory.ConfirmContent()
        pop = Popup(title="", separator_height=0, background="",
                    background_color=(0, 0, 0, 0.45),
                    size_hint=(None, None), size=(dp(300), dp(210)),
                    auto_dismiss=True)
        content.ids.cancelar.bind(on_release=pop.dismiss)
        content.ids.sair.bind(on_release=lambda *a: App.get_running_app().stop())
        pop.content = content
        pop.open()
        return True


class Tarefas(Screen):
    path = ''
    popSound = None
    poppapSound = None
    _sonsIniciados = False

    # esse metodo e executado antes de entrar na tela
    def on_pre_enter(self):
        self._carregarSons()
        self.path = App.get_running_app().user_data_dir + "/"
        self.loadData()

        Window.bind(on_keyboard=self.voltar)

    def _carregarSons(self):
        # Carrega os efeitos sonoros em uma thread separada. Em alguns
        # sistemas a inicializacao do audio pode demorar (ou ate travar)
        # ao abrir o dispositivo; fazendo isso fora da thread principal a
        # interface nunca congela ao entrar nesta tela. Se o audio falhar,
        # o app continua funcionando normalmente, apenas sem os sons.
        if self._sonsIniciados:
            return
        self._sonsIniciados = True

        def _load():
            try:
                self.popSound = SoundLoader.load('assets/audios/pop.wav')
                self.poppapSound = SoundLoader.load('assets/audios/poppap.wav')
            except Exception:
                pass

        threading.Thread(target=_load, daemon=True).start()

    def voltar(self, window, key, *args):
        # esc tem o codigo 27
        if key == 27:
            App.get_running_app().root.current = "menu_name"
            return True

        return False

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    def loadData(self, *args):
        # antes de carregar qualquer coisa, limpa o que ficou da
        # ultima vez que a tela foi montada
        self.ids.box.clear_widgets()

        dados = []
        try:
            with open(self.path + "data.json", 'r') as data:
                dados = json.load(data)
        except (FileNotFoundError, ValueError):
            dados = []

        for item in dados:
            # compatibilidade: o formato antigo era uma lista de strings
            if isinstance(item, str):
                texto, feito = item, False
            else:
                texto, feito = item.get("texto", ""), item.get("feito", False)
            self.ids.box.add_widget(Tarefa(texto=texto, feito=feito))

        self.atualizarEstado()

    def coletar(self):
        # children ficam em ordem reversa de insercao, entao invertemos
        return [{"texto": w.texto, "feito": w.feito}
                for w in reversed(self.ids.box.children)]

    def saveData(self, *args):
        with open(self.path + "data.json", 'w') as data:
            json.dump(self.coletar(), data)

    def atualizarEstado(self):
        # mostra o estado vazio quando nao ha tarefas
        vazio = len(self.ids.box.children) == 0
        self.ids.empty_state.opacity = 1 if vazio else 0
        self.ids.empty_state.disabled = not vazio

    def addWidget(self):
        texto = self.ids.texto.text.strip()
        if not texto:
            return
        if self.poppapSound:
            self.poppapSound.play()
        self.ids.box.add_widget(Tarefa(texto=texto))
        self.ids.texto.text = ""
        self.saveData()
        self.atualizarEstado()

    def removeWidget(self, tarefa):
        if self.popSound:
            self.popSound.play()
        self.ids.box.remove_widget(tarefa)
        self.saveData()
        self.atualizarEstado()

    def onToggle(self):
        # chamado quando uma tarefa e marcada/desmarcada como feita
        self.saveData()


class Tarefa(BoxLayout):
    texto = StringProperty('')
    feito = BooleanProperty(False)

    def __init__(self, texto='', feito=False, **kwargs):
        super().__init__(**kwargs)
        self.texto = texto
        self.feito = feito

    def alternar(self, *args):
        self.feito = not self.feito
        App.get_running_app().root.get_screen('tarefas_name').onToggle()


class FrontAdmin(App):
    def build(self):
        return Gerenciador()


FrontAdmin().run()