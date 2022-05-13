import cesar_mejorado as cm
import enigma as en
import SEL as sl
from tkinter import *


def main():
    window = Tk()
    window.title("Cesar Mejorado")
    window.configure(bg="#F1EEE9")
    window.geometry("300x300")
    my_menu = Menu(window)

    def btn(window, texto, comando):
        return Button(window, text=texto, command=comando, bg="#EC994B", fg="black")
    def label(window,texto,estilo = ("Arial",12)):
        return Label(window, text=texto,bg="#F1EEE9",font=estilo,fg="black")

    option_menu = Menu(my_menu,background="#F1EEE9",foreground="black",tearoff=0)
    my_menu.add_cascade( label="Opciones", menu= option_menu)
    option_menu.add_command(label="Salir",command=window.quit)
    window.config(menu=my_menu)

    def cessar():
        window.destroy()
        cm.execute()
        main()

    def enig():
        window.destroy()
        en.execute()
        main()

    def sel():
        window.destroy()
        sl.execute()
        main()

    lbltitulo = label(window,"CriptoGebra",estilo=("Times",15))
    lbltitulo.pack()
    btncesar = btn(window,"Cesar (Mejorado)",lambda: cessar())
    btncesar.pack()
    btnenig = btn(window,"Enigma",lambda: enig())
    btnenig.pack()
    btnselr = btn(window,"Sistema de Ecuaciones Lineales",lambda: sel())
    btnselr.pack()

    window.mainloop()


if __name__ == '__main__':
    main()
