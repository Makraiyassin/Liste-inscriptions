from tkinter import *
from PIL import Image,ImageTk



def listeInscrits(fenetre,liste):
    new_window = Toplevel(fenetre)
    new_window.geometry("350x400+350+150")
    new_window.title("liste des inscrits")

    liste_canvas= Canvas(new_window, bg="#337ec0")
    fontLabel = "arial 11 bold"

    resultat = Label(liste_canvas, text="liste des gens inscrits",font = fontLabel,fg="white",bg="#337ec0",)
    prenom = Label(liste_canvas, text="prenom", font= fontLabel, fg="white",bg="#337ec0", width="15")
    nom = Label(liste_canvas, text="nom", font= fontLabel, fg="white",bg="#337ec0", width="6")
    photo = Label(liste_canvas, text="photo", font= fontLabel, fg="white",bg="#337ec0", width="12")
    status = Label(liste_canvas, text="aucun inscrit pour le moment", font= "arial 9 bold", fg="white",bg="#337ec0")

    liste_canvas.grid(row=0,column=0)
    resultat.grid(row=0,column=0,columnspan=3,pady=2)
    photo.grid(row=1,column=0,padx=5,pady=5)
    prenom.grid(row=1,column=1,padx=5,pady=5)
    nom.grid(row=1,column=2,padx=5,pady=5)
    status.grid(row=2,column=0,columnspan=3,pady=2)

    if liste:
        r=2
        for p in liste:
            photo_label= Label(liste_canvas, height=50)
            img = Image.open(p.photo)
            img = img.resize((80,80), Image.ANTIALIAS)
            photo_label.img = ImageTk.PhotoImage(img)
            photo_label.configure(image=photo_label.img)

            firstname = Label(liste_canvas, text=p.prenom, font= fontLabel, fg="white",bg="#337ec0")
            lastname = Label(liste_canvas, text=p.nom, font= fontLabel, fg="white",bg="#337ec0")

            photo_label.grid(row=r,column=0, pady =2)
            firstname.grid(row=r,column=1)
            lastname.grid(row=r,column=2)
            
            liste_canvas.create_line(9,58,355,58,width=1,fill="white")

            r+=1

            status.configure(text="{} inscrits pour le moment".format(len(liste)))
            status.grid(row=r,column=0,columnspan=3, pady=2)
    new_window.mainloop()
