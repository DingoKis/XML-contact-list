import webbrowser
import xml.etree.ElementTree as ET
import os.path

print("\nGestore file XML (software versione 1.1)"
      "\nPiattaforma software di testing: Windows 10 Pro 64bit"
      "\nPiattaforma hardware di testing: AMD Ryzen 2600X"
      "\nSviluppato da DingoKis con Python 3.8")

run = True

while run:
    scelta = input("\nScrivere 1 se si vuole verificare l'esistenza della rubrica"
                   "\nScrivere 2 se si vuole visualizzare tutto il contenuto della rubrica"
                   "\nScrivere 3 se si vuole ricercare un nome nella rubrica"
                   "\nScrivere 4 se si vuole creare una rubrica vuota"
                   "\nScrivere 5 se si vuole aggiungere nuovi elementi alla rubrica"
                   "\nScrivere 6 se si vuole modificare un campo esistente nella rubrica"
                   "\nScrivere 7 se si vuole eliminare un campo nella rubrica"
                   "\nScrivere 8 se si vuole consultare il manuale di documentazione"
                   "\nScrivere 9 se si vuole aprire o aggiornare il file xml "
                   "\nPremere invio se si vuole uscire"
                   "\nScelta: ")

    if scelta == '1':
        if os.path.exists('./rubrica.xml'):
            print('\nLa rubrica esiste')
        else:
            print('\nLa rubrica non esiste')

    elif scelta == '2':
        if os.path.exists('./rubrica.xml'):
            print("\nLa stampa di tutta la rubrica:")
            tree = ET.parse('rubrica.xml')
            root = tree.getroot()
            for child in root:
                print("\n"+ child.tag, child.attrib)
                for child in child:
                    print(child.tag, child.text)

        else:
            print('\nNon esiste la rubrica')

    elif scelta == '3':
        if os.path.exists('./rubrica.xml'):
            missing = True
            tree = ET.parse('rubrica.xml')
            root = tree.getroot()
            ricerca = input('\nInserisci il nome\cognome da cercare: ')
            print()
            for contatto in root.iter('contatto'):
                nome = contatto.find('nome').text
                cognome = contatto.find('cognome').text
                if nome.lower() == ricerca.lower():
                    print('Nome presente nel contatto ' + str(contatto.attrib))
                    missing = False
                if cognome.lower() == ricerca.lower():
                    print('Cognome presente nel contatto ' + str(contatto.attrib))
                    missing = False
            if missing:
                print("Non ci sono nomi corrispondenti!")

        else:
            print('\nNon esiste la rubrica')

    elif scelta == '6':
        if os.path.exists('./rubrica.xml'):
            tree = ET.parse('rubrica.xml')
            root = tree.getroot()
            ricerca = input("\nScrivere 1 se si vuole modificare il nome"
                            "\nScrivere 2 se si vuole modificare il cognome"
                            "\nScrivere 3 se si vuole modificare il numero"
                            "\nScrivere 4 se si vuole modificare l'email"
                            "\nPremere invio se non si vuole modificare nulla"
                            "\nScelta: ")

            if ricerca == '1':
                ricerca = input("\nInserisci ID del contatto nel quale modificare il nome: ")
                for contatto in root.iter('contatto'):
                    id = contatto.attrib
                    if str(id) == str("{'id': '" + ricerca + "'}"):
                        print("Nome attuale: " + str(contatto.find('nome').text))
                        nuovoNome = input('Inserisci il nuovo nome: ')
                        contatto.find('nome').text = str(nuovoNome)
                        tree.write("rubrica.xml")
                        print("Nome aggiornato!")

            elif ricerca == '2':
                ricerca = input("\nInserisci ID del contatto nel quale modificare il cognome: ")
                for contatto in root.iter('contatto'):
                    id = contatto.attrib
                    if str(id) == str("{'id': '" + ricerca + "'}"):
                        print("Cognome attuale: " + str(contatto.find('cognome').text))
                        nuovoCognome = input('Inserisci il nuovo cognome: ')
                        contatto.find('cognome').text = str(nuovoCognome)
                        tree.write("rubrica.xml")
                        print("Cognome aggiornato!")

            elif ricerca == '3':
                ricerca = input("\nInserisci ID del contatto nel quale modificare il numero: ")
                for contatto in root.iter('contatto'):
                    id = contatto.attrib
                    if str(id) == str("{'id': '" + ricerca + "'}"):
                        print("Numero attuale: " + str(contatto.find('numero').text))
                        nuovoNumero = input('Inserisci il nuovo numero: ')
                        contatto.find('numero').text = str(nuovoNumero)
                        tree.write("rubrica.xml")
                        print("Numero aggiornato!")

            elif ricerca == '4':
                ricerca = input("\nInserisci ID del contatto nel quale modificare l'email: ")
                for contatto in root.iter('contatto'):
                    id = contatto.attrib
                    if str(id) == str("{'id': '" + ricerca + "'}"):
                        print("E-mail attuale: "+str(contatto.find('email').text))
                        nuovaMail = input('Inserisci la nuova e-mail: ')
                        contatto.find('email').text = str(nuovaMail)
                        tree.write("rubrica.xml")
                        print("E-mail aggiornata!")

            else:
                print("\nVa bene!")

        else:
            print('\nNon esiste la rubrica')

    elif scelta == '5':
        if os.path.exists('./rubrica.xml'):
            tree = ET.parse('rubrica.xml')
            root = tree.getroot()

            i = input('\nInserisci id: ')

            doc = ET.SubElement(root, "contatto")
            doc.attrib['id'] = str(i)

            nome = input('Inserisci nome: ')
            cognome = input('Inserisci cognome: ')
            numero = input('Inserisci numero di telefono: ')
            email = input('Inserisci indirizzo e-mail: ')

            ET.SubElement(doc, "nome").text = nome
            ET.SubElement(doc, "cognome").text = cognome
            ET.SubElement(doc, "numero").text = numero
            ET.SubElement(doc, "email").text = email

            tree.write("rubrica.xml")

        else:
            print('\nNon esiste la rubrica')

    elif scelta == '4':
        root = ET.Element('rubrica')
        tree = ET.ElementTree(root)
        tree.write("rubrica.xml", encoding="utf-8", xml_declaration=True)
        print("\nRubrica vuota creata!")

    elif scelta == '7':
        if os.path.exists('./rubrica.xml'):
            tree = ET.parse('rubrica.xml')
            root = tree.getroot()

            ricerca = input("\nInserisci ID del contatto da eliminare: ")
            for contatto in root.findall('contatto'):
                id = contatto.attrib
                if str(id) == str("{'id': '" + ricerca + "'}"):
                    root.remove(contatto)
                    tree.write('rubrica.xml')
                    print("Contatto eliminato!")
        else:
            print('\nNon esiste la rubrica')

    elif scelta == '8':
        webbrowser.open("shorturl.at/hACLN")

    elif scelta == '9':
        if os.path.exists('./rubrica.xml'):
            webbrowser.open("rubrica.xml")
        else:
            print('\nLa rubrica non esiste')

    else:
        run = False

print("\nGrazie per aver scelto questo software!")