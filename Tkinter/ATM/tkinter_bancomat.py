import pickle
from tkinter import *
import matplotlib.pyplot as plt


class Contocorrente:
    def __init__(self, username, id, saldo):
        self.username = username
        self.id = id
        self.saldo = saldo
        self.categorie = ["Prelievi", "Versamenti", "Bonifici"]
        self.cifre = [[], [], []]

    def __str__(self):
        return f"Username: {self.username}, ID conto: {self.id}, Saldo: € {self.saldo}\n"


class Bancomat:
    def __init__(self, conti):
        self.conti = conti

    def __str__(self):
        return self.conti

    def prelievo(self, cifra, id):
        for i in self.conti:
            if i.id == id:
                if i.saldo > cifra:
                    i.saldo -= cifra
                    stampa = (f"Prelievo effettuato con successo\nIl saldo aggiornato è di € {i.saldo}")
                    i.cifre[0].append(cifra)
                    return stampa
                else:
                    stampa = "Saldo non disponibile"
                    return stampa

    def versamento(self, cifra, id):
        for i in self.conti:
            if i.id == id:
                i.saldo += cifra
                stampa = (f"Versamento effettuato con successo\nIl saldo aggiornato è di € {i.saldo}")
                i.versamenti += cifra
                i.cifre[1].append(i.versamenti)
                return stampa

    def bonifico(self, cifra, id):
        for i in self.conti:
            if i.id == id:
                if i.saldo > cifra:
                    i.saldo -= cifra + 1.50
                    stampa = (f"Bonifico effettuato con successo\nIl saldo aggiornato è di € {i.saldo}")
                    i.bonifici += cifra
                    i.cifre[2].append(i.bonifici)
                    return stampa
                else:
                    stampa = "Saldo non disponibile"
                    return stampa

    def stampa_saldo(self, id):
        for i in self.conti:
            if i.id == id:
                stampa = (f"Il saldo aggiornato è di € {i.saldo}")
                return stampa

    def mostra_movimenti(self, id):
        for i in self.conti:
            if i.id == id:
                fig, axes = plt.subplots(1, 2)
                # First graph
                # Dati da visualizzare
                categories = i.categorie
                values = [sum(i.cifre[0]), sum(i.cifre[1]), sum(i.cifre[2])]
                axes[0].bar(categories, values)
                axes[0].set_title("Istogramma")
                axes[0].set_xlabel("Categorie")
                axes[0].set_ylabel("Valori")
                # End first graph

                # Second graph
                # Dati da visualizzare
                labels = categories
                sizes = values
                colors = ['red', 'blue', 'green']
                # Creazione del grafico a torta
                axes[1].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
                axes[1].set_title("Grafico a torta")
                # End second graph

                plt.show()


"""
utente1 = Contocorrente("User 1", "01", int(10000))
utente2 = Contocorrente("User 2", "02", int(30000))
lista_utenti = []
lista_utenti.append(utente1)
lista_utenti.append(utente2)
b1 = Bancomat(lista_utenti)
f = open("testBancomat1.pkl", "wb")
pickle.dump(lista_utenti, f)
f.close()
"""


# Start code to center the window

def centerWindow(window):
    width = 600  # Width
    height = 400  # Height

    screen_width = window.winfo_screenwidth()  # Width of the screen
    screen_height = window.winfo_screenheight()  # Height of the screen

    # Calculate Starting X and Y coordinates for Window
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


# End code to center the window


f = open("testBancomat1.pkl", "rb")
unpickler = pickle.Unpickler(f)
lista_utenti = unpickler.load()
b1 = Bancomat(lista_utenti)
f.close()


def open_():
    user = password_entry.get()
    password = password_entry1.get()
    for el in lista_utenti:
        if user == el.username and password == el.id:
            # Define the function p inside the open function
            def p():
                importo = int(amount.get())
                output = b1.prelievo(importo, password)
                display_label.configure(text=output)

            def v():
                importo = int(amount.get())
                output = b1.versamento(importo, password)
                display_label.configure(text=output)

            def b():
                importo = int(amount.get())
                output = b1.bonifico(importo, password)
                display_label.configure(text=output)

            def s():
                output = b1.stampa_saldo(password)
                display_label.configure(text=output)

            def m():
                b1.mostra_movimenti(password)


            def close():
                f = open("testBancomat1.pkl", "wb")
                pickle.dump(lista_utenti, f)
                f.close()
                root.destroy()

            Preleva = Button(root, text="Preleva", command=p)
            Preleva.pack()
            Versa = Button(root, text="Versa", command=v)
            Versa.pack()
            Bonifico = Button(root, text="Bonifico", command=b)
            Bonifico.pack()
            Saldo = Button(root, text="Saldo", command=s)
            Saldo.pack()
            Movimenti = Button(root, text="Movimenti", command=m)
            Movimenti.pack()
            Logout = Button(root, text="Logout", command=close)
            Logout.pack()
            amount.pack()


# create root window
root = Tk()
root.geometry('300x300')
# root window title and dimension
root.title("Bancomat Talentform")
# Set geometry(widthxheight)
password_label = Label(root, text="Username:")
password_label.pack()
password_entry = Entry(root)
password_entry.pack()
password_label1 = Label(root, text="Password:")
password_label1.pack()
password_entry1 = Entry(root, show="*")
password_entry1.pack()
# Creazione del pulsante di login
login_button = Button(root, text="Login", command=open_)
login_button.pack()

amount = Entry(root)
amount.pack_forget()
display_label = Label(root)
display_label.pack()

centerWindow(root)

# Execute Tkinter
root.mainloop()
