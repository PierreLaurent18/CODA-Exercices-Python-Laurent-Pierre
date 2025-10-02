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

def exercice8():
    a = float(input("Entrez un nombre :")) 
    b = float(input("Entrez un nombre :")) 
    print()
    print("Le résultat est :", a / b)

def exercice9():
    a = int(input("Entrez un nombre :")) 
    print("Le résultat est :", a**2)

def exercice10():
    a = int(input("Entrez un nombre :")) 
    print("Le résultat est :", a*2)

def exercice11():
    a = float(input("Entrez un nombre :")) 
    print("Le résultat est :", a/2)

def exercice12():
    for i in range(5):
        print("Bonjour !")

def exercice13():
    for i in range(1,6):
        print(i)

def exercice14():
    for i in range(1,6):
        print("2x",i,"=",2*i)

def exercice15():
    c = int(input("Entrez un nombre :"))
    print(c*c)




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
    elif choix == "8":
        exercice8()
    elif choix == "9":
        exercice9()
    elif choix == "10":
        exercice10()
    elif choix == "11":
        exercice11()
    elif choix == "12":
        exercice12()
    elif choix == "13":
        exercice13()
    elif choix == "14":
        exercice14()
    elif choix == "15":
        exercice15()
    else:
        print("Exercice non reconnu.")
    
        
if __name__ == "__main__":
    main()