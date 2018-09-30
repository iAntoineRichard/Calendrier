from datetime import datetime

# Initialisation des variables :

result = input("Calcul du jour de la semaine gregorienne, veuillez utiliser la forme JJMMAAAA : ")

Date = datetime.strptime(result, '%d%m%Y')

Year = int(Date.strftime('%y'))

Day = int(Date.strftime('%d'))

Month = int(Date.strftime('%m'))

Bissex = False

# Question n°1 et n°2 :

iCal = (Year + (Year / 4))

# Question n°3 :

iCal += Day

# Question n°4 :

if 2 == Month:
    iCal += 3

elif Month == 3:
    iCal += 3

elif Month == 4:
    iCal += 6

elif Month == 5:
    iCal += 1

elif Month == 6:
    iCal += 4

elif Month == 7:
    iCal += 6

elif Month == 8:
    iCal += 2

elif Month == 9:
    iCal += 5

elif Month == 11:
    iCal += 3

elif Month == 12:
    iCal += 5

# Question n°5 :

annee = int(Date.strftime('%Y'))

if annee % 400 == 0:
    Bissex = True

elif annee % 100 == 0:
    Bissex = False

elif annee % 4 == 0:
    Bissex = True


if Bissex:
    if Month == 1 or Month == 2:
        iCal = iCal - 1

# Question n°6

siecle = annee - Year

if siecle == 1600:
    iCal += 6
elif siecle == 1700:
    iCal += 4
elif siecle == 1800:
    iCal += 2
elif siecle == 1900:
    iCal += 0
elif siecle == 2000:
    iCal += 6
elif siecle == 2100:
    iCal += 4

# Question n°7 :

iCal = iCal % 7

# Question n°8 et affichage du jour de la semaine'

ListeDesJours = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]

Resultat = len(ListeDesJours)

for i in range(len(ListeDesJours)):
    if i == int(iCal):
        print(ListeDesJours[i])

        break
