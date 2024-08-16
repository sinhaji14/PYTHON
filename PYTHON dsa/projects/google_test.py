from tkinter import *
from tkinter import ttk  # ttk for combo boxes
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    trans = Translator()
    trans1 = trans.translate(text, src=src.lower(), dest=dest.lower())
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0, END)
    textget = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='blue')

lab_txt = Label(root, text="Translator", font=("Times New Roman", 40, "bold"))
lab_txt.place(x=100, y=40, height=50, width=300)

frame = Frame(root, bg='blue')
frame.pack(side=BOTTOM, fill=BOTH, expand=True)

lab_txt = Label(frame, text="Source Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="blue")
lab_txt.place(x=100, y=100, height=20, width=300)

Sor_txt = Text(frame, font=("Times New Roman", 20, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=130, height=150, width=480)

list_text = list(LANGUAGES.values())
comb_sor = ttk.Combobox(frame, values=list_text)
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set("english")

button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=170, y=300, height=40, width=150)

comb_dest = ttk.Combobox(frame, values=list_text)
comb_dest.place(x=340, y=300, height=40, width=150)
comb_dest.set("hindi")

lab_txt = Label(frame, text="Destination Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="blue")
lab_txt.place(x=100, y=360, height=20, width=300)

dest_txt = Text(frame, font=("Times New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

root.mainloop()
