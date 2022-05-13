from tkinter import*
import numpy as np

def execute():
    print(__name__)
    window = Tk()
    window.title("Cesar Mejorado")
    window.configure(bg="black")
    window.geometry("300x300")
    my_menu = Menu(window)

    def ver_mas():
        pass
    option_menu = Menu(my_menu,background="black",foreground="white",tearoff=0)
    my_menu.add_cascade( label="Opciones", menu= option_menu)
    option_menu.add_command(label="Ver Mas",command=ver_mas)
    option_menu.add_separator()
    option_menu.add_command(label="Salir",command=window.quit)
    window.config(menu=my_menu)

    def label(window,texto,estilo = ("Arial",12)):
        return Label(window, text=texto,bg="black",font=estilo,fg="white")
    def entry(window,var,status="normal"):
        return Entry(window,bg="green",textvariable=var,state=status)
    def btn(window,texto,comando):
        return Button(window,text=texto,command=comando,bg="green",fg="white")

    palabra = StringVar()
    code = StringVar()
    lbltitulo = label(window,"Cesar",("Arial",30)).pack()
    lblpalabra = label(window,"Palabra").pack()
    txtpalabra = entry(window,palabra)
    txtpalabra.pack()
    lblcodigo = label(window,"Codigo").pack()
    txtcodigo = entry(window,code)
    txtcodigo.pack()
    txtcodigo.configure(state="disable")

    def cesar(signo="",numero=None):
        word = palabra.get()
        if numero == "":
            numero = "3"
        salto = int(signo+numero)
        new_word = ""
        for i in word:
            if i.isupper() == True:
                new_word += chr((((ord(i.lower)+salto)-97)%26)+97).upper()
            else:
                new_word += chr((((ord(i) + salto) - 97) % 26) + 97)
        palabra.set(new_word)
    def cesar_normal():
        txtcodigo.configure(state="disable")
    def cesar_mejorado():
        txtcodigo.configure(state="normal")

    btncodificar = btn(window,"Codificar",lambda:cesar(numero=code.get())).pack(pady=10)
    btndecodificar = btn(window,"Decodificar",lambda: cesar(signo="-",numero=code.get())).pack()
    btncesar_normal = btn(window,"Cesar",cesar_normal).pack(anchor="s",side="left")
    btncesar_mejorado = btn(window,"Cesar Mejorado",cesar_mejorado).pack(anchor="s",side="right")
    window.mainloop()




if __name__ == "__main__":
    execute()