import pickle

"""
Scrivere una classe contocorrente che rappresenta un conto corrente bancario. Il conto è rappresentato da uno username, 
un id e un saldo. Successivamente scrivere la classe bancomat che inizializza una lista di contocorrente e permette 
di prelevare dal conto, versare sul conto, fare un bonifico, visualizzare il saldo (plus se nel saldo riusciamo 
a visualizzare la lista movimenti). Inoltre scrivere un programma che permette all'utente di usufruire del bancomat 
dopo aver digitato lo username e l'id corretto associato al conto.

Write a checking account class that represents a checking account. The account account includes a username,
an id and the balance. Then write an ATM class that initializes a current account list and allows
to withdraw from the account, deposit into the account, make a transfer and view the balance (plus if possible, 
implement the function to display the transaction list). Also write a program that allows the user to use the ATM
after entering the correct username and ID associated with the account.

"""


class Contocorrente:
    def __init__(self, username, id, saldo):
        self.username = username
        self.id = id
        self.saldo = saldo
        self.movimenti = []

    # I created the methods in the checking account instead of in the ATM

    def prelevare(self, importo):
        self.saldo -= importo

    def versare(self, importo):
        self.saldo += importo

    def bonifico(self, importo):
        self.saldo = self.saldo - importo - 1.5
    # Transfer to another user function: 1.5 represents the fee in euros to pay for the transfer.
    def visualizzare(self):
        return self.saldo

    def __str__(self):
        return f"Username: {self.username} - ID: {self.id} - Saldo: {self.saldo}"


class Bancomat:
    def __init__(self, lista):
        self.lista = lista

    def __str__(self):
        return f"{self.lista}"


c1 = Contocorrente("Mario", 100, 2000)
# print(c1)
c2 = Contocorrente("Luigi", 101, 2000)
# print(c2)
lista = []
b1 = Bancomat(lista)
b1.lista.append(c1)
b1.lista.append(c2)


def read_account():
    f = open("conto.pkl", "rb")
    unpickler = pickle.Unpickler(f)
    b1.lista = unpickler.load()
    f.close()

def save():
    f = open("conto.pkl", "wb")
    pickle.dump(b1.lista, f)
    f.close()
    print("Saved")


inp = input("Benvenuto nel BANCOMAT di Banca Python. Premere invio per continuare")

accesso = False
while accesso == False:
    username = input("Per accedere ai servizi della banca, digitare il proprio username: ")
    id = int(input("Per accedere ai servizi della banca, digitare la propria ID: "))
    for c in b1.lista:
        if c.username == username and c.id == id:
            print("Credenziali corrette, accesso effettuato correttamente")
            accesso = True
            cliente = c

while inp != "5":
    read_account()
    inp = input(
        """
    Inserire uno dei seguenti pulsanti per avviare la corrispondente operazione:
    1) Prelevare dal conto
    2) Versare sul conto
    3) Fare un bonifico ad un altro utente 
    4) Visualizzare il proprio saldo e la lista degli ultimi movimenti
    5) Logout
    
    """)
    if inp == "1":
        importo = int(input("Inserire l'importo da prelevare: "))
        for c in b1.lista:
            if c.id == cliente.id:
                if importo < c.saldo:
                    c.prelevare(importo)
                    print("Importo prelevato correttamente, il suo saldo è:", c.saldo)
                    c.movimenti.append(f"Prelievo: -{importo}")
                    save()
                else:
                    print("Importo troppo elevato, liquidità insufficiente sul proprio conto ")
    elif inp == "2":
        importo = int(input("Inserire l'importo da versare: "))
        for c in b1.lista:
            if c.id == cliente.id:
                c.versare(importo)
                print("Operazione effettuata con successo, questo è il suo nuovo saldo:", c.saldo)
                c.movimenti.append(f"Versamento: +{importo}")
                save()
    elif inp == "3":
        importo = int(input("Inserire l'importo del bonifico: "))
        for c in b1.lista:
            if c.id == cliente.id:
                if importo < c.saldo:
                    id = int(input("Inserire l'ID dell'utente a cui inviare il bonifico: "))
                    for i in b1.lista:
                        if i.id == id:
                            c.bonifico(importo)
                            c.movimenti.append(f"Bonifico in uscita: -{importo}")
                            i.versare(importo)
                            i.movimenti.append(f"Bonifico in entrata: +{importo}")
                            print("Bonifico effettuato con successo, questo è il suo nuovo saldo:", c.saldo)
                            save()
                else:
                    print("Importo troppo elevato, liquidità insufficiente sul proprio conto ")
    elif inp == "4":
        for c in b1.lista:
            if c.id == cliente.id:
                print("Questo è il suo saldo:", c.saldo)
                print(f"Questa è la lista degli ultimi movimenti:")
                for mov in c.movimenti:
                    print(mov)
    elif inp == "5":
        save()
        print("Logout effettuato con successo")
        break
    else:
        print("Scelta non valida, inserisca un numero tra quelli qui sotto: ")
