#importamos la libreria Flask
from traceback import print_tb
from flask import Flask,jsonify, render_template, url_for, flash, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt
from bson import ObjectId
from bson.json_util import dumps






app = Flask(__name__, template_folder='templates')


#-----
app.config['MONGO_DBNAME'] = 'educativa'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/educativa'

mongo = PyMongo(app)

#---------------------------------------
#Administrador
#---------------------------------------

@app.route('/')
def administrador():
    if 'username' in session:
        return render_template('/RegistratUser.html')
    return render_template('/selectUser.html')

@app.route('/loginAd', methods=['POST'])
def loginAd():
    users = mongo.db.Users
    login_user = users.find_one({'name' : request.form['username']})
    login_pass = users.find_one({'password' : request.form['pass']}) 
    login_admin = "Administrador" 

    if login_user != None:
        if login_pass:
            if login_admin == request.form['Tusuario']:
                session['username'] = request.form['username']
                return redirect(url_for('administrador'))
            else:
                flash("Acceso Denegado")
                return render_template('loginAd.html')
        else:
            flash("Contaseña Incorrecta")
            return render_template('loginAd.html')
    else:
        flash("Usuario No encontrado")
        return render_template('loginAd.html')
  

#Iniciar Sesion Administrador
@app.route('/loginAd')
def logAd():
    return render_template('/loginAd.html')


#---------------------------------------
#Registrar Administrador
#---------------------------------------
@app.route('/registerUsuario', methods=['POST', 'GET'])
def registerD():
    if request.method == 'POST':
        users = mongo.db.Users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            if 'submitButton' in request.form:
                users.insert_one({
                    'nombre' : request.form['nombre'], 
                    'apellido' : request.form['apellido'],
                    'name' : request.form['username'], 
                    'password' : request.form['pass'],
                    'TUsuario' : 'Administrador', })
                session['username'] = request.form['username']
            return redirect(url_for('administrador'))
        return 'That username already exists!'
    return render_template('/RegistratUser.html')

#---------------------------------------
#Registrar Alumnno
#---------------------------------------
@app.route('/registerAlumno', methods=['POST', 'GET'])
def registerAl():
    if request.method == 'POST':
        users = mongo.db.Users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            if 'submitButtonAlumno' in request.form:
                users.insert_one({
                    'nombre' : request.form['nombre'], 
                    'apellido' : request.form['apellido'],
                    'name' : request.form['username'], 
                    'password' : request.form['pass'],
                    'foto' : request.form['foto'],
                    'paralelo' : request.form['paralelo'],
                    'TUsuario' : 'Alumno', })
                session['username'] = request.form['username']
            return redirect(url_for('alumnoReg'))
        return 'That username already exists!'
    return render_template('/RegistroAlumno.html')

@app.route('/alumno')
def alumnoReg():
    if 'username' in session:
        return render_template('/RegistroAlumno.html')
    return render_template('/selectUser.html')


#---------------------------------------
#Registrar Docente
#---------------------------------------
@app.route('/registerDocente', methods=['POST', 'GET'])
def registerDoc():
    if request.method == 'POST':
        users = mongo.db.Users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            if 'submitButtonAlumno' in request.form:
                users.insert_one({
                    'nombre' : request.form['nombre'], 
                    'apellido' : request.form['apellido'],
                    'name' : request.form['username'], 
                    'password' : request.form['pass'],
                    'clase' : request.form['paralelo'],
                    'TUsuario' : 'Docente', })
                session['username'] = request.form['username']
            return redirect(url_for('docenteReg'))
        return 'That username already exists!'
    return render_template('/RegistroAlumno.html')

@app.route('/docente')
def docenteReg():
    if 'username' in session:
        return render_template('/RegistroDocente.html')
    return render_template('/selectUser.html')

#---------------------------------------
# Alumno
#---------------------------------------
@app.route('/Juegos')
def juegos():
    if 'username' in session:
        return redirect(url_for('verAlumnosActual'))
    return render_template('/selectUser.html')

@app.route('/JuegosP')
def juegosP():
    if 'username' in session:
        return redirect(url_for('verAlumnosActualP'))
    return render_template('/selectUser.html')

@app.route('/OpcionesJuegos')
def OpcionesJuegos():
    if 'username' in session:
        return  render_template('/opciones.html')
    return render_template('/selectUser.html')



@app.route('/loginAl', methods=['POST'])
def loginAl():
    users = mongo.db.Users
    login_user = users.find_one({'name' : request.form['username']})
    login_pass = users.find_one({'password' : request.form['pass']}) 
    login_alum = "Alumno" 

    if login_user != None:
        if login_pass:
            if login_alum == request.form['Tusuario']:
                session['username'] = request.form['username']
                return redirect(url_for('OpcionesJuegos'))
            else:
                flash("Acceso Denegado")
                return render_template('loginAl.html')
        else:
            flash("Contaseña Incorrecta")
            return render_template('loginAl.html')
    else:
        flash("Usuario No encontrado")
        return render_template('loginAl.html')
        
#Iniciar sesion Alumno
@app.route('/loginAl')
def logAl():
    return render_template('/loginAl.html')

#---------------------------------------
#Docente
#---------------------------------------

@app.route('/docente')
def docente():
    if 'username' in session:
        return redirect(url_for('verAlumnos'))
    return render_template('/selectUser.html')
    
@app.route('/loginD', methods=['POST'])
def loginD():
    users = mongo.db.Users
    login_user = users.find_one({'name' : request.form['username']})
    login_pass = users.find_one({'password' : request.form['pass']}) 
    log_claseA = "A" 
    log_claseB = "B" 
    login_doc = "Docente" 

    if login_user != None:
        if login_pass:
            if login_doc == request.form['Tusuario']:
                if log_claseA == request.form['clase']:
                    session['username'] = request.form['username']
                    return redirect(url_for('verAlumnosA'))
                elif log_claseB == request.form['clase']:
                        session['username'] = request.form['username']
                        return redirect(url_for('verAlumnosB'))
        else:
            flash("Contaseña Incorrecta")
            return render_template('loginD.html')
    else:
        flash("Usuario No encontrado")
        return render_template('loginD.html')
        

#Iniciar Sesion Docente
@app.route('/loginDo')
def logDo():
    return render_template('/loginD.html')

#---------------------------------------
#Guardar Calificacion
#---------------------------------------
@app.route('/registroCalificacion', methods=['POST', 'GET'])
def registroCalificacion():
    if request.method == 'POST':
            calificacion = mongo.db.Calificaciones
            calificacion.insert_one({
                'idAlumno' : request.form['idAlumno'], 
                'nombre' : request.form['nombre'], 
                'score' : request.form['score'], })
    return redirect(url_for('OpcionesJuegos'))



#Ver Alumnos
@app.route('/verAlumnosActualP')
def verAlumnosActualP():
    users = mongo.db.Users
    login_userActual = users.find_one({'name' : session['username']})
    print(login_userActual)
    return render_template("JuegoMemoriasPractica.html", login_userActual = login_userActual)


#Ver Alumnos
@app.route('/verAlumnosActual')
def verAlumnosActual():
    users = mongo.db.Users
    login_userActual = users.find_one({'name' : session['username']})
    print(login_userActual)
    return render_template("JuegoMemoria.html", login_userActual = login_userActual)


#---------------------------------------
#Cerrar Sesion
#---------------------------------------
@app.route('/login')
def CerrarSession():
    session.pop('username',None)
    return render_template('/selectUser.html')




#Ruta a app administrador
@app.route('/loginAdmin')
def logAdmin():
    return render_template('/administrador.html')

#Ruta a app docente
@app.route('/RegisterUsers')
def logUser():
    return render_template('/RegistratUser.html')

#Ruta a app alumno
@app.route('/loginAlumno')
def logAlumno():
    return render_template('/IAlumnos.html')

#Ruta a app JuegoNaves
@app.route('/JuegoNaves')
def JuegoNaves():
    return render_template('/JuegoNaves.html')

#Ruta a app JuegoMemorias
@app.route('/JuegoMemorias')
def JuegoMemorias():
    return render_template('/JuegoMemoria.html')

#Ruta a app JuegoMemorias
@app.route('/JuegoTresEnRaya')
def JuegoTresEnRaya():
    return render_template('/indexTresEnRaya.html')



#Ver Alumnos
@app.route('/verAlumnosA')
def verAlumnosA():    
    Alumn_list = mongo.db.Users.find({'paralelo' : "A"})
    return render_template("paralelos.html", Alumn_list = Alumn_list)

#Ver Alumnos
@app.route('/verAlumnosB')
def verAlumnosB():
    Alumn_list = mongo.db.Users.find({'paralelo' : "B"})
    return render_template("paralelos.html", Alumn_list = Alumn_list)













#---------------------------------------
#iniciamos la aplicacion
if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
