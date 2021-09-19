from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.config import Config
Config.set('graphics','resizable','0')#зафиксировать размер окна его нельзя менять
Config.set('graphics','height','200')#высота
Config.set('graphics','width','310')
class Объяснение(App):
    def build(self):
        bl=BoxLayout(orientation="vertical")
        self.k=Label(text="Для лучшего шифрования,можно сделать",size_hint=(1,.3))
        bl.add_widget(self.k)
        self.k1=Label(text="так чтобы программа шифровала данные в",size_hint=(1,.2))
        bl.add_widget(self.k1)
        self.k3=Label(text="несколько слоёв это обезопасит их.",size_hint=(1,.3))
        bl.add_widget(self.k3)
        return bl
if __name__=="__main__":
    Объяснение().run()
