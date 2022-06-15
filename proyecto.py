from markupsafe import escape
from flask import Flask, render_template,request,redirect
app = Flask(__name__, template_folder= 'templates')

#Lista dónde se almacenará los nombres de los ponentes
lista= []
#ruta - Página 

@app.route('/')
@app.route('/about.html')
#metodo que llama a la pagina
def pag_about():
    return render_template('about.html')

@app.route('/')
@app.route('/agponente.html')
#metodo que llama a la pagina
def pag_ponet():
    return render_template('agponente.html')

#ruta - Página 
@app.route('/')
@app.route('/contact.html')
#metodo que llama a la pagina
def pag_contac():
    return render_template('contact.html')

@app.route('/')
@app.route('/formatos.html')
#metodo que llama a la pagina
def pag_format():
    return render_template('formatos.html')

@app.route('/')
@app.route('/index.html')
#metodo que llama a la pagina
def pag_index():
    return render_template("index.html")
#ruta - Página 

@app.route('/')
@app.route('/services.html')
#metodo que llama a la pagina
def pag_servi():
    return render_template("services.html")

#ruta - Página 

@app.route('/')
@app.route('/team.html')
#metodo que llama a la pagina
def pag_team():
    return render_template("team.html")
#ruta - Página 

    

@app.route('/')
@app.route('/login.html')
#metodo que llama a la pagina
def pag_log():
    return render_template("login.html",lista =lista)
#ruta - Página 

@app.route('/enviar', methods=[ 'POST'])

#Función para enviar la lista
def enviar():
 if request.method == 'POST':
		
		# Esto lo hacemos con el diccionario "form"
		tarea = request.form.get('tareaI')
		lista.append(tarea)
		# Retornamos la respuesta a la página index
		return redirect('/login.html')
#Define la ruta borrar, y para que acepte las peticiones POST.
@app.route("/borrar", methods=['POST'])

#Función para borrar la lista
def borrar():
    if request.method == 'POST':
		
		# Esto lo hacemos con el diccionario "form"
        tarea = request.form.get('tareaB')
        lista.remove(tarea) 
		# Retornamos la respuesta a la página index
        return redirect('/login.html')


if __name__ == '__main__':
    #debug = True, para reiniciar automáticamente el servidor
    app.run(debug=True)