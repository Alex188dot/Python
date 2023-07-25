from flask import Flask, request, render_template, make_response
import mysql.connector
from datetime import datetime

pwd = 'your-db-pwd'



"""

Esercizio supermarket

Creare un programma supermarketFlask che rappresenta la gestione di un supermercato online. Inizialmente creare l’interfaccia per l’utente: l’utente può scegliere tra 4 select prodotti da banco, prodotti freschi, prodotti da frigo, inoltre nell’ultima select  possiamo scegliere tra vari elettrodomestici. In questo programma l’utente può anche scegliere di non selezionare alcuni prodotti (stringa vuota o null). Inoltre una volta effettuato l’ordine il programma va a scrivere su una tabella mysql i dati. ATTENZIONE: tra i dati sono presenti la mail e la password dell’utente, e quindi i relativi cookie dei dati di sessione.


"""




class Prodotto:
    def __init__(self, id, prezzo):
        self.id = id
        self.prezzo = prezzo


    def __str__(self):
        return f"{self.prezzo}"

# Prodotti confezionati
pasta = Prodotto(1, 1)
riso = Prodotto(2, 1.5)
paneInCassetta = Prodotto(3, 1.2)

# Prodotti freschi
lattuga = Prodotto(4, 1.2)
cetrioli = Prodotto(5, 1.3)
carne = Prodotto(6, 8)

# Prodotti da frigo
ricotta = Prodotto(7, 4)
provola = Prodotto(8, 3.5)
latte = Prodotto(9, 1.5)

# Elettrodomestici
ferroDaStiro = Prodotto(10, 35)
lavatrice = Prodotto(11, 350)
asciugaCapelli = Prodotto(12, 49)

sceltaNulla = Prodotto(0, 0)

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('flask_supermarket_login.html')

@app.route('/register')
def register_page():
    return render_template('flask_supermarket_register.html')


@app.route('/registrate', methods=['POST'])
def registration():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=pwd,
            database='Talentform'
        )
        cursor = connection.cursor()
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        last_access = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO users3 (email, username, password, last_access) VALUES (%s, %s, %s, %s)"
        values = (email, username, password, last_access)
        cursor.execute(query, values)
        connection.commit()
        print("Dati salvati correttamente nel database.")
        response = make_response('Cookie impostati con successo!')
        response.set_cookie('username', username)
        response.set_cookie('last_access_time', datetime.now().isoformat())
        msg = "Registrazione effettuata con successo"
    except mysql.connector.Error as error:
        print("Errore durante il salvataggio dei dati:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return render_template('flask_supermarket_login.html', msg=msg)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pwd,
        database="Talentform"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Talentform.users3;")
    myresult = mycursor.fetchall()
    conta = []
    for x in myresult:
        if username not in x and password not in x:
            conta.append("0")
        elif username in x and password in x:
            conta.append("1")
            if conta.count("1") == 1:
                # Leggi il cookie esistente, se presente
                last_access_time = request.cookies.get('last_access_time')
                msg = f"Bentornato {username}! Scegli tra i prodotti disponibili per la tua spesa a domicilio: "
                return render_template('flask_supermarket_choose_product.html', msg=msg, last_access_time=last_access_time)
            #elif conta.count("1") == 0:
                #msg = "Username or password not valid"
                #return render_template('flask_supermarket_login.html', msg=msg)

@app.route('/order', methods=['POST'])
def order():
    cart = []
    confezionati = request.form['confezionati']
    freschi = request.form['freschi']
    frigo = request.form['frigo']
    elettrodomestici = request.form['elettrodomestici']
    if confezionati == "0":
        confezionati = ""
        cart.append(int(sceltaNulla.prezzo))
    elif confezionati == "1":
        confezionati = "Pasta"
        cart.append(int(pasta.prezzo))
    elif confezionati == "2":
        confezionati = "Riso"
        cart.append(int(riso.prezzo))
    elif confezionati == "3":
        confezionati = "Pane in cassetta"
        cart.append(int(paneInCassetta.prezzo))
    if freschi == "4":
        freschi = "Lattuga"
        cart.append(int(lattuga.prezzo))
    elif freschi == "5":
        freschi = "Cetrioli"
        cart.append(int(cetrioli.prezzo))
    elif freschi == "6":
        freschi = "Carne"
        cart.append(int(carne.prezzo))
    elif freschi == "0":
        freschi = ""
        cart.append(int(sceltaNulla.prezzo))
    if frigo == "7":
        frigo = "Ricotta"
        cart.append(int(ricotta.prezzo))
    elif frigo == "8":
        frigo = "Provola"
        cart.append(int(provola.prezzo))
    elif frigo == "9":
        frigo = "Latte"
        cart.append(int(latte.prezzo))
    elif frigo == "0":
        frigo = ""
        cart.append(int(sceltaNulla.prezzo))
    if elettrodomestici == "10":
        elettrodomestici = "Ferro da Stiro"
        cart.append(int(ferroDaStiro.prezzo))
    elif elettrodomestici == "11":
        elettrodomestici = "Lavatrice"
        cart.append(int(lavatrice.prezzo))
    elif elettrodomestici == "12":
        elettrodomestici = "Asciuga Capelli"
        cart.append(int(asciugaCapelli.prezzo))
    elif elettrodomestici == "0":
        elettrodomestici = ""
        cart.append(int(sceltaNulla.prezzo))
    prezzo = sum(cart)
    username = request.cookies.get('username')
    ordine = f"La sua spesa: {confezionati}, {freschi}, {frigo}, {elettrodomestici}. Il totale è: {prezzo}€"
    # This code will retrieve the email of the user
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pwd,
        database="Talentform"
    )
    mycursor = mydb.cursor()
    sql = f"SELECT * FROM users3 WHERE username ='{username}'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    email = ""
    for x in myresult:
        email = x[1]
    # This code will add the order to the DB
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pwd,
        database="Talentform"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO prodotti_scelti (confezionati, freschi, frigo, elettrodomestici, username, email, totale) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (confezionati, freschi, frigo, elettrodomestici, username, email, prezzo)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Scelta registrata")
    return render_template('flask_supermarket_order.html', ordine=ordine)








if __name__ == "__main__":
    app.run(debug=True)