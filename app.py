from flask import *

app = Flask(__name__)
    

@app.route('/', methods= ['GET'])  #establecer ruta inicial
def inicio():  #definir funcion
    return render_template('index.html') #llamar al html

