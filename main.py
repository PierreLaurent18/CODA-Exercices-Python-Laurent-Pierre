def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    nom = input("Votre prénom est ?")
    print ("Votre nom est",nom)

def exercice3():
    print("Salut\nc'est un\nretour a la ligne")

def exercice4():
    annee = int(input("Quelle est votre année de naissance ?"))
    
    print("Vous avez environ", 2025-annee)

def exercice5():
    a = int(input("Entrez un nombre :")) 
    b = int(input("Entrez un nombre :")) 
    print()
    print("Le résultat est :", a + b)

def exercice6():
    a = int(input("Entrez un nombre :")) 
    b = int(input("Entrez un nombre :")) 
    print()
    print("Le résultat est :", a - b)

def exercice7():
    a = int(input("Entrez un nombre :")) 
    b = int(input("Entrez un nombre :")) 
    print()
    print("Le résultat est :", a * b)




def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    elif choix == "4":
        exercice4()
    elif choix == "5":
        exercice5()
    elif choix == "6":
        exercice6()
    elif choix == "7":
        exercice7()
    else:
        print("Exercice non reconnu.")
    
        
if __name__ == "__main__":
    main()