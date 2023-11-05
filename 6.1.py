from tkinter import *

G = Tk()
G.geometry("500x250")
a = str()
b = str()
p = str()

def f(*args):
   Label(G, text=a).pack(pady = 4)

def f1(*args):
   global a, b, p
   a = a + '1'
   if p != str():
      if p == '+': a = str(float(b) + float(a))
      if p == '-': a = str(float(b) - float(a))
      if p == '*': a = str(float(b) * float(a))
      if p == '//': a = str(float(b) // float(a))
      if p == '%': a = str(float(b) * float(a) / 100)

def f2(*args):
   global a, b, p
   a = a + '2'
   if p != str():
      if p == '+': a = str(float(b) + float(a))
      if p == '-': a = str(float(b) - float(a))
      if p == '*': a = str(float(b) * float(a))
      if p == '//': a = str(float(b) // float(a))
      if p == '%': a = str(float(b) * float(a) / 100)

def f3(*args):
   global a, b, p
   a = a + '3'
   if p != str():
      if p == '+': a = str(float(b) + float(a))
      if p == '-': a = str(float(b) - float(a))
      if p == '*': a = str(float(b) * float(a))
      if p == '//': a = str(float(b) // float(a))
      if p == '%': a = str(float(b) * float(a) / 100)

def f4(*args):
   global a, b, p
   a = a + '4'
   if p != str():
      if p == '+': a = str(float(b) + float(a))
      if p == '-': a = str(float(b) - float(a))
      if p == '*': a = str(float(b) * float(a))
      if p == '//': a = str(float(b) // float(a))
      if p == '%': a = str(float(b) * float(a) / 100)

def f5(*args):
   global a, b, p
   a = a + '5'
   if p != str():
      if p == '+': a = str(float(b) + float(a))
      if p == '-': a = str(float(b) - float(a))
      if p == '*': a = str(float(b) * float(a))
      if p == '//': a = str(float(b) // float(a))
      if p == '%': a = str(float(b) * float(a) / 100)

def f6(*args):
   global a, b, p
   a = a + '6'
   if p != str():
      if p == '+': a = str(float(b) + float(a))
      if p == '-': a = str(float(b) - float(a))
      if p == '*': a = str(float(b) * float(a))
      if p == '//': a = str(float(b) // float(a))
      if p == '%': a = str(float(b) * float(a) / 100)

def f7(*args):
   global a, b, p
   a = a + '7'
   if p != str():
      if p == '+': a = str(float(b) + float(a))
      if p == '-': a = str(float(b) - float(a))
      if p == '*': a = str(float(b) * float(a))
      if p == '//': a = str(float(b) // float(a))
      if p == '%': a = str(float(b) * float(a) / 100)

def f8(*args):
   global a, b, p
   a = a + '8'
   if p != str():
      if p == '+': a = str(float(b) + float(a))
      if p == '-': a = str(float(b) - float(a))
      if p == '*': a = str(float(b) * float(a))
      if p == '//': a = str(float(b) // float(a))
      if p == '%': a = str(float(b) * float(a) / 100)

def f9(*args):
   global a, b, p
   a = a + '9'
   if p != str():
      if p == '+': a = str(float(b) + float(a))
      if p == '-': a = str(float(b) - float(a))
      if p == '*': a = str(float(b) * float(a))
      if p == '//': a = str(float(b) // float(a))
      if p == '%': a = str(float(b) * float(a) / 100)

def f0(*args):
   global a, b, p
   a = a + '0'
   if p != str():
      if p == '+': a = str(float(b) + float(a))
      if p == '-': a = str(float(b) - float(a))
      if p == '*': a = str(float(b) * float(a))
      if p == '//': a = str(float(b) // float(a))
      if p == '%': a = str(float(b) * float(a) / 100)

def summ(*args):
   global p, a, b
   p = '+'
   b = a
   a = str()

def diff(*args):
   global p, a, b
   p = '-'
   b = a
   a = str()

def mult(*args):
   global p, a, b
   p = '*'
   b = a
   a = str()

def div(*args):
   global p, a, b
   p = '//'
   b = a
   a = str()

def pers(*args):
   global p, a, b
   p = '%'
   b = a
   a = str()

G.bind('1', f1)
G.bind('2', f2)
G.bind('3', f3)
G.bind('4', f4)
G.bind('5', f5)
G.bind('6', f6)
G.bind('7', f7)
G.bind('8', f8)
G.bind('9', f9)
G.bind('0', f0)
G.bind('-', diff)
G.bind('*', mult)
G.bind('/', div)
G.bind('%', pers)
G.bind('+', summ)

X = Button(G, text="Калькулировать", command = f)
X.pack(ipadx=50)

G.title("Калькулятор (ввод с ENG-раскладки)")

G.mainloop()