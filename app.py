from flask import Flask, render_template,send_from_directory, request
from firebase import firebase
import sqlite3

app = Flask(__name__,template_folder='template')

#Accessing firebase page
firebase = firebase.FirebaseApplication('https://noddht-default-rtdb.firebaseio.com/', None)

def create_connection():
    conn = sqlite3.connect('contact.db')
    return conn


# Function to create a table in the database if it does not exist
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       email VARCHAR NOT NULL,
                       message CHAR NOT NULL)''')
    conn.commit()

@app.route('/')
def index():

    #Connecting HTML page
    return render_template('index.html')

@app.route('/images/<path:filename>')
def get_image(filename):
    return send_from_directory('images', filename)

@app.route('/Home')
def Home():

    # getting real-time data from firebase

    result = firebase.get('/DHT', None)
    temperature = result['temperature']
    humidity = result['humidity']

    # Connecting HTML page

    return render_template('Home.html', temperature=temperature, humidity=humidity)
@app.route('/State')
def state():

    # getting real-time data from firebase

    result = firebase.get('/DHT', None)
    temperature = result['temperature']
    humidity = result['humidity']
    t = temperature
    h = humidity

    #pondicherry

    py_t_1 = t - 28.1
    py_h_1 = h - 71

    py_t_2 = t - 27.9
    py_h_2 = h - 70

    py_t_3 = t - 28
    py_h_3 = h - 72

    py_t_4 = t - 28.1
    py_h_4 = h - 73

    py_t_5 = t - 28.4
    py_h_5 = h - 71

    #chennai

    ch_t_1 = t - 28.5
    ch_h_1 = h - 69

    ch_t_2 = t - 28.3
    ch_h_2 = h - 69.5

    ch_t_3 = t - 28.3
    ch_h_3 = h - 71

    ch_t_4 = t - 28.4
    ch_h_4 = h - 72

    ch_t_5 = t - 28.6
    ch_h_5 = h - 70

    #kerala

    kl_t_1 = t - 27.9
    kl_h_1 = h - 78

    kl_t_2 = t - 27.4
    kl_h_2 = h - 78.6

    kl_t_3 = t - 27.5
    kl_h_3 = h - 79.25

    kl_t_4 = t - 28.2
    kl_h_4 = h - 78.6

    kl_t_5 = t - 28
    kl_h_5 = h - 78

    #Karnataka

    ka_t_1 = t - 24.3
    ka_h_1 = h - 73

    ka_t_2 = t - 23.7
    ka_h_2 = h - 74

    ka_t_3 = t - 23.9
    ka_h_3 = h - 72

    ka_t_4 = t - 24.3
    ka_h_4 = h - 73

    ka_t_5 = t - 24.6
    ka_h_5 = h - 74

    #andhra pradesh

    tl_t_1 = t - 28
    tl_h_1 = h - 69

    tl_t_2 = t - 27.4
    tl_h_2 = h - 70.5

    tl_t_3 = t - 27.5
    tl_h_3 = h - 65

    tl_t_4 = t - 27.4
    tl_h_4 = h - 66

    tl_t_5 = t - 27.4
    tl_h_5 = h - 69

    # Connecting HTML page

    return render_template('State.html', pyt1=py_t_1, pyt2=py_t_2, pyt3=py_t_3, pyt4=py_t_4, pyt5=py_t_5,
                                                           pyh1=py_h_1, pyh2=py_h_2, pyh3=py_h_3, pyh4=py_h_4, pyh5=py_h_5,
                                                           cht1=ch_t_1, cht2=ch_t_2, cht3=ch_t_3, cht4=ch_t_4, cht5=ch_t_5,
                                                           chh1=ch_h_1, chh2=ch_h_2, chh3=ch_h_3, chh4=ch_h_4, chh5=ch_h_5,
                                                           klt1=kl_t_1, klt2=kl_t_2, klt3=kl_t_3, klt4=kl_t_4, klt5=kl_t_5,
                                                           klh1=kl_h_1, klh2=kl_h_2, klh3=kl_h_3, klh4=kl_h_4, klh5=kl_h_5,
                                                           kat1=ka_t_1, kat2=ka_t_2, kat3=ka_t_3, kat4=ka_t_4, kat5=ka_t_5,
                                                           kah1=ka_h_1, kah2=ka_h_2, kah3=ka_h_3, kah4=ka_h_4, kah5=ka_h_5,
                                                           tlt1=tl_t_1, tlt2=tl_t_2, tlt3=tl_t_3, tlt4=tl_t_4, tlt5=tl_t_5,
                                                           tlh1=tl_h_1, tlh2=tl_h_2, tlh3=tl_h_3, tlh4=tl_h_4, tlh5=tl_h_5,)

@app.route('/Country')
def country():

    # getting real-time data from firebase

    result = firebase.get('/DHT', None)
    temperature = result['temperature']
    humidity = result['humidity']
    t = temperature
    h = humidity

    # INDIA

    t_1 = t - 25.93
    h_1 = h - 49

    t_2 = t - 25.78
    h_2 = h - 53

    t_3 = t - 25.86
    h_3 = h - 51.5

    t_4 = t - 25.9
    h_4 = h - 50.7

    t_5 = t - 26.04
    h_5 = h - 50

    t_6 = t - 26.2
    h_6 = h - 49.6

    t_7 = t - 25.92
    h_7 = h - 53.8

    t_8 = t - 25.73
    h_8 = h - 47.5

    t_9 = t - 25.68
    h_9 = h - 47

    t_10 = t - 25.6
    h_10 = h - 49.3

    # Connecting HTML page

    return render_template('Country.html', t1=t_1, t2=t_2, t3=t_3, t4=t_4, t5=t_5, t6=t_6, t7=t_7, t8=t_8, t9=t_9, t10=t_10,
                                                             h1=h_1, h2=h_2, h3=h_3, h4=h_4, h5=h_5, h6=h_6, h7=h_7, h8=h_8, h9=h_9, h10=h_10)

@app.route('/About_us')
def aboutus():

    # Connecting HTML page
    return render_template('About_us.html')

@app.route('/About_project')
def aboutproject():

    # Connecting HTML page
    return render_template('About_project.html')

@app.route('/Event')
def event():

    # Connecting HTML page
    return render_template('Event.html')

@app.route('/Feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Store data in the database
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, message) VALUES (?, ?, ?)", (name, email, message))
        conn.commit()
        conn.close()

    # Connecting HTML page
    return render_template('Feedback.html')

if __name__ == '__main__':
    conn = create_connection()
    create_table(conn)
    conn.close()

    app.run(debug=True)
