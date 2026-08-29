from tkinter import Tk, Frame, Button, Label
from random import choice

previous = 'cyan'

def kl(player, label):
    global previous
    while True:
        background = choice(['yellow', 'green', 'blue', 'red', 'cyan'])
        if previous != background:
            previous = background
            break
    machine = choice(['Heads', 'Tails'])
    label.config(text=f"{machine}, {'You won!' if player==machine else 'Sorry - you lost!'}",
                 bg=background)

def main():
    root = Tk()
    root.title('Heads or Tails')
    root.geometry('250x100')
    label = Label(root, text='', width=100)
    label.pack()
    frame = Frame(root).pack()
    Button(frame, text='Heads', command=lambda k='Heads': kl(k, label)).pack(side='left', padx=30)
    Button(frame, text='Tails', command=lambda k='Tails': kl(k, label)).pack(side='right', padx=30)    
    root.mainloop()

if __name__=='__main__':
    main()



    
