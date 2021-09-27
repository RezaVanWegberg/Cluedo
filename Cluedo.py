print("""-------------------------------------------------------------
|                       Solicitatie Cluedo                  |
-------------------------------------------------------------""")

naam = input("Hoe heet u? :")

Leeftijd = int(input("Hoe oud bent u? :"))# 2e opdracht
Geslacht = input("Bent u een man of een vrouw? M/V :")#1 Van de drie personage vragen
Ervaring = int(input("Heeft u al acteer ervaring? zo ja, hoeveel jaar dan? :")) #Verplicht voor aduitie
Spel = input("Heeft u ooit het spel gespeeld? J/N :") #a 2e opdracht
KleurHaar = input("Wat voor kleur haar heeft u? Antwoord in één volle kleur:")#1 van de drie personage vragen
Lengte = int(input("Hoe lang bent u in cm? :"))#1 van de drie personage vragen

if Ervaring > 3 and Leeftijd > 24 and Spel == "J": #Ik vindt dat dit meer dan 3 jaar moet zijn
    if Leeftijd >30 and Geslacht == ("M") and KleurHaar == "Grijs" or "Wit" and Lengte >= 180: #Kolonel van Geelen
        print("Je mag op auditie voor de rol van Kolonel van Geelen")
    elif Leeftijd >40 and Geslacht == ("V") and KleurHaar == "Grijs" or "Wit" and Lengte >120 <150: #Dominee groenewoud
        print("Je mag op auditie voor de rol van Dominee Groenewoud") 
    else:
        print("Je mag helaas niet op auditie")