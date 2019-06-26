import math
import tkinter
okno = tkinter.Tk()
ekran=tkinter.Text(okno,state='disabled',height=2,width=27)

#ekran.config(height=2,width=27)
ekran.grid(row=0,column=0,columnspan=5,pady=5)

def usun():
    ekran.configure(state='normal')
    ekran.delete(1.0, tkinter.END)
    ekran.configure(state='disabled')


def wydobadz():
    return ekran.get("1.0",tkinter.END)

def wprowadz(wartosc):
    #ekran.delete('1.0',END)
    ekran.configure(state='normal')
    ekran.insert(tkinter.END,wartosc)
    ekran.configure(state='disabled')

def dodaj():
    x=wydobadz()
    for i in range(len(x)-1):
        if x[i].isdigit()==False and x[i]!='.':
            break
        if i==len(x)-2:
            wprowadz("+")
            break
def odejmij():
    x=wydobadz()
    for i in range(len(x)-1):
        if x[i].isdigit()==False and x[i]!='.':
            break
        if i==len(x)-2:
            wprowadz("-")
            break
def pomnoz():
    x=wydobadz()
    for i in range(len(x)-1):
        if x[i].isdigit()==False and x[i]!='.':
            break
        if i==len(x)-2:
            wprowadz("*")
            break
def podziel():
    x=wydobadz()
    for i in range(len(x)-1):
        if x[i].isdigit()==False and x[i]!='.':
            break
        if i==len(x)-2:
            wprowadz("/")
            break
def procent():
    x=wydobadz()
    if isinstance(float(x),float):
        x=float(x)*0.01
        usun()
        wprowadz(x)
    else:
        usun()
        wprowadz("NaN")

def pierwiastkuj():

    x=math.sqrt(float(wydobadz()))
    
    if isinstance(int(x), int) or isinstance(float(x),float):
        usun()
        wprowadz(x)
    else:
        usun()
        wprowadz("NaN")
def rownasie():
    input=wydobadz()
def jeden():
    wprowadz("1")
def dwa():
    wprowadz("2")
def trzy():
    wprowadz("3")
def cztery():
    wprowadz("4")
def piec():
    wprowadz("5")
def szesc():
    wprowadz("6")
def siedem():
    wprowadz("7")
def osiem():
    wprowadz("8")
def dziewiec():
    wprowadz("9")
def zero():
    wprowadz("0")
def przecinek():
    x=wydobadz()
    if len(x)<3:
        usun()
        x= x[0] + '.'
    elif len(x)>3:
       usun()
       x= x[:len(x)-1]+'.'
    wprowadz(x)

def rownasie():
    x=ekran.get("1.0",tkinter.END)
    for i in range(len(x)):
        if x[i].isdigit() or x[i]=='.':
            continue
        else:
            pierwszaliczba = x[:i]
            drugaliczba=x[i+1:]
            znak=x[i]
            break
    if znak=='+':
        wynik=float(pierwszaliczba)+float(drugaliczba)
    elif znak=='-':
        wynik=float(pierwszaliczba)-float(drugaliczba)
    elif znak=='*':
        wynik=float(pierwszaliczba)*float(drugaliczba)
    elif znak=='/':
        wynik=float(pierwszaliczba)/float(drugaliczba)
    usun()
    wprowadz(wynik)
    
p1 = tkinter.Button(okno,text="1", command=lambda: jeden())
p1.config(height=3,width=7)
p2 = tkinter.Button(okno,text="2", command=lambda: dwa())
p2.config(height=3,width=7)
p3 = tkinter.Button(okno,text="3", command=lambda: trzy())
p3.config(height=3,width=7)
p4 = tkinter.Button(okno,text="4", command=lambda: cztery())
p4.config(height=3,width=7)
p5 = tkinter.Button(okno,text="5", command=lambda: piec())
p5.config(height=3,width=7)
p6 = tkinter.Button(okno,text="6", command=lambda: szesc())
p6.config(height=3,width=7)
p7 = tkinter.Button(okno,text="7", command=lambda: siedem())
p7.config(height=3,width=7)
p8 = tkinter.Button(okno,text="8", command=lambda: osiem())
p8.config(height=3,width=7)
p9 = tkinter.Button(okno,text="9", command=lambda: dziewiec())
p9.config(height=3,width=7)
p0 = tkinter.Button(okno,text="0", command=lambda: zero())
p0.config(height=3,width=7)
pplus = tkinter.Button(okno,text="+", command=lambda: dodaj())
pplus.config(height=3,width=7)
pminus = tkinter.Button(okno,text="-", command=lambda: odejmij())
pminus.config(height=3,width=7)
prownasie = tkinter.Button(okno,text="=", command=lambda: rownasie())
prownasie.config(height=11,width=7)
pmnozenie = tkinter.Button(okno,text="*", command=lambda: pomnoz())
pmnozenie.config(height=3,width=7)
pdzielenie = tkinter.Button(okno,text="/", command=lambda: podziel())
pdzielenie.config(height=3,width=7)
pprzecinek = tkinter.Button(okno,text=",", command=lambda: przecinek())
pprzecinek.config(height=3,width=7)
pprocent = tkinter.Button(okno,text="%", command=lambda: procent())
pprocent.config(height=3,width=7)
ppierwiastek = tkinter.Button(okno,text="√", command=lambda: pierwiastkuj())
ppierwiastek.config(height=3,width=7)
pusun=tkinter.Button(okno,text="C", command=lambda: usun())
pusun.config(height=3,width=7)
p9.grid(row=1,column=0)
p8.grid(row=1,column=1)
p7.grid(row=1,column=2)
p6.grid(row=2,column=0)
p5.grid(row=2,column=1)
p4.grid(row=2,column=2)
p3.grid(row=3,column=0)
p2.grid(row=3,column=1)
p1.grid(row=3,column=2)
p0.grid(row=4,column=0)
pdzielenie.grid(row=1,column=3)
ppierwiastek.grid(row=4,column=2)
pmnozenie.grid(row=2,column=3)
pprocent.grid(row=2,column=4)
pminus.grid(row=3,column=3)
pplus.grid(row=4,column=3)
prownasie.grid(row=2,column=4,rowspan=3)
pusun.grid(row=1,column=4)
pprzecinek.grid(row=4,column=1)
okno.mainloop()
