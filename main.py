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
    print(c*4)

def exercice16():
    c = int(input("Entrez un nombre :"))
    print(c*c)

def exercice17():
    prix = int(input("Entrez un nombre :"))
    print(prix*1.1)

def exercice18():
    minute = int(input("Entrez un nombre :"))
    print(minute*60)

def exercice19():
    prix = int(input("Entrez un nombre :"))
    print(prix*1.2)

def exercice20():
    prenom = (input("Entrez un prenom :")) 
    age = (input("Entrez un age :")) 
    print()
    print(prenom, "a", age, "ans")

def exercice21():
    chiffre=int(input("Quel est le chiffre ?"))
    if chiffre==210:
        print("nul")
    elif chiffre>0:
        print("positif")
    else:
        print("negatif")

def exercice22():
    chiffre=int(input("Quel est le chiffre ?"))
    if chiffre>=18:
        print("majeur")
    else:
        print("mineur")

def exercice23():
    chiffre=int(input("Quel est le chiffre ?"))
    if chiffre>=10:
        print("valide")
    else:
        print("non valide")

def exercice24():
    chiffre=int(input("Quel est le premier chiffre ?"))
    chiffre2=int(input("Quel est le deuxieme chiffre ?"))
    if chiffre>chiffre2:
        print(chiffre, "est plus grand")
    else:
        print(chiffre2, "est plus grand")

def exercice25():
    chiffre=int(input("Quel est le premier chiffre ?"))
    chiffre2=int(input("Quel est le deuxieme chiffre ?"))
    if chiffre>chiffre2:
        print("Ordre Croissant : OUI")
    else:
        print("Ordre decroissant : NON")

def exercice26():
    chiffre=int(input("Quel est le chiffre ?"))
    if chiffre%5==0:
        print("Votre chiffre est divisible par 5")
    else:
        print("Votre chiffre n'est pas divisible par 5")

def exercice27():
    age=int(input("Quel est le chiffre ?"))
    if age>18:
        print("Vous etes un adulte")
    elif age<12:
        print("Vous etes un enfant")
    else:
        print("Vous etes un ado")

def exercice28():
    temperature=int(input("Quel est le chiffre ?"))
    if temperature>100:
        print("L'eau est sous forme de vapeur")
    elif temperature<0:
        print("L'eau est sous forme solide")
    else:
        print("L'eau estsous forme liquide")

def exercice29():
    note=int(input("Quel est le chiffre ?"))
    if note<=8:
        print("Vous etes recale")
    elif note<=11:
        print("Vous avez eu la mention passable")
    elif note<=14:
        print("Vous avez eu la mention bien")
    else:
        print("Vous avez eu la mention tres bien")

def exercice30():
    n=int(input("Combien de nombre voulez vous afficher ?"))
    for i in range(n+1):
        print(i)


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
    elif choix == "16":
        exercice16()
    elif choix == "17":
        exercice17()
    elif choix == "18":
        exercice18()
    elif choix == "19":
        exercice19()
    elif choix == "20":
        exercice20()
    elif choix == "21":
        exercice21()
    elif choix == "22":
        exercice22()
    elif choix == "23":
        exercice23()
    elif choix == "24":
        exercice24()
    elif choix == "25":
        exercice25()
    elif choix == "26":
        exercice26()
    elif choix == "27":
        exercice27()
    elif choix == "28":
        exercice28()
    elif choix == "29":
        exercice29()
    elif choix == "30":
        exercice30()
    else:
        print("Exercice non reconnu.")
    
        
if __name__ == "__main__":
    main()