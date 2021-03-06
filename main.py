import kivy
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.popup import Popup
from kivy.uix.image import Image
import manager
from get import SimpleSnmp
from manager import *

class SnmpToolApp(App):

    btn2 = 'Consulta'
    btn3 = 'Agendar'
    btn4 = 'Gerar relatório'
    btn5 = 'Limpar'
    btn6 = 'Sair'

    def consulta(self,ip, community):
        manager.opt2(self,ip, community)

    def agendar(self,ip,community,time1,time2):
        manager.opt3(self,ip,community,time1,time2)

    def gera_rel(self,ip):
        manager.opt4(self,ip)

    def clean(self,ip):
        manager.opt5(self,ip)

    def build(self):
        Window.size = (1000, 650)
        self.load_kv('main.kv')

    def set_result_form(self, resultado):
        self.root.ids.textinput_resultado.text = resultado
        print (resultado)
if __name__ == "__main__":
    SnmpToolApp().run()
