from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.switch import Switch
import random
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
import threading
import os
#Config.set('graphics','resizable','0')#зафиксировать размер окна его нельзя менять
Config.set('graphics','width','655')
Config.set('graphics','height','825')
alfaw=['A','B','C','D','E','F','G','L','J','K','I','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','l','j','k','i','m','n','o','p','q','r','s','t','u','v','w','x','y','z','А','Б','В','Г','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я','а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',' ',',','.','<','>',':',';','?','/','!','@','#','№','$','|','%','&','*','(',')','-','+','_','=','^','0','1','2','3','4','5','6','7','8','9']
class Подготовить_для_передачи_шифр(App):
    def callback(self,instance, value):
        #print('the switch', instance, 'is', value)
        if self.ghi==False:
            self.ghi=True
        elif self.ghi==True:
            self.ghi=False
    def obrabot(self,args):
        g=open('shif/0.txt','r')
        f=len(g.read())
        g.close()
        d=random.randint(10*f,69*f)
        g=open('kwo.txt','r')
        kwo=int(g.read())
        g.close()
        g=open('shif/kol.txt','r')
        kol=int(g.read())
        g.close()
        alfaw=[]
        g=open('layout.txt','r', encoding='utf-8')
        fg=str("alfaw += "+g.read())
        g.close()
        exec(fg)
        #print(f,kwo,kol,alfaw)
        try:
            sm=int(self.ns.text)#количество лживых шифров на шифр каждой буквы
            nrsh=int(self.ns1.text)# номер реального шифра
            sme=int(self.ns2.text)#смещение шифров
            smc=int(self.ns4.text)#сдвиг для шифрования всего цезарем
            kss=int(self.ns5.text)#оличество слоёв ддля шиврования цезарем
            if sm>0 and nrsh>0 and sme>=0 and smc>=0 and kss>=0:
                if nrsh<sm:
                    if kwo*sm>sme:
                        if kwo>smc:
                            if kss<1:
                                kss=1
                            loe=[]
                            #print(loe)
                            if int(f/2)>2 and self.ghi==1:
                                self.add_sh_s=random.randint(2,int(f/2))
                            else:
                                if self.ghi==1:
                                    self.add_sh_s=random.randint(2,4)
                            if nrsh==0:
                                nrsh=1
                            b=""
                            k=[]
                            po=0
                            n=0
                            oi=""
                            vb=""
                            for e in range(kwo*kol*sm):
                                if po==sm:
                                    po=0
                                if po==nrsh:
                                    fv=open('shif/'+str(n)+'.txt','r')
                                    vb=fv.read()
                                    b+=vb
                                    fv.close()
                                    n+=1
                                    if self.ghi==1:
                                        for v in range(self.add_sh_s):
                                            rop=random.randint(0,kwo-1)
                                            b+=alfaw[rop]
                                            oi+=alfaw[rop]
                                    k.extend([vb+oi])
                                    vb=""
                                    oi=""
                                    po+=1
                                else:
                                    po+=1
                                    for jk in range(f):
                                        rop=random.randint(0,kwo-1)
                                        b+=alfaw[rop]
                                        oi+=alfaw[rop]
                                    if self.ghi==1:
                                        for v in range(self.add_sh_s):
                                            rop=random.randint(0,kwo-1)
                                            b+=alfaw[rop]
                                            oi+=alfaw[rop]
                                    k.extend([oi])
                                    oi=""
                            if sme>0:
                                for y in range(len(k)):
                                    if y+sme<len(k):
                                        loe.extend([k[y+sme]])
                                    else:
                                        #kwo-y+sme
                                        loe.extend([k[(-1*(len(k)-y))+sme]])
                                b=""
                                for l in range(len(loe)):
                                    b+=loe[l]
                            for v in range(d):
                                rop=random.randint(0,kwo-1)
                                b+=alfaw[rop]
                            gj=open('shif for shipment/шифр.txt','w')
                            gj.write(b)
                            gj.close()
                            self.ns3.text=b
                            self.kah.text=str(self.add_sh_s)
                            gl=""
                            qw=b
                            if smc>0:
                                for d in range(kss):
                                    for z in range(len(b)):
                                        for n in range(len(alfaw)):
                                            if b[z]==alfaw[n]:
                                                if n+smc<=len(alfaw)-1:
                                                    gl+=alfaw[n+smc]
                                                if n+smc>len(alfaw)-1:
                                                    #print(len(b),n)
                                                    #print(-1*(len(alfaw)-n)+smc)
                                                    gl+=alfaw[-1*(len(alfaw)-n)+smc]
                                                break
                                        
                                b=gl
                                
                            gl=""
                            if smc>0:
                                for d in range(kss):
                                    for z in range(len(b)):
                                        for n in range(len(alfaw)):
                                            if b[z]==alfaw[n]:
                                                if n-smc<=len(alfaw)-1:
                                                    gl+=alfaw[n-smc]
                                                if n-smc>len(alfaw)-1:
                                                    #print(len(b),n)
                                                    #print((len(alfaw)+n)-smc)
                                                    gl+=alfaw[(len(alfaw)+n)-smc]
                                                break
                                b=gl
                            if self.ghi==False:
                                self.add_sh_s=0
                            threading.Thread(target=lambda: os.system('увед 2.py')).start()
                            print(1111)
                        else:
                            print(1116)
                            threading.Thread(target=lambda: os.system('ош6.py')).start()
                    else:
                        print(1115)
                        threading.Thread(target=lambda: os.system('ош5.py')).start()
                else:
                    print(1114)
                    threading.Thread(target=lambda: os.system('ош4.py')).start()
            else:
                print(1113)
                threading.Thread(target=lambda: os.system('ошm.py')).start()
        except:
            print(1112)
            threading.Thread(target=lambda: os.system('ош3.py')).start()
    def build(self):
        self.ghi=0
        bl=GridLayout(cols=1, spacing=10, size_hint_y=None)
        bl.bind(minimum_height=bl.setter('height'))
        self.k=Label(text="Шифр обработанный для передачи в сети интернет сохранится в папке shif for",size_hint_y=None, height=40)
        bl.add_widget(self.k)
        self.k2=Label(text="shipment.Указанные настройки запомните и заранее обговорите их с получателем шифра",size_hint_y=None, height=40)
        bl.add_widget(self.k2)

        self.ns=TextInput(size_hint_y=None, height=40)
        bl.add_widget(Label(text="сколько составить лживых шифров на каждый реальный"))
        gr=GridLayout(cols=2,size_hint_y=None, height=40)
        gr.add_widget(self.ns)
        bl.add_widget(gr)
        self.ns1=TextInput(size_hint_y=None, height=40)
        bl.add_widget(Label(text="под каким номером из лживых шифров будет находится реальный шифр"))
        gr=GridLayout(cols=2,size_hint_y=None, height=40)
        gr.add_widget(self.ns1)
        bl.add_widget(gr)
        
        self.ns2=TextInput(size_hint_y=None, height=40,text="0")
        bl.add_widget(Label(text="смещение вариантов шифра как в шифре Цезаря"))
        gr=GridLayout(cols=2,size_hint_y=None, height=40)
        gr.add_widget(self.ns2)
        bl.add_widget(gr)

        self.ns4=TextInput(size_hint_y=None, height=40,text="0")
        bl.add_widget(Label(text="Шифрование обработаного шифра шифром Цезаря введите смещение"))
        gr=GridLayout(cols=2,size_hint_y=None, height=40)
        gr.add_widget(self.ns4)
        bl.add_widget(gr)
        
        self.ns5=TextInput(size_hint_y=None, height=40,text="0")
        bl.add_widget(Label(text="Количество слоёв шифрования обработаного шифра шифром Цезаря"))
        gr=GridLayout(cols=2,size_hint_y=None, height=40)
        gr.add_widget(self.ns5)
        bl.add_widget(gr)
        
        lk=Button(text="Обработать для передачи в сети",size_hint=(0.7,1),on_press=self.obrabot)
        gr=GridLayout(cols=2,size_hint_y=None, height=40)
        gr.add_widget(lk)
        bl.add_widget(gr)
        bl.add_widget(Label(text="Добавить к каждому варианту шифрования символа случайные символы"))
        switch = Switch(size_hint_y=None, height=40)
        switch.bind(active=self.callback) 
        bl.add_widget(switch)

        gr=GridLayout(cols=2,size_hint_y=None, height=40)
        gr.add_widget(Label(text="Количество случайных символов добавленных к каждому варианту шифрования"))
        bl.add_widget(gr)
        self.add_sh_s=0
        self.kah=Label(text=str(self.add_sh_s))
        bl.add_widget(self.kah)

        gr=GridLayout(cols=2,size_hint_y=None, height=40)
        gr.add_widget(Label(text="Количество букв на шифр каждой буквы"))
        x=open('Shif/0.txt','r')
        z=str(len(x.read()))
        x.close()
        gr.add_widget(Label(text=z))
        bl.add_widget(gr)
        
        bl.add_widget(Label(text="Обработанный шифр"))
        self.ns3=TextInput(size_hint_y=None, height=180)
        bl.add_widget(self.ns3)
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(bl)
        return root
if __name__=="__main__":
    Подготовить_для_передачи_шифр().run()
