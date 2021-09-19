from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.config import Config
Config.set('graphics','resizable','0')#зафиксировать размер окна его нельзя менять
Config.set('graphics','height','100')#высота
Config.set('graphics','width','210')
class Уведомление(App):
    def build(self):
        bl=BoxLayout(orientation="vertical")
        self.k=Label(text="Шифр успешно сгенерирован",size_hint=(1,.3))
        bl.add_widget(self.k)
        return bl
if __name__=="__main__":
    Уведомление().run()
