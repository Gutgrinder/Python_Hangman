# DONE #Schwierigkeit eingeben
# DONE #Pruefen ob die Eingabe den korrekten Wert hat
# DONE #Wort eingeben
# DONE #Pruefen ob die Eingabe den korrekten Wert hat (splitten und )
# DONE #Wortlaenge in einer Variable abspeichern
# DONE #Eingabe abfragen
# DONE #Pruefen ob die Eingabe Nur ein Buchstabe ist(1. Laenge und 2. Buchstabe)
#Schleife schauen, ob der eingegebene Buchstabe im vorhandenen wort ist.
#Wort ausgeben mit dem "eventuell Korrekt geratenen" Buchstaben eingesetzt
import os

os.system('cls' if os.name == 'nt' else 'clear')
i = 1
word = ''
wordCheck = []
wordBlank = []
difficulty = 0
tries = 0
def wortEingabe():
	global i
	global word
	global wordCheck
	word = input("Bitte gib ein Wort ein, welches erraten werden soll: ")
	wordCheck = list(word)
	i = 0

def schwierigkeit():
	global difficulty
	print("""
	Please choose a difficulty level:
	1. Easy
	2. Medium
	3. Hard
	""")
	difficulty = input('Bitte waehle einen Schwierigkeitsgrad(1/2/3): ')

def guessing():
	global wordGuess
	global wordLength
	wordGuess = input("Bitte gib einen Buchstaben ein (a-z): ")
	wordLength = len(wordGuess)
	#Schleife zum checken, ob die Eingabe ein Zahl beinhaltet/länger als 1 Zeichen ist.
	while len(wordGuess) > 1 or wordGuess.isdigit() == True:
		if len(wordGuess) > 1:
			wordGuess = input('Bitte maximal einen Buchstaben eingeben: ')
			continue
		elif wordGuess.isdigit() == True:
			wordGuess = input('Die eingabe sollte keine zahl sein: ')
			continue
#
"""
Funktion die überprüft, ob der eingegebene Buchstabe im zu suchenden Wort zu finden ist.
def wordCheck():
	global splitWord
	global wordBlank
	global tries
	global wordGuess

	while i < len(splitWord)
		if splitWord[i] == wordGuess
			wordBlank[i] = wordGuess
		elif
			stuff
	
if Buchstabe in wort:
	geupdatetes wort zurückgeben
elif Buchstabe NICHT in wort:
	tires += 1

"""
schwierigkeit()
#Schleife zum checken ob difficulty wirklich eine Zahl ist.
while difficulty != '1' and difficulty != '2' and difficulty != '3':
	os.system('cls' if os.name == 'nt' else 'clear')
	print('Ungueltige Eingabe!')
	schwierigkeit()

if difficulty == '1':
	difficulty = 10
elif difficulty == '2':
	difficulty = 7
elif difficulty == '3':
	difficulty = 4

wortEingabe()
# Schleife zum pruefen ob das Wort eine Zahl beinhaltet
while i < len(word):
	if wordCheck[i].isdigit() == True:
		os.system('cls' if os.name == 'nt' else 'clear')
		print ('Das Wort beinhaltet eine Zahl.')
		wortEingabe()
	i += 1
i = 0

#Schleife um in der Variable "wordBlank" so viele "_" einzutragen, wie es Buchstaben in eingegebenen Wort gibt.
while i < len(word):
	wordBlank.append('_')
	i += 1

i = 0
splitWord = list(word)
joinWord = ''
wordBlank = joinWord.join(wordBlank)

#Hauptschleife
while wordBlank != word:
	os.system('cls' if os.name == 'nt' else 'clear')
	if tries = difficulty:
		print('Du hast zu viele Versuche benötigt')
		print('Game Over')
		input()
		break
	print('Es bleiben noch ', difficulty - tries, ' Fehlschlaege')
	guessing()
	wordBlank = list(wordBlank)
#	wordCheck()
	wordBlank = joinWord.join(wordBlank)
	print(word)
	print(wordBlank)


print('End of ULTRA HARDCORE Prog :D')
input()