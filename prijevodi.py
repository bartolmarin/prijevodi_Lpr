#Ovo je GUI verzija programa. Razlika od običnog je što ovoj verziji nedostaje 
# Ne nedostaje - izgradnja fajla u koji će se zapisivati rješenja kao !: Zadatak, 2. Zadatak itd.
#Nije više  Problem je što ovaj program nije u petlji kao prethodni nego se svaki put ponovo pokreće
# ZA NAPRAVITI:
#Rijepeno  1. da možeš stvoriti fajl u koji će se zapisivati odgovori a ne samo na prozor
#RIjepeno 2. napraviti program u petlji, bez restartanja (i zbog 1.)
#Riješeno 3. napraviti ljepši prozor, možda u onom customtkinteru ili neš slično...
#Riješeno  4. napraviti prozor koji će te prvo pitati Igra1(prijevodi na) ili Igra2(prijevodi sa), a onda odabrati igru (dakako, prije toga prvi prozor ti daje mogućnost stvaranja fajla!
#Riješeno 5. napraviti da reagira na Enter ili Tab a ne na gumb!
import sys #za restartanje programa
import os #za relativni path u koji će se spremati testovi
from random import * #za nasumičan odabir zadatka
from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


prozor=customtkinter.CTk()
prozor.geometry("1200x800")
prozor.title('Prijevodi')

o1=customtkinter.CTkLabel(prozor,text="Prijevodi na i sa jezika logike prvog reda", text_font=("Roboto",20))
o1.place(x=350,y=50)
o2=customtkinter.CTkLabel(prozor,text="Zadana je rečenica:", text_font=("Roboto",12))
o2.place(x=50,y=300)
ob=customtkinter.CTkLabel(prozor,text="Napišite prijevod rečenice koja je zadana, pa <Enter>: ", text_font=("Roboto",12))
ob.place(x=50, y=350)
b=customtkinter.CTkEntry(prozor,width=300, text_font=("Roboto",12))
b.place(x=450,y=350)
o3=customtkinter.CTkLabel(prozor,text="Vaš odgovor:", text_font=("Roboto",12), justify="left")
o3.place(x=40,y=400)
o4=customtkinter.CTkLabel(prozor,text="Očekivani odgovor:", text_font=("Roboto",12))
o4.place(x=50,y=450)

ozadatak=customtkinter.CTkLabel(prozor,text='')
ozadatak.place(x=250,y=300)
oodgovor=customtkinter.CTkLabel(prozor,text='')
oodgovor.place(x=310,y=400)
oocekivano=customtkinter.CTkLabel(prozor,text='')
oocekivano.place(x=310,y=500)
o0=customtkinter.CTkLabel(prozor, text="Napišite ime fajla u koji želite spremiti rezultate (na kraju stitnite <Enter>)", text_font=("Roboto",10))
o0.place(x=50, y=120)
mojfajl=customtkinter.CTkEntry(prozor,width=200, text_font=("Roboto",10))
mojfajl.place(x=650,y=120)

#Otvori dva dokumenta iz kojih uzimaš retke
k=open('kvantificirane.txt', 'r')
sadrzajk=k.read()
o=open('obicne.txt', 'r')
sadrzajo=o.read()
    






def brisi():
    mojfajl.place_forget()
    o0.place_forget()

fajl=str()

def upis():
    global fajl
    global f
    fajl=mojfajl.get()
    fajl=str(fajl)+str(".txt")
    f=open(os.path.join('./testovi', fajl), 'a')
#    f=open(fajl, 'a')

    if fajl[-1]=="t":
        brisi()

mojfajl.bind('<Return>',lambda event: upis())

brojac=0

def lprnaobicni():
    def glavno():
        global fajl
        global f
        global ozadatak
        global oodgovor
        global oocekivano
        #brojač broji broj klikova na PritisniMe i time numerira zadatke u dokumentu
        global brojac
        brojac=brojac + 1

        oodgovor.place_forget()
        oocekivano.place_forget()
        ozadatak.place_forget()
        global odaberi
        global zadatak
        odaberi=randint(1,122)
        lista1=[]
        lista1=list(map(str,sadrzajk.splitlines()))
        zadatak=lista1[odaberi]
        ozadatak=customtkinter.CTkLabel(prozor,text=str(zadatak), text_font=("Roboto",12))
        ozadatak.place(x=450,y=300)

        #Upisuje se u odabrani dokument u ./testovi/mojfajl.txt
        f.write('\n\n\n' + str(brojac) +". ZADATAK"+'\n\n')
        f.write(str(zadatak)+'\n')

    def rezultat():    
        #Ovo više ne znam trebaju li mi ove iste globalne varijable u glavno(). Sad se briše stari ulaz nakon što se pokrene glavno() s novim zadatkom
        global fajl
        global f
        global oodgovor
        global oocekivano
        oodgovor.place_forget()
        oocekivano.place_forget()

        odgovor=str(b.get())
        oodgovor=customtkinter.CTkLabel(prozor,text=str(odgovor), text_font=("Roboto",12))
        oodgovor.place(x=450,y=400)
        #Upisuje u fajl
        f.write("Vaš odgovor je: "+ "\""+str(odgovor)+"\""+'\n')
        #Traži očekivani odgovor
        lista2=list(map(str,sadrzajo.splitlines()))
        ocekivaniOdgovor=lista2[odaberi]

        oocekivano=customtkinter.CTkLabel(prozor,text=str(ocekivaniOdgovor), text_font=("Roboto",12))
        oocekivano.place(x=450,y=450)
        #Piše očekivani odgovor
        f.write("Očekivani odgovor je: "+ str(ocekivaniOdgovor) +'\n\n\n')
        
        b.delete(0,END)
    def zavrsi():
        global f
        f.write('\n\n\n'+"============ Kraj ============= "+'\n\n\n')
    z=customtkinter.CTkButton(prozor, text="PritisniMe", command=glavno)
    z.place(x=900,y=300)
#    g=customtkinter.CTkButton(prozor, text="Priloži rješenje", command=rezultat)
#    g.place(x=900,y=350)
    kraj=customtkinter.CTkButton(prozor, text="Ako ti  je dosta, prvo mene stisni pa utipkaj 'q'!", command=zavrsi)
    kraj.place(x=100,y=700)
    #Ovo bi trebalo nakon <Return> pokrenuti glavno() ili rezultat(), ne znam... u svakom slučaju, da ne klikamo gumb, nego tipke
    b.bind('<Return>',lambda event: rezultat())


    prozor.bind('q', lambda event:prozor.destroy()) 


def obicninalpr():
    def glavno():
        global fajl
        global f
        global ozadatak
        global oodgovor
        global oocekivano
        #brojač broji broj klikova na PritisniMe i time numerira zadatke u dokumentu
        global brojac
        brojac=brojac + 1

        oodgovor.place_forget()
        oocekivano.place_forget()
        ozadatak.place_forget()
        global odaberi
        global zadatak
        odaberi=randint(1,122)
        lista1=[]
        lista1=list(map(str,sadrzajo.splitlines()))
        zadatak=lista1[odaberi]
        ozadatak=customtkinter.CTkLabel(prozor,text=str(zadatak), text_font=("Roboto",12))
        ozadatak.place(x=450,y=300)

        #Upisuje se u odabrani dokument u ./testovi/mojfajl.txt
        f.write('\n\n\n' + str(brojac) +". ZADATAK"+'\n\n')
        f.write(str(zadatak)+'\n')

    def rezultat():    
        #Ovo više ne znam trebaju li mi ove iste globalne varijable u glavno(). Sad se briše stari ulaz nakon što se pokrene glavno() s novim zadatkom
        global fajl
        global f
        global oodgovor
        global oocekivano
        oodgovor.place_forget()
        oocekivano.place_forget()

        odgovor=str(b.get())
        odgovor=list(map(str,odgovor.split()))
        for j in range(len(odgovor)):
            if odgovor[j]=='svi':
                odgovor[j]='∀'
            elif odgovor[j]=='postoji':
                odgovor[j]='∃'
            elif odgovor[j]=='i':
                odgovor[j]='∧'
            elif odgovor[j]=='ili':
                odgovor[j]='∨'
            elif odgovor[j]=='samoako':
                odgovor[j]='→'
            elif odgovor[j]=='ne':
                odgovor[j]='¬'
            elif odgovor[j]=='akoisamoako':
                odgovor[j]='↔'
            elif odgovor[j]=='nejed':
                odgovor[j]='≠'
        odgovor=''.join(odgovor)
        oodgovor=customtkinter.CTkLabel(prozor,text=str(odgovor), text_font=("Roboto",12))
        oodgovor.place(x=450,y=400)
        #Upisuje u fajl
        f.write("Vaš odgovor je: "+ "\""+str(odgovor)+"\""+'\n')
        #Traži očekivani odgovor
        lista2=list(map(str,sadrzajk.splitlines()))
        ocekivaniOdgovor=lista2[odaberi]

        oocekivano=customtkinter.CTkLabel(prozor,text=str(ocekivaniOdgovor), text_font=("Roboto",12))
        oocekivano.place(x=450,y=450)
        #Piše očekivani odgovor
        f.write("Očekivani odgovor je: "+ str(ocekivaniOdgovor) +'\n\n\n')
        
        b.delete(0,END)
    def zavrsi():
        global f
        f.write('\n\n\n'+"============ Kraj ============= "+'\n\n\n')
    z=customtkinter.CTkButton(prozor, text="PritisniMe", command=glavno)
    z.place(x=900,y=300)
    #g=customtkinter.CTkButton(prozor, text="Priloži rješenje", command=rezultat)
    #g.place(x=900,y=350)
    kraj=customtkinter.CTkButton(prozor, text="Ako ti  je dosta, prvo mene stisni pa utipkaj 'q'!", command=zavrsi)
    kraj.place(x=100,y=700)
    #Ovo bi trebalo nakon <Return> pokrenuti glavno() ili rezultat(), ne znam... u svakom slučaju, da ne klikamo gumb, nego tipke
    b.bind('<Return>',lambda event: rezultat())


    prozor.bind('q', lambda event:prozor.destroy()) 

    

    
    #UPUTE ZA UNOS SIMBOLA - dolje desno

    kljuc=customtkinter.CTkLabel(prozor,text='Ključ upisivanja:',text_font=("Roboto",8))
    kljuc.place(x=850,y=400)
    svi=customtkinter.CTkLabel(prozor,text='svi = ∀',text_font=("Roboto",8))
    svi.place(x=950,y=430)
    postoji=customtkinter.CTkLabel(prozor,text='postoji = ∃',text_font=("Roboto",8))
    postoji.place(x=950,y=460)
    ne=customtkinter.CTkLabel(prozor,text='ne = ¬',text_font=("Roboto",8))
    ne.place(x=950,y=490)
    i=customtkinter.CTkLabel(prozor,text='i = ∧',text_font=("Roboto",8))
    i.place(x=950,y=520)
    ili=customtkinter.CTkLabel(prozor,text='ili = ∨',text_font=("Roboto",8))
    ili.place(x=950,y=550)
    samoako=customtkinter.CTkLabel(prozor,text='samoako = →',text_font=("Roboto",8))
    samoako.place(x=950,y=580)
    akoisamoako=customtkinter.CTkLabel(prozor,text='akoisamoako = ↔',text_font=("Roboto",8))
    akoisamoako.place(x=950,y=610)
    nejed=customtkinter.CTkLabel(prozor,text='nejed = ≠',text_font=("Roboto",8))
    nejed.place(x=950,y=610)
    primjer=customtkinter.CTkLabel(prozor,text='Primjer: "svi x svi y ((x nejed y i ne postoji zRzx) samoako (Syy ili ne ne ne Sxx))"',text_font=("Roboto",9))
    primjer.place(x=750,y=660)
    izgled=customtkinter.CTkLabel(prozor,text='Proizvodi: "∀x∀y((x≠y∧¬∃zRzx)→(Syy∨¬¬¬Sxx))"',text_font=("Roboto",9))
    izgled.place(x=750,y=690)


#Odabirenje vrste igre
lprob=customtkinter.CTkButton(prozor, height=50, width=80, text="Lpr na obični", text_font=("Roboto",13), command=lprnaobicni)
lprob.place(x=480,y=180)
oblpr=customtkinter.CTkButton(prozor, height=50 , width=80, text="Obični na Lpr",  text_font=("Roboto",13),command=obicninalpr)
oblpr.place(x=680,y=180)

prozor.mainloop()

k.close()
o.close()
