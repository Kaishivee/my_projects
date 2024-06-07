import tkinter as tk
import random

window = tk.Tk()
window.config(bg='black')
window.title('Камень ножницы бумага')
window.geometry('600x400')
window.resizable(False, False)


def whyknb():
    knb = ['Камень', 'Ножницы', 'Бумага']
    value = random.choice(knb)
    opponent.configure(text=value)


opponent = tk.Label(window, text='', fg='white', bg='black', font=('Roman', 20))
opponent.place(x=210, y=110)

but_stone = tk.Button(window, text='Камень', fg='white', font=('Roman', 20), bg='#FF6103', command=whyknb)
but_stone.place(x=30, y=250)
but_scissors = tk.Button(window, text='Ножницы', fg='white', font=('Roman', 20), bg='#FF6103', command=whyknb)
but_scissors.place(x=210, y=250)
but_paper = tk.Button(window, text='Бумага', fg='white', font=('Roman', 20), bg='#FF6103', command=whyknb)
but_paper.place(x=430, y=250)

window.mainloop()