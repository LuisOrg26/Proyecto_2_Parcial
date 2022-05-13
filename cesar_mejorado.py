from tkinter import*
import numpy as np
from PIL import Image, ImageTk

def execute():
    print(__name__)
    window = Tk()
    window.title("Cesar Mejorado")
    window.configure(bg="#F1EEE9")
    window.geometry("300x300")
    my_menu = Menu(window)

    def label(window,texto,estilo = ("Arial",12)):
        return Label(window, text=texto,bg="#F1EEE9",font=estilo,fg="black")
    def entry(window,var,status="normal"):
        return Entry(window,bg="#73777B",textvariable=var,state=status,fg="white")
    def btn(window,texto,comando):
        return Button(window,text=texto,command=comando,bg="#EC994B",fg="black")

    def ver_mas():
        ver = Toplevel()
        ver.title("Ver Mas")
        ver.geometry("450x300")
        ver.configure(bg="#F1EEE9")
        ver_titulo = label(ver,"¿Qué es el cifrado Cesar?",estilo=("Times",20))
        ver_titulo.pack()
        exp1 = label(ver,"El cifrado Cesar es uno de los más simples y conocidas\n"
                         "se basa en el cifrado monoalfabético y se considera\n"
                         " un método débil de criptografía, ya que es fácil\n"
                         " decodificar el mensaje debido a sus técnicas de\n"
                         " seguridad mínimas.")
        exp1.pack()
        image = Image.open("Imagenes/cesar.png")
        resize_image = image.resize((200, 132))
        img = ImageTk.PhotoImage(resize_image)
        cesar_img = Label(ver,image=img,bg="#F1EEE9")
        cesar_img.image = img
        cesar_img.pack()

        ver.mainloop()

    option_menu = Menu(my_menu,background="#F1EEE9",foreground="black",tearoff=0)
    my_menu.add_cascade( label="Opciones", menu= option_menu)
    option_menu.add_command(label="Ver Mas",command=ver_mas)
    option_menu.add_separator()
    option_menu.add_command(label="Salir",command=lambda: window.destroy())
    window.config(menu=my_menu)



    palabra = StringVar()
    code = StringVar()
    lbltitulo = label(window,"Cesar Mejorado",("Arial",30)).pack()
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
            if i == " ":
                new_word += " "
            elif i.isupper() == True:
                t = i.lower()
                new_word += chr((((ord(t)+salto)-97)%26)+97).upper()
            else:
                new_word += chr((((ord(i) + salto) - 97) % 26) + 97)
        palabra.set(new_word)
    def cesar_normal():
        txtcodigo.delete(0,END)
        txtcodigo.configure(state="disable")
    def cesar_mejorado():
        txtcodigo.configure(state="normal")

    btncodificar = btn(window,"Codificar",lambda:cesar(numero=code.get())).pack(pady=10)
    btndecodificar = btn(window,"Decodificar",lambda: cesar(signo="-",numero=code.get())).pack()
    btncesar_normal = btn(window,"Cesar",cesar_normal).pack(anchor="s",side="left")
    btncesar_mejorado = btn(window,"Cesar Mejorado",cesar_mejorado).pack(anchor="s",side="right")
    window.mainloop()

#Hola
if __name__ == "__main__":
    execute()