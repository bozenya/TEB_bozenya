#from flask import Flask
import flask
 
app=flask.Flask(__name__)

def parity(v):
    return "Nieparzyste" if v % 2 == 1 else Parzyste

@app.route('/')
def start():
    return flask.render_template('index.html')
    #return '<h1>Podstawowa strona WWW</h1>'

@app.route('/ajax/<page>', methods = ['POST'])
def get_page(page):
    #print(f'pages/{page}.html')
    return flask.render_template(f'pages/{page}.html')
    #return '<p>Pobrano WWW!</p>'

@app.route('/wiedza/<id>')
def wiedza(id):
    m = parity(int(id))
    return flask.render_template('wiedza.html', identyficator=id, mody=m)
    #m =  "Przykład"
    #if int(id) % 2 == 1:
    #    m = "Nieparzyste"
    #else:
    #    m = "Parzyste"
    

@app.route('/przelicznik')
def przelicznik():
    return flask.render_template('przelicznik.html')


