from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.config import Config
Config.set('graphics','resizable','0')#зафиксировать размер окна его нельзя менять
Config.set('graphics','height','100')#высота
Config.set('graphics','width','410')
class Ошибка(App):
    def build(self):
        bl=BoxLayout(orientation="vertical")
        self.k=Label(text="Ошибка",size_hint=(1,.3))
        bl.add_widget(self.k)
        self.k1=Label(text="Количество лживых шифров должно быть",size_hint=(1,.2))
        bl.add_widget(self.k1)
        self.k2=Label(text="больше номера реального шифра",size_hint=(1,.2))
        bl.add_widget(self.k2)
        return bl
if __name__=="__main__":
    Ошибка().run()
