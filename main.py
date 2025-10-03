import random
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

def exercice31():
    n=int(input("Combien de nombre voulez vous afficher ?"))
    for i in range(0,n+1):
        print(n-i)

def exercice32():
    r=0
    n=int(input("Combien de nombre voulez vous afficher ?"))
    for i in range(0,n+1):
        r+=i
    print(r)

def exercice33():
    n=int(input("quel est votre nombre ?"))
    for i in range(1,11):
        print(n,"x",i,"=",i*n)

def exercice34():
    n=int(input("quel est votre nombre ?"))
    for i in range(1,n+1):
        if i%2==0:
            print(i)

def exercice35():
    n=int(input("quel est votre nombre ?"))
    for i in range(0,n+1):
        if i*i<20:
            print(i*i)

def exercice36():
    i="bonjour"
    for i in range(3):
        print("bonjour")

def exercice37():
    print("  X  \n XXX \nXXXXX")

def exercice38():
    signe = (input("Entrez un signe :"))
    if signe == "+":
        exercice5()
    elif signe == "-":
        exercice6()
    elif signe == "*":
        exercice7()
    else:
        exercice8()

def exercice39():
    secret=random.randint(1,10)
    guess=input("pair ou impair :")
    if secret%2==0:
        print("GG BG")
    else:
        print("perdu sale bot")

def exercice40():
    mdp=input("quel est votre mot de passe ?")
    if len(mdp) < 6:
        print("Trop court")
    else:
        print("Valide")

def exercice41():
    a=int(input("quel est le premier nombre ?"))
    b=int(input("quel est le deuxieme nombre ?"))
    c=int(input("quel est le troisieme nombre ?"))
    d=int(input("quel est le quatrieme nombre ?"))
    e=int(input("quel est le cinquieme nombre ?"))
    print((a+b+c+d+e)/5)

def exercice42():
    a=int(input("quel est le premier nombre ?"))
    b=int(input("quel est le deuxieme nombre ?"))
    c=int(input("quel est le troisieme nombre ?"))
    d=int(input("quel est le quatrieme nombre ?"))
    e=int(input("quel est le cinquieme nombre ?"))
    print(max(a,b,c,d,e))   
    print(min(a,b,c,d,e))

def exercice43():
    phrase=input("Entrez une phrase :")
    compteur=0
    for lettre in phrase:
        if lettre in "aeiouyAEIOUY":
            compteur+=1
    print("Il y a",compteur,"voyelles dans cette phrase")

def exercice44():
    mot=input("Entrez un mot :")
    print(mot[::-1])   

def exercice45():
    liste=[1,2,3,4,5]
    print(sum(liste))

def exercice46():
    liste=[1,2,3,4,5]
    n=int(input("Quel nombre voulez vous chercher ?"))
    if n in liste:
        print("Le nombre est dans la liste")
    else:
        print("Le nombre n'est pas dans la liste")

def exercice47():
    liste=[1,2,3,4,5,1,2,1,1]
    n=int(input("Quel nombre voulez vous compter ?"))
    compteur=0
    for i in liste:
        if i==n:
            compteur+=1
    print("Le nombre",n,"apparaît",compteur,"fois dans la liste")

def exercice48():
    n=int(input("Entrez un nombre :"))
    diviseurs=[]
    for i in range(1,n+1):
        if n%i==0:
            diviseurs.append(i)
    print("Les diviseurs de",n,"sont :",diviseurs)

def exercice49():
    n=int(input("Entrez un nombre :"))
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print(n,"n'est pas un nombre premier")
                break
        else:
            print(n,"est un nombre premier")
    else:
        print(n,"n'est pas un nombre premier")

def exercice50():
    n=int(input("Entrez un nombre :"))
    a,b=0,1
    while a<=n:
        print(a,end=" ")
        a,b=b,a+b
    print()

def exercice51():
    lp = [1]
    n = int(input("jusqu'à n = "))
    for j in range(n):
        nl = lp + [1]
        for i in range(len(lp) - 1):
            nl[i + 1] = lp[i] + lp[i + 1]
        lp = nl
    print(nl)

def main():
    while True:
        print("\n=== Menu des exercices ===")
        print("q - Quitter")
    
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
        elif choix == "31":
            exercice31()
        elif choix == "32":
            exercice32()
        elif choix == "33":
            exercice33()
        elif choix == "34":
            exercice34()
        elif choix == "35":
            exercice35()
        elif choix == "36":
            exercice36()
        elif choix == "37":
            exercice37()
        elif choix == "38":
            exercice38()
        elif choix == "39":
            exercice39()
        elif choix == "40":
            exercice40()
        elif choix == "41":
            exercice41()
        elif choix == "42":
            exercice42()
        elif choix == "43":
            exercice43()
        elif choix == "44":
            exercice44()
        elif choix == "45":
            exercice45()
        elif choix == "46":
            exercice46()
        elif choix == "47":
            exercice47()
        elif choix == "48":
            exercice48()
        elif choix == "49":
            exercice49()
        elif choix == "50":
            exercice50()
        elif choix == "51":
            exercice51()


        elif choix == "q":
            print("Au revoir 👋")
            break
        else:
            print("⚠️ Choix non reconnu. Essayez encore.")

        # Pause entre deux exécutions pour laisser le temps de lire
        input("\nAppuyez sur Entrée pour revenir au menu...")
    
        
if __name__ == "__main__":
    main()