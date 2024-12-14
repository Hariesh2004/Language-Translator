from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1100x320')
root.resizable(0,0)
root['bg'] = 'grey'
root.title('Language Translator')
Label(root,text='Language Translator', font='Arial 20 bold').pack()

Label(root,text='Enter Your Text',font='Arial 13 bold',bg='white').place(x=165, y=90)

inp_text = Entry(root,width=60)
inp_text.place(x=30, y=130)
inp_text.get()

Label(root,text='Output',font='Arial 13 bold',bg='white').place(x=780,y=90)
outpt_text=Text(root,font='Arial 10',height=5,wrap= WORD,padx=5,pady=5,width=50)
outpt_text.place(x=700,y=130)

language = list(LANGUAGES.values())
desti_lang = ttk.Combobox(root,values=language,width=22)
desti_lang.place(x=130,y=180)
desti_lang.set('choose language')

def Translate():
    translator = Translator()
    translate = translator.translate(text=inp_text.get(), dest=desti_lang.get())
    outpt_text.delete(1.0, END)
    outpt_text.insert(END,translate.text)

trans_btn = Button(root,text='Translate',font='Arial 12 bold',pady=5,command=Translate,bg='blue',activebackground='red')
trans_btn.place(x=445,y=180)

root.mainloop()