from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def execute():
    window = Tk()
    window.title("Cifrado Enigma")
    window.geometry("300x200")
    window.configure(bg="#F1EEE9")
    my_menu = Menu(window)


    def entry(window,variable=StringVar()):
        return Entry(window, borderwidth=2, background="#73777B", textvariable=variable,fg="white",justify="center")
    def label(window, texto, estilo=("Calibri", 8)):
        return Label(window, text=texto, background="#F1EEE9", fg="black", font=estilo)
    def btn(window,texto,comando):
        return Button(window,text=texto,command=comando,bg="#EC994B",fg="black")
    def ver_mas():
        ver = Toplevel()
        ver.title("Ver Mas")
        ver.geometry("490x300")
        ver.configure(bg="#F1EEE9")
        ver_titulo = label(ver, "¿Qué es el cifrado Enigma?", estilo=("Times", 16))
        ver_titulo.pack()
        exp1 = label(ver, "Es un sencillo cifrado César utilizado para ocultar un texto sustituyendo\n"
                          " cada letra por la letra que está trece posiciones por delante en el alfabeto. \n"
                          "A se convierte en N, B se convierte en O y así hasta la M, que se convierte en Z. \n"
                          "Luego la secuencia se invierte",estilo=("Arial",10))
        exp1.pack()
        image = Image.open("Imagenes/enigma.png")
        resize_image = image.resize((200, 132))
        img = ImageTk.PhotoImage(resize_image)
        enig_img = Label(ver, image=img,bg="#F1EEE9")
        enig_img.image = img
        enig_img.pack()
    option_menu = Menu(my_menu,background="#F1EEE9",foreground="black",tearoff=0)
    my_menu.add_cascade( label="Opciones", menu= option_menu)
    option_menu.add_command(label="Ver Mas",command=ver_mas)
    option_menu.add_separator()
    option_menu.add_command(label="Salir",command=lambda: window.destroy())
    window.config(menu=my_menu)

    lbltitulo = label(window,"Codigo Enigma",estilo=("Times",20))
    lbltitulo.pack()
    lblpalabra = label(window,"Palabra")
    lblpalabra.pack()
    palabra = StringVar()
    txtpalabra = entry(window,variable=palabra)
    txtpalabra.pack()
    global code
    code = False
    def codificar(signo = ""):
        global code
        word = txtpalabra.get()
        continuer = True
        for i in word:
            if i.isalpha() or i.isspace():
                continue
            else:
                continuer =  False
                break
        if continuer:
            numero = "13"
            salto = int(signo+numero)
            new_word = ""
            for i in word:
                if i == " ":
                    new_word += " "
                elif i.isupper():
                    t = i.lower()
                    new_word += chr((((ord(t)+salto)-97)%26)+97).upper()
                else:
                    new_word += chr((((ord(i) + salto) - 97) % 26) + 97)
            if code==False:
                code = True
                btncodificar.configure(text="Decodificar")
            else:
                code = False
                btncodificar.configure(text="Codificar")
            palabra.set(new_word)
        else:
            messagebox.showwarning("Valor Erroneo","Ingresa solo valores alfabeticos y espacios")
    btncodificar = btn(window,"Codificar", lambda: codificar())
    btncodificar.pack(pady=30)
    window.mainloop()



if __name__ == '__main__':
    execute()
