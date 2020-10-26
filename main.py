

répertoire={

}
a = False


def create_contact(name, nbPhone, fav2):

    contact1={
        "name": name,
        "nbPhone": nbPhone,
        "fav": fav2,
    }
    return contact1

def add_contact(contact1):
    name = contact1["name"]
    répertoire[ name ] = contact1
    return répertoire
boucle1 = False

def get_names(répertoire):
    for i in répertoire:
        print(i)


while True :
    a = False
    boucle1 = False
    print("Bienvenue dans le menu principal de ton répertoire \n Tu as le chois entre deux options \n liste des contacts \n créer un contact")
    chois = input("tape 1 pour liste des contacts et 2 pour créer un contact")
    if chois == "1" :
        get_names(répertoire)


    if chois == "2" :

        #ajout contact
        while not a:
            while not boucle1:
                    nbphone1 = input("écrit le numéro de téléphone?")
                    if nbphone1.isdigit():
                        boucle1 = True
                        name1 = input("écrit le nom?")

                    fav1 = input("Veux-tu le mettre en favory ? OUI ou NON ?")
                    if fav1 == "OUI":
                        fav2 = True
                    else:
                        fav2 = False

            c = create_contact(nbphone1 , name1 , fav1 )
            add = input("Veux-tu le rajouter au contact? OUI ou NON ?")
            if add == "OUI":
                add_contact(c)
                a = True
            else:
                print("Tu peux créer un nouveaux contact: ")

