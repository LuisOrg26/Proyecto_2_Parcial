import numpy as np
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# %%Formacion de la Interfaz
def execute():
    window = Tk()
    window.title("Sistemas de Ecuaciones Lineales")
    window.geometry("700x300")
    # %%Constantes
    def entry(window):
        variable = StringVar()
        return Entry(window, width=8, borderwidth=2, background="#73777B", textvariable=variable,fg="white",justify="center")

    def label(window, texto, estilo=("Calibri", 8)):
        return Label(window, text=texto, background="#F1EEE9", fg="black", font=estilo)

    def ver_mas():
        ver = Toplevel()
        ver.title("Ver Mas")
        ver.geometry("490x300")
        ver.configure(bg="#F1EEE9")
        ver_titulo = label(ver,"¿Qué es el Sistema de Ecuaciones Lineales?",estilo=("Times",16))
        ver_titulo.pack()
        exp1 = label(ver,"En matemáticas y álgebra lineal, un sistema de ecuaciones lineales,\n"
                         " también conocido como sistema lineal de ecuaciones o simplemente sistema \n"
                         "lineal, es un conjunto de ecuaciones lineales (es decir, un sistema de ecuaciones\n"
                         " en donde cada ecuación es de primer grado), definidas sobre un cuerpo o un anillo\n"
                         " conmutativo. Un ejemplo de sistema lineal de ecuaciones sería el siguiente:",estilo=("Arial",10))
        exp1.pack()
        image = Image.open("Imagenes/SEL.png")
        resize_image = image.resize((200, 132))
        img = ImageTk.PhotoImage(resize_image)
        sel_img = Label(ver, image=img,bg="#F1EEE9")
        sel_img.image = img
        sel_img.pack()

        ver.mainloop()
    my_menu = Menu(window)
    option_menu = Menu(my_menu, background="#F1EEE9", foreground="black", tearoff=0)
    my_menu.add_cascade(label="Opciones", menu=option_menu)
    option_menu.add_command(label="Ver Mas", command=ver_mas)
    option_menu.add_separator()
    option_menu.add_command(label="Salir", command=lambda: window.destroy())
    window.config(menu=my_menu)




    window.configure(background="#F1EEE9")
    x = 20
    y = 80
    z = 140
    r = 200
    rx = 280
    ry = 340
    rz = 400
    rr = 460
    lbl = 50
    txt = 70
    txt2 = 110
    xyy = 150
    btn = 180
    global multi
    multi = 0
    global numero
    numero = False

    # %% Widgets
    # lbltitulo = tk.Label(window,text="Ecuaciones Lineales",font=("Arial",20),background="black",fg="white")
    lbltitulo = label(window, "Ecuaciones Lineales", estilo=("Times", 20))
    lbltitulo.place(x=250, y=0)

    lblx = label(window, "X")
    lblx.place(x=x, y=lbl)
    txtx= entry(window)
    txt3x= entry(window)
    txt2x = entry(window)
    txtx.place(x=x, y=txt);
    txt3x.place(x=x, y=txt2);
    txt2x.place(x=x, y=txt2)

    lbly = label(window, "Y")
    lbly.place(x=y, y=lbl)
    txty= entry(window)
    txt3y= entry(window)
    txt2y = entry(window)
    txty.place(x=y, y=txt);
    txt3y.place(x=y, y=txt2);
    txt2y.place(x=y, y=txt2)

    lblz = label(window, "Z")
    lblz.place(x=z, y=lbl)
    txtz = entry(window)
    txtz.place(x=z, y=txt)
    txt3z = entry(window)
    txt3z.place(x=z, y=txt2)
    txt2z = entry(window)
    txt2z.place(x=z, y=txt2)

    lblresultado = label(window, "R")
    lblresultado.place(x=z, y=lbl)
    txtr = entry(window)
    txtr.place(x=z, y=txt)
    txt3r = entry(window)
    txt3r.place(x=z, y=txt2)
    txt2r = entry(window)
    txt2r.place(x=z, y=txt2)
    # %% Widgets Resultado

    lblrx1 = label(window, "", estilo=("Arial", 15))
    lblrx1.place(x=rx, y=txt)
    lblrx3 = label(window, "", estilo=("Arial", 15))
    lblrx3.place(x=rx, y=xyy)
    lblrx2 = label(window, "", estilo=("Arial", 15))
    lblrx2.place(x=rx, y=txt2)

    lblry1 = label(window, "", estilo=("Arial", 15))
    lblry1.place(x=ry, y=txt)
    lblry3 = label(window, "", estilo=("Arial", 15))
    lblry3.place(x=ry, y=xyy)
    lblry2 = label(window, "", estilo=("Arial", 15))
    lblry2.place(x=ry, y=txt2)

    lblrz1 = label(window, "", estilo=("Arial", 15))
    lblrz1.place(x=rz, y=txt)
    lblrz2 = label(window, "", estilo=("Arial", 15))
    lblrz2.place(x=rz, y=txt2)
    lblrz3 = label(window, "", estilo=("Arial", 15))
    lblrz3.place(x=rz, y=xyy)

    lblrr1 = label(window, "", estilo=("Arial", 15))
    lblrr1.place(x=rz, y=txt)
    lblrr3 = label(window, "", estilo=("Arial", 15))
    lblrz3.place(x=rz, y=xyy)
    lblrr2 = label(window, "", estilo=("Arial", 15))
    lblrr2.place(x=rz, y=txt2)


    # %%Funcion
    def TresD():
        lblresultado.place(x=r, y=lbl)
        txtr.place(x=r, y=txt)
        txt2r.place(x=r, y=txt2)
        txt3x.place(x=x, y=xyy)
        txt3y.place(x=y, y=xyy)
        txt3z.place(x=z, y=xyy)
        txt3r.place(x=r, y=xyy)

        lblrr1.place(x=rr, y=txt)
        lblrr2.place(x=rr, y=txt2)
        lblrr3.place(x=rr, y=xyy)
        global numero
        numero = True


    def DosD():
        lblresultado.place(x=z, y=lbl)
        txtr.place(x=z, y=txt)
        txt2r.place(x=z, y=txt2)
        txt3x.place(x=x, y=txt2)
        txt3y.place(x=y, y=txt2)
        txt3z.place(x=z, y=txt2)
        txt3r.place(x=z, y=txt2)

        lblrr1.place(x=rz, y=txt)
        lblrr2.place(x=rz, y=txt2)
        lblrr3.place(x=rz, y=xyy)
        global numero
        numero = False


    def calcular():
        global numero
        global multi
        if numero == True:
            try:
                x1 = float(txtx.get())
                x2 = float(txt2x.get())
                x3 = float(txt3x.get())
                y1 = float(txty.get())
                y2 = float(txt2y.get())
                y3 = float(txt3y.get())
                z1 = float(txtz.get())
                z2 = float(txt2z.get())
                z3 = float(txt3z.get())
                r1 = float(txtr.get())
                r2 = float(txt2r.get())
                r3 = float(txt3r.get())
            except(ValueError):
                messagebox.showwarning("Advertencia","Ha ingresado los datos de forma incorrecta, cambielos y vuelva a hacerlo")
                return

            a = np.array([[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]])
            b = np.array([r1, r2, r3])
            x = np.linalg.solve(a, b)

            lblrx1.configure(text=str(x1) + "x")
            lblrx2.configure(text=str(x2) + "x")
            lblrx3.configure(text=str(x3) + "x")
            lblry1.configure(text=str(y1) + "y")
            lblry2.configure(text=str(y2) + "y")
            lblry3.configure(text=str(y3) + "y")
            lblrz1.configure(text=str(z1) + "z")
            lblrz2.configure(text=str(z2) + "z")
            lblrz3.configure(text=str(z3) + "z")
            lblrr1.configure(text=" = " + str(r1))
            lblrr2.configure(text=" = " + str(r2))
            lblrr3.configure(text=" = " + str(r3))
            lblvalor = label(window, "x = " + str(round(x[0],2)) + " |  y = " + str(round(x[1],2)) + " |  z = " + str(round(x[2],2)), estilo=("Arial", 15))
            lblvalor.place(x=rx, y=btn + (30 * multi))


        elif numero == False:
            try:
                x1 = float(txtx.get())
                x2 = float(txt2x.get())
                y1 = float(txty.get())
                y2 = float(txt2y.get())
                r1 = float(txtr.get())
                r2 = float(txt2r.get())
            except(ValueError):
                messagebox.showwarning("Advertencia","Ha ingresado los datos de forma incorrecta, cambielos y vuelva a hacerlo")
                return

            a = np.array([[x1, y1], [x2, y2]])
            b = np.array([r1, r2])
            x = np.linalg.solve(a, b)

            lblrx1.configure(text=str(x1) + "x")
            lblrx2.configure(text=str(x2) + "x")
            lblry1.configure(text=str(y1) + "y")
            lblry2.configure(text=str(y2) + "y")
            lblrr1.configure(text=" = " + str(r1))
            lblrr2.configure(text=" = " + str(r2))
            lblvalor = label(window, "x = " + str(round(x[0],2)) + " |  y = " + str(round(x[1],2)), estilo=("Arial", 15))
            lblvalor.place(x=rx, y=btn + (30 * multi))
        multi += 1


    # %%Boton
    btn3d = Button(window, text="3D", command=TresD, background="#EC994B")
    btn3d.place(x=x, y=btn)
    btn2d = Button(window, text="2D", command=DosD, background="#EC994B")
    btn2d.place(x=y, y=btn)
    btncalcular = Button(window, text="Calcular", command=calcular, background="#EC994B")
    btncalcular.place(x=r, y=btn)
    window.mainloop()

if __name__ == '__main__':
    execute()
