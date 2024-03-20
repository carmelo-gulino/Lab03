import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!
    try:
        if int(txtIn) == 1:
            sc.aggiungiLingua("italian", './resources/Italian.txt')
            print("Inserisci la tua frase in Italiano\n")
            txtIn = input()
            sc.handleSentence(txtIn,"italian")

        elif int(txtIn) == 2:
            sc.aggiungiLingua("english", './resources/English.txt')
            print("Inserisci la tua frase in Inglese\n")
            txtIn = input()
            sc.handleSentence(txtIn,"english")

        elif int(txtIn) == 3:
            sc.aggiungiLingua("spanish", './resources/Spanish.txt')
            print("Inserisci la tua frase in Spagnolo\n")
            txtIn = input()
            sc.handleSentence(txtIn,"spanish")

        elif int(txtIn) == 4:
            break

    except ValueError:
        print("Inserisci un numero da 1 a 4")

"Il dinosaruo in pigiama decise di andare a fare la spesa, dimenticandosi però che non avva porsolio ne pantaloni, suscituando sguardi perpxpelsi tra i passanti"