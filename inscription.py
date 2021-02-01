from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror, showinfo
from listedesinscrits import listeInscrits


class User():
    def __init__(self,prenom,nom,photo):
        self.prenom = prenom
        self.nom = nom
        self.photo = photo
    def __eq__(self,other):
        return(self.prenom == other.prenom and self.nom == other.nom)

def parcourir():
    global imageName

    imn = askopenfilename( 
        initialdir="/", 
        title="selectionner une image",
        filetypes=[("image files","*.jpg"),("image files","*.png")]
        # filetypes= [("jpeg files","*.jpg"),("png files","*.png")]

    )
    if imn:
        imageName=imn
    if imageName:
        texte= imageName.split("/")
        photoEntry.configure(text=".../"+texte[-1])

def appartient(liste,val):
    for i in range(len(liste)):
        if liste[i].__eq__(val):
            return 1
    return 0

def valider():
    global listeUser,imageName
    photo = imageName

    print(prenomEntry.get())
    print(nomEntry.get())
    print(photo)

    if prenomEntry.get() and nomEntry.get() and photo:
        pn = User(prenomEntry.get(),nomEntry.get(),photo)
        if appartient(listeUser, pn):
            showerror(title="Formulaire invalide",message="cet utilisateur existe déjà !")
        else:
            listeUser.append(pn)
            showinfo(title="validation réussie", message="{} a bien été ajouté".format(prenomEntry.get()))
    else:
        showerror(title="validation echec", message="tous les champs doivent être remplis")

def reinitialiser():
    global imageName
    prenomEntry.delete(0,END) 
    nomEntry.delete(0,END) 
    imageName=''
    photoEntry.configure(text="aucune image selectionnée")

imageName, listeUser= '',[]


window = Tk()
window.geometry("315x320")
window.title("page d'inscription")

contenu = Canvas(window,bg="#51728f")

fontLabel = 'arial 13 bold'
fontEntry = 'arial 11 bold'

prenom = Label(contenu, text="votre prénom: ", font= fontLabel, fg="#e5eaec",bg="#51728f")
nom = Label(contenu, text="votre nom: ", font= fontLabel, fg="#e5eaec",bg="#51728f")
photo = Label(contenu, text="votre photo: ", font= fontLabel, fg="#e5eaec",bg="#51728f")
validation = Label(contenu, text="Entrez vos informations ici ", font= fontLabel, fg="#e5eaec",bg="#51728f")

prenomEntry = Entry(contenu, font=fontEntry)
nomEntry = Entry(contenu, font=fontEntry)
photoEntry = Label(contenu,text="aucune image selectionnée", font='arial 8 bold', fg="#51728f",bg="#e5eaec")
buttonParcourir = Button(contenu,text="Parcourir", command=parcourir, fg="#51728f",bg="#e5eaec")

validation.grid(row=0,column=0, columnspan=2,pady=5)
prenom.grid(row=1, column=0, sticky=E,padx=5, pady=5)
nom.grid(row=2, column=0, sticky=E,padx=5, pady=5)
photo.grid(row=3, column=0, sticky=E,padx=5, pady=5)

prenomEntry.grid(row=1,column=1, padx=5, pady=5)
nomEntry.grid(row=2,column=1, padx=5, pady=5)
photoEntry.grid(row=3,column=1, padx=5, pady=5,sticky=W)
buttonParcourir.grid(row=3,column=1, padx=5, pady=5,sticky=E)

b1 = Button(window,text="Valider", command=valider,width=10, fg="#51728f",bg="#e5eaec")
b2 = Button(window,text="Réinitialiser", command=reinitialiser,width=10, fg="#51728f",bg="#e5eaec")
b3 = Button(window,text="Voir la liste", command=lambda: listeInscrits(window,listeUser),width=10, fg="#51728f",bg="#e5eaec")

b1.grid(row=4,column=0, pady=5)
b2.grid(row=5,column=0, pady=5)
b3.grid(row=6,column=0, pady=5)

contenu.grid(row=0,column=0, padx=5, pady=5)

window.mainloop()