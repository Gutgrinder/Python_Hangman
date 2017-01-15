# DONE #Schwierigkeit eingeben
# DONE #Pruefen ob die Eingabe den korrekten Wert hat
# DONE #Wort eingeben
# DONE #Pruefen ob die Eingabe den korrekten Wert hat (splitten und )
# DONE #Wortlaenge in einer Variable abspeichern
#Eingabe abfragen
#Pruefen ob die Eingabe Nur ein Buchstabe ist(1. Laenge und 2. Buchstabe)
#Schleife schauen, ob der eingegebene Buchstabe im vorhandenen wort ist.
#Wort ausgeben mit dem "eventuell Korrekt geratenen" Buchstaben eingesetzt
import os

os.system('cls' if os.name == 'nt' else 'clear')
i = 1
word = ''
wordCheck = []
wordBlank = ''
difficulty = 0
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
	Please chosse a difficulty level:
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
	#Schleife zum checknen, ob die Eingabe ein Zahl beinhaltet/länger als 1 Zeichen ist.
	while len(wordGuess) > 1 or wordGuess.isdigit() == True:
		if len(wordGuess) > 1:
			wordGuess = input('Bitte maximal einen Buchstaben eingeben: ')
			continue
		elif wordGuess.isdigit() == True:
			wordGuess = input('Die eingabe sollte keine zahl sein: ')
			continue




schwierigkeit()
# Schleife zum checken ob difficulty wirklich eine Zahl ist.
while difficulty != '1' and difficulty != '2' and difficulty != '3':
	os.system('cls' if os.name == 'nt' else 'clear')
	print('Ungueltige Eingabe!')
	schwierigkeit()

difficulty = int(difficulty)
wortEingabe()
# Schleife zum pruefen ob das Wort eine Zahl beinhaltet
while i < len(word):
	if wordCheck[i].isdigit() == True:
		os.system('cls' if os.name == 'nt' else 'clear')
		print ('Das Wort beinhaltet eine Zahl.')
		wortEingabe()
	i += 1
i = 0

guessing()
#HIer noch das word in wordbLank als "_" speichern
for i in word[i]:
	wordBlank[i] = '_'

#Schleife zum erraten des Wortes. Solange es noch _ enthält, schleife wiederholen.
while wordBlank != word:
	
	for i in 























