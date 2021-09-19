from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.config import Config
Config.set('graphics','resizable','0')#зафиксировать размер окна его нельзя менять
Config.set('graphics','height','120')#высота
Config.set('graphics','width','365')
class Ошибка(App):
    def build(self):
        bl=BoxLayout(orientation="vertical")
        self.k=Label(text="Ошибка",size_hint=(1,.3))
        bl.add_widget(self.k)
        self.k1=Label(text="Смещение для шифрования обработанного шифра",size_hint=(1,.2))
        bl.add_widget(self.k1)
        self.k2=Label(text=" шифром Цезаря должно быть не больше чем количество количеств символова в равкладке, по умолчанию это 150",size_hint=(1,.2))
        bl.add_widget(self.k2)
        return bl
if __name__=="__main__":
    Ошибка().run()
