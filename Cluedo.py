print("""-------------------------------------------------------------
|                       Solicitatie Cluedo                  |
-------------------------------------------------------------""")

naam = input("Hoe heet u? :")

Leeftijd = int(input("Hoe oud bent u? :"))# 2e opdracht
Geslacht = input("Bent u een man of een vrouw? M/V :")#1 Van de drie personage vragen
if Geslacht == "M":
    Snor = input("Heeft u een snor? J/N :")
Ervaring = int(input("Heeft u al acteer ervaring? zo ja, hoeveel jaar dan? :")) #Verplicht voor aduitie
Spel = input("Heeft u ooit het spel gespeeld? J/N :") #a 2e opdracht
KleurHaar = input("Wat voor kleur haar heeft u? Antwoord in één volle kleur :")#1 van de drie personage vragen
if KleurHaar == "Bruin":
    Krullen = input("Heeft u krullen? J/N:")
Lengte = int(input("Hoe lang bent u in cm? :"))#1 van de drie personage vragen
Huidskleur = input("Wat voor huidskleur heeft u? :")#1 van de drie personage vragen


if Ervaring > (3) and Spel == "J": #Ik vindt dat dit meer dan 3 jaar moet zijn
    if Leeftijd >= (30) and Geslacht == ("M") and KleurHaar == "Grijs" and Lengte >= (180): #Kolonel van Geelen
        print("Je mag op auditie voor de rol van Kolonel van Geelen")
    elif Leeftijd >= (40) and Geslacht == ("V") and KleurHaar == "Wit" and  Lengte <= (150): #Mevrouw de wit
        print("Je mag op auditie voor de rol van Mevrouw de Wit") 
    elif Leeftijd >=(20) and Geslacht == ("V") and KleurHaar == "Blond" and Huidskleur == "Wit": #Mevrouw Blaauw van Draet
        print("Je mag op auditie voor de rol van Mevrouw Blaauw van Draet")
    elif Leeftijd >=(38) and Snor == ("J") and Lengte > (160): #Prof Pimpel
        print("Je mag op auditie voor de rol van Professor Pimpel")
    elif Leeftijd >(20) and Geslacht == ("V") and Krullen == "J": #Rosa Roodhart
        print("Je mag op auditie voor de rol van Rosa Roodhart")
    elif Leeftijd >=(40) and Geslacht == ("M") and Ervaring >=(10): #Dominee Groenewoud
        print("Je mag op auditie voor de rol van Dominee Groenewoud")
    else:
        print("Je mag helaas niet op auditie")
else:
    print("Je mag helaas niet op auditie")