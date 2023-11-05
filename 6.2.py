from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        m0 = float(m.get())
        h0 = float(h.get())
        I.set(round(float(m0) / float((h0/100)**2), 1))
        global T
        if  float(m0) / float((h0/100)**2) < 16: T.set('Выраженный дефицит массы тела')
        if 16 <= float(m0) / float((h0 / 100) ** 2) <= 18.5: T.set('Недостаточная (дефицит) масса тела')
        if 18.5 < float(m0) / float((h0 / 100) ** 2) < 25: T.set('Норма')
        if 25 <= float(m0) / float((h0 / 100) ** 2) < 30: T.set('Избыточная масса тела (предожирение)')
        if 30 <= float(m0) / float((h0 / 100) ** 2) < 35: T.set('Ожирение 1 степени')
        if 35 <= float(m0) / float((h0 / 100) ** 2) < 40: T.set('Ожирение 2 степени')
        if float(m0) / float((h0 / 100) ** 2) > 40: T.set('Ожирение 3 степени')

    except ValueError:
        pass

G = Tk()
G.title("ИМТ")

mainframe = ttk.Frame(G, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
G.columnconfigure(0, weight=1)
G.rowconfigure(0, weight=1)

m = StringVar()
M = ttk.Entry(mainframe, width=7, textvariable=m)
M.grid(column=2, row=1, sticky=(W, E))


h = StringVar()
H = ttk.Entry(mainframe, width=7, textvariable=h)
H.grid(column=2, row=2, sticky=(W, E))


I = StringVar()
ttk.Label(mainframe, textvariable=I).grid(column=2, row=4, sticky=(W, E))

T = StringVar()
ttk.Label(mainframe, textvariable=T).grid(column=2, row=5, sticky=(W, E))

ttk.Button(mainframe, text="Узнать ИМТ", command=calculate).grid(column=3, row=7, sticky=W)

ttk.Label(mainframe, text="Вес (в кг)").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Рост (в см)").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Ваш ИМТ:").grid(column=1, row=4, sticky=E)
ttk.Label(mainframe, text="кв.см/кг").grid(column=3, row=4, sticky=W)
ttk.Label(mainframe, text="Ваш вердикт:").grid(column=1, row=5, sticky=E)

for d in mainframe.winfo_children():
    d.grid_configure(padx=5, pady=5)

G.bind("<Return>", calculate)

G.mainloop()