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
class Расшифровать_полученный_шифр(App):
    def callback(self,instance, value):
        #print('the switch', instance, 'is', value)
        if self.ghi==False:
            self.ghi=True
        elif self.ghi==True:
            self.ghi=False
    def obrabot(self,args):
        try:
            f=int(self.ns7.text)
            d=random.randint(10*f,69*f)
            g=open('kwo.txt','r')
            kwo=int(g.read())
            g.close()
            kol=int(self.ns8.text)
            alfaw=[]
            g=open('layout.txt','r', encoding='utf-8')
            fg=str("alfaw += "+g.read())
            g.close()
            exec(fg)
            #print(f,kwo,kol,alfaw)
            sm=int(self.ns.text)
            nrsh=int(self.ns1.text)
            sme=int(self.ns2.text)
            smc=int(self.ns4.text)
            kss=int(self.ns5.text)
            self.add_sh_s=int(self.ns6.text)
            if sm>0 or nrsh>0 or sme>0 or smc>0 or kss>0 or self.add_sh_s>0:
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
                            b=self.ns3.text
                            k=[]
                            po=0
                            n=0
                            oi=""
                            vb=""
                            
                            if self.ghi==False:
                                self.add_sh_s=0
                            loe=[]
                            rsh=[]
                            po=0
                            ns=0
                            mv=[]
                            ks=""
                            zo=1
                            nkb=f*kol*sm*kwo#колличество символов на шифрование букв
                            krb=(len(b)-(len(b)-nkb))#оличество реальных букв
                            kshs=int(krb/kwo)#колличество букв на шифр буквы c лживыми шифрами
                            lsnb=int(kshs/sm)#колличество букв на шифр буквы
                            df=1
                            if sme>0:
                                bio=[]
                                sp=""
                                dz=0
                                for n in range(kwo*kol*sm):
                                    for i in range(f+self.add_sh_s):
                                        sp+=b[dz]
                                        dz+=1
                                    bio.extend([sp])
                                    sp=""
                                for y in range(len(bio)):
                                    if y-sme>=0:
                                        loe.extend([bio[y-sme]])
                                    else:
                                        #kwo-y+sme
                                        #len(rsh)-1*(y-sme)
                                        NU=((len(bio)+y))-sme
                                        #if y/lsnb==len(bio)-1:
                                            
                                        #print(len(bio))
                                        #print(y)
                                        #print(sme)
                                        #NU=((len(bio)-kshs)+(y)-sme)
                                        #NU=((len(bio)-1)+(y-sme))
                                        loe.extend([bio[NU]])
                                if sme>2:
                                    ui=loe[len(loe)-sm:len(loe)]
                                    del loe[len(loe)-sm:len(loe)]
                                    ui.extend(loe)
                                    loe=ui
                                #print(loe)
                                #loe.pop(0)
                                b=""
                                for p in range(len(loe)):
                                    b+=loe[p]
                            for e in range(kwo*kol):
                                for i in range(sm):
                                    for i in range(f+self.add_sh_s):
                                        ks+=b[ns]
                                        df+=1
                                        '''
                                        if self.ghi==True and df==f:
                                            ns+=self.add_sh_s
                                            df=0
                                        else:
                                            ns+=1
                                        '''
                                        ns+=1
                                    ks=ks[0:f]
                                        
                                        #print(ns)
                                    df=0
                                    mv.extend([ks])
                                    ks=""
                                #print(ks,ns,e,mv)
                                rsh.extend([mv[nrsh]])
                                mv=[]
                                ks=""
                                zo=1
                            r=""
                            if sme<3 and sme>0:
                                rsh.pop(len(rsh)-1)
                            if sme>2:
                                tr=rsh[0]
                                rsh.pop(0)
                                rsh.extend([tr])
                            for z in range(len(rsh)):
                                gh=open("shif/"+str(z)+".txt","w")
                                gh.write(rsh[z])
                                gh.close()
                            print(888)
                            gk=open("shif/kol.txt","w")
                            gk.write(str(kol))
                            gk.close()
                            threading.Thread(target=lambda: os.system('увед 2.py')).start()
                        else:
                            threading.Thread(target=lambda: os.system('ош6.py')).start()
                    else:
                        threading.Thread(target=lambda: os.system('ош5.py')).start()
                else:
                    threading.Thread(target=lambda: os.system('ош4.py')).start()
            else:
                threading.Thread(target=lambda: os.system('ошm.py')).start()
        except:
            threading.Thread(target=lambda: os.system('ош3.py')).start()
        '''
                if po==nrsh:
                    rsh+=b[e]
                    b+=fv.read()
                    fv.close()
                    po=1
                    ns+=1
                    if self.ghi==1:
                        for v in range(add_sh_s):
                            rop=random.randint(0,kwo-1)
                            b+=alfaw[rop]
                else:
                    po+=1
        '''
    def build(self):
        self.ghi=0
        bl=GridLayout(cols=1, spacing=10, size_hint_y=None)
        bl.bind(minimum_height=bl.setter('height'))
        self.k=Label(text="Расшифрованный шифр сохранится в папке shif",size_hint_y=None, height=40)
        bl.add_widget(self.k)
        self.k2=Label(text="Укажите настройки которые вы заранее обговорили с создателем шифра",size_hint_y=None, height=40)
        bl.add_widget(self.k2)

        self.ns=TextInput(size_hint_y=None, height=40)
        bl.add_widget(Label(text="сколько было составлено лживых шифров на каждый реальный"))
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
        
        lk=Button(text="Расшифровать шифр переданный из сети",size_hint=(0.7,1),on_press=self.obrabot)
        gr=GridLayout(cols=2,size_hint_y=None, height=40)
        gr.add_widget(lk)
        bl.add_widget(gr)
        bl.add_widget(Label(text="Добавляются ли к каждому варианту шифрования символа случайные символы"))
        switch = Switch(size_hint_y=None, height=40)
        switch.bind(active=self.callback) 
        bl.add_widget(switch)

        gr=GridLayout(cols=2,size_hint_y=None, height=40)
        gr.add_widget(Label(text="Количество случайных символов добавленных к каждому варианту шифрования"))
        bl.add_widget(gr)
        self.ns6=TextInput(size_hint_y=None, height=40,text="0")
        bl.add_widget(self.ns6)

        gr=GridLayout(cols=2,size_hint_y=None, height=40)
        gr.add_widget(Label(text="Количество букв на шифр каждой буквы"))
        self.ns7=TextInput(size_hint_y=None, height=40)
        gr.add_widget(self.ns7)
        bl.add_widget(gr)

        gr=GridLayout(cols=2,size_hint_y=None, height=40)
        gr.add_widget(Label(text="Количество шифров на шифр каждой буквы"))
        self.ns8=TextInput(size_hint_y=None, height=40)
        gr.add_widget(self.ns8)
        bl.add_widget(gr)
        
        bl.add_widget(Label(text="Шифр для обработки"))
        self.ns3=TextInput(size_hint_y=None, height=240)
        bl.add_widget(self.ns3)
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(bl)
        return root
if __name__=="__main__":
    Расшифровать_полученный_шифр().run()
