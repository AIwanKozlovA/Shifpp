from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
import threading
import os
import random
Config.set('graphics','height','700')#высота
Config.set('graphics','width','1350')
'''
cvb=open("ras.txt","r")
vy=cvb.read()
cvb.close()
file=open('ras.txt','r')
kolsb=file.read()
file.close()
'''
def alfa():
    fil=open("layout.txt","r", encoding='utf-8')
    layout=str(fil.read())
    fil.close()
    f=[]
    exec("f.extend("+layout+")")
    return f
    #return ['A','B','C','D','E','F','G','L','J','K','I','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','l','j','k','i','m','n','o','p','q','r','s','t','u','v','w','x','y','z','А','Б','В','Г','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я','а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',' ',',','.','<','>',':',';','?','/','!','@','#','№','$','|','%','&','*','(',')','-','+','_','=','^','0','1','2','3','4','5','6','7','8','9']
cvb=open('kwo.txt','w')
b6=len(alfa())
cvb.write(str(b6))
cvb.close()
class Shif_PPApp(App):
    def callback(self,instance, value):
        if self.ghi==False:
            self.ghi=True
        elif self.ghi==True:
            self.ghi=False
    def sg(self,args):
        alfaw=alfa()
        kwo=len(alfaw)
        kolsb=self.ns.text
        file=open('Shif/kol.txt','r')
        vb=file.read()
        file.close()
        file=open('Shif/kol.txt','w')
        file.write(kolsb)
        file.close()
        j=self.t.text
        al=[]
        #try:
        j=int(j)
        kolsb=int(kolsb)
        ma=1
        if j>1000:
            threading.Thread(target=lambda: os.system('ош1.py')).start()
        elif j>0 and j<1001:
            skr=0
            y=''
            ir=""
            p=kwo*kolsb
            for gh in range(p):
                file=open('Shif/'+str(skr)+'.txt','w')
                y=""
                for e in range(j):
                    q=random.randint(0, kwo-1)
                    y+=alfaw[q]
                if y not in al:
                    file.write(str(y))
                    file.close()
                    skr+=1
                    al.extend(y)
                else:
                    while y in al:
                        y=""
                        for e in range(j):
                            q=random.randint(0, kwo-1)
                            y+=alfaw[q]
                    file.write(str(y))
                    file.close()
                    skr+=1
                    al.extend(y)
            if int(kolsb)<int(vb):
                for z in range((int(vb)*kwo)-int(skr)):
                    try:
                        os.remove('Shif/'+str(skr)+'.txt')
                        skr+=1
                    except:
                        pass
            threading.Thread(target=lambda: os.system('увед.py')).start()
        elif j<0 or j==0 or kolsb<0:
            threading.Thread(target=lambda: os.system('ошm.py')).start()
        else:
            threading.Thread(target=lambda: os.system('ош.py')).start()
        #except:
            #threading.Thread(target=lambda: os.system('ош2.py')).start()
    def ssh(self,args):
        alfawsh=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        alfaw=alfa()
        alfator=[]
        kwo=len(alfaw)
        bws=[]
        bwsh=[]
        st=0
        br=0
        bz=0
        ma=0
        j=0
        dn=""
        file=open('Shif/kol.txt','r')
        kolsb=file.read()
        file.close()
        kolsb=int(kolsb)
        m=kwo*kolsb
        for i in range(m):
            file=open('Shif/'+str(st)+".txt","r")
            dn=file.read()
            file.close()
            if st<=kwo-1:
                alfawsh[st]=dn
            elif st>kwo-1:
                alfawsh+='6'
                alfawsh[st]=dn
            st+=1
        ft=self.ti.text
        zr=len(ft)
        file=open("зашифровано.txt","w")
        file.close()
        om=False
        pr=False
        n=0
        for iz in range(zr):
            br=0
            k=len(bws)
            if self.ghi==True:
                j=random.randint(1,kolsb)
                om=True
            else:
                for h in range(k):
                    #if k-1<0:
                    if ft[bz]== bws[h]:
                        om=True
                        pr=True
                        hk=bws[k-1]
                        if j<kolsb-1:
                            j+=1
                        elif j>=kolsb-1:
                            j=0
                        n+=1
            for e in range(kwo):
                if ft[bz]==alfaw[br]:
                    if om==False and self.ghi!=True:
                        file=open("зашифровано.txt","a")
                        file.write(alfawsh[br])
                        bws+= alfaw[br]
                        file.close()
                    else:
                        file=open("зашифровано.txt","a")
                        bb=br+(150*j)
                        if j<kolsb:
                            file.write(alfawsh[br+(kwo*(j))])
                        elif j>=kolsb:
                            file.write(alfawsh[br+(kwo*(j-1))])
                        bws+= alfaw[br]
                        file.close()
                    break
                br+=1
            om=False
            j=0
            bz+=1
        file=open("зашифровано.txt","r")
        ik=file.read()
        file.close()  
        self.tp.text=ik
        self.tp.text
    def ob(self,args):
        threading.Thread(target=lambda: os.system('ob.py')).start()
    def ob2(self,args):
        threading.Thread(target=lambda: os.system('ob2.py')).start()
    def ob3(self,args):
        threading.Thread(target=lambda: os.system('ob3.py')).start()
    def sh(self,args):
        threading.Thread(target=lambda: os.system('forin.py')).start()
    def dsh(self,args):
        threading.Thread(target=lambda: os.system('rashinsh.py')).start()
    def ssr(self,args):
        alfawsh=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        alfaw=alfa()
        ht=len(alfaw)
        print(ht)
        fz=self.ti.text
        dn=""
        kwo=len(alfaw)
        st=0
        #111
        file=open('Shif/kol.txt','r')
        kolsb=file.read()
        file.close()
        kolsb=int(kolsb)
        m=ht*kolsb
        for i in range(m):
            file=open('Shif/'+str(st)+".txt","r")
            dn=file.read()
            file.close()
            if st<=kwo-1:
                alfawsh[st]=dn
            elif st>kwo-1:
                alfawsh+='6'
                alfawsh[st]=dn
            st+=1
        st=0
        bn=0
        dn=""
        pahz=""
        yz=""
        hj=0
        file=open('Shif/kol.txt','r')
        kolsb=file.read()
        file.close()
        kolsb=int(kolsb)
        for i in range(m):
            file=open('Shif/'+str(st)+".txt","r")
            dn=file.read()
            file.close()
            alfawsh[st]=dn
            st+=1
        ul=len(alfawsh[0])
        gh=len(fz)/ul
        '''
        for z in range(kolsb):
                    print(i+(z*ht))
        '''
        for i in range(int(gh)):
            for hu in range(ul):
                yz+=fz[hj]
                hj+=1
            for i in range(m):
                if yz==alfawsh[i]:
                    pahz+=alfaw[i-(ht*int(i/ht))]
                    break
            yz=""
        file=open("раскодировано.txt","w")
        file.write(pahz)
        file.close()
        file=open("раскодировано.txt","r")
        self.tp.text=file.read()
        file.close()
    def build(self):
        self.ghi=0
        bl=BoxLayout(orientation="vertical")
        gr=GridLayout(cols=7,size_hint=(1,.1))
        self.t=TextInput(text="")
        gr.add_widget(self.t)
        gr.add_widget(Button(text="Cгенерировать",on_press=self.sg,size_hint=(1.1,.05)))
        gr.add_widget(Button(text="подготовить шифр для передачи",on_press=self.sh,size_hint=(1.1,.05)))
        gr.add_widget(Button(text="подготовить полученный шифр",on_press=self.dsh,size_hint=(1.1,.05)))
        gr.add_widget(Button(text="зашифровать",on_press=self.ssh))
        gr.add_widget(Button(text="расшифровать",on_press=self.ssr,size_hint=(1.1,.05)))
        bl.add_widget(gr)
        self.ti=TextInput()
        self.tp=TextInput()
        bl.add_widget(self.ti)
        bl.add_widget(self.tp)
        gn=GridLayout(cols=3,size_hint=(1,.12))
        self.ns=TextInput(size_hint=(0.7,1),text="1")
        gn.add_widget(Label(text="сколько составить шифров на каждую букву"))
        gn.add_widget(self.ns)
        gn.add_widget(Button(text="Не понял?",size_hint=(0.7,1),on_press=self.ob))
        bl.add_widget(gn)

        gp=GridLayout(cols=3,size_hint=(1,.12))
        gp.add_widget(Label(text="ставить варианты шифров букв в случайно"))
        switch = Switch()
        switch.bind(active=self.callback) 
        gp.add_widget(switch)
        gp.add_widget(Button(text="Не понял?",size_hint=(0.7,1),on_press=self.ob3))
        bl.add_widget(gp)
        
        return bl
if __name__=="__main__":
    Shif_PPApp().run()
