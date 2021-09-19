from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.config import Config
Config.set('graphics','resizable','0')#зафиксировать размер окна его нельзя менять
Config.set('graphics','height','200')#высота
Config.set('graphics','width','775')
class Объяснение(App):
    def build(self):
        bl=BoxLayout(orientation="vertical")
        self.k=Label(text="Для лучшего шифрования,можно сделать так чтобы программа разные варианты шифровки каждой",size_hint=(1,.3))
        bl.add_widget(self.k)
        self.k1=Label(text="буквы ставила в случайном порядке при встрече.Например у буквы А три варианта шифра QQQ и ZZZ BBB.",size_hint=(1,.2))
        bl.add_widget(self.k1)
        self.k3=Label(text="И буква А может быть зашифрована либо первым вариантов вторым или третим выбор варианта шифра",size_hint=(1,.3))
        bl.add_widget(self.k3)
        self.k4=Label(text="производится случайно.Работает, если вариантов шивра больше одного.",size_hint=(1,.3))
        bl.add_widget(self.k4)
        return bl
if __name__=="__main__":
    Объяснение().run()
