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

class SnmpToolApp(App):

    btn1 = 'Cadastro'
    btn2 = 'Consulta'
    btn3 = 'Agendar'
    btn4 = 'Gerar relatório'
    btn5 = 'Limpar'
    btn6 = 'Sair'
    
    def cadastro(self):
        gerente.opt1(self,ip,community)


    def build(self):
        Window.size = (1000, 650)
        self.load_kv('main.kv')

    def set_result_form(self, resultado):
        self.root.ids.textinput_resultado.text = resultado
        print (resultado)



    def cadastro(self, ip, community):
        a = SimpleSnmp(ip, community)
        result = a.GetSNMP1()
        result = result + '\n IP ' + ip
        result = result + ' e Community ' + community



        self.set_result_form(result)





if __name__ == "__main__":
    SnmpToolApp().run()
