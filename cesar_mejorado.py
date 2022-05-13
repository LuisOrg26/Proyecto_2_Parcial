from tkinter import*
import numpy as np

def execute():
    print(__name__)
    window = Tk()
    window.title("Cesar Mejorado")
    window.configure(bg="black")
    window.geometry("300x300")

    def label(window,texto,estilo = ("Arial",12)):
        return Label(window, text=texto,bg="black",font=estilo,fg="white")
    def entry(window,var):
        return Entry(window,bg="green",textvariable=var)
    def btn(window,texto,comando):
        return Button(window,text=texto,command=comando,bg="green",fg="white")

    palabra = StringVar()
    lbltitulo = label(window,"Cesar",("Arial",30)).pack()
    lblpalabra = label(window,"Palabra").pack()
    txtpalabra = entry(window,palabra).pack()
    lblcodigo = label(window,"Codigo").pack()
    txtcodigo = entry(window,StringVar()).pack()

    def cesar():
        word = palabra.get()
        salto = 3
        new_word = ""
        for i in word:
            if i.isupper() == True:
                new_word += chr((((ord(i.lower)+salto)-97)%26)+97).upper()
            else:
                new_word += chr((((ord(i) + salto) - 97) % 26) + 97)
        palabra.set(new_word)

    btncodificar = btn(window,"Codificar",cesar).pack(pady=10)
    btndecodificar = btn(window,"Decodificar",comando=cesar).pack()
    window.mainloop()




if __name__ == "__main__":
    execute()