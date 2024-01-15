from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/calculonotas', methods=['GET', 'POST'])
def calculoNotas():
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        numero3 = float(request.form['numero3'])
        numero4 = float(request.form['numero4'])

        resultado = round((numero1 + numero2 + numero3)/3,2)
        if numero4 >= 75 and resultado >= 40:
         resultado2 = str('APROBADO')
        else:
         resultado2 = str('REPROBADO')

        return render_template('calculonotas.html', resultado1=resultado, resultado2=resultado2)
    return render_template('calculonotas.html')


@app.route('/largonombre', methods=['GET', 'POST'])
def largoNombre():
    if request.method == 'POST':

        nom1 = request.form['nombre1']
        nom2 = request.form['nombre2']
        nom3 = request.form['nombre3']

        long1 = len(nom1)
        long2 = len(nom2)
        long3 = len(nom3)

        maxlong = len(max(nom1, nom2, nom3))

        nombre_max_long = []

        if long1 == maxlong:
            nombre_max_long.append(nom1)
            nombre_max_long.append(", ")
        if long2 == maxlong:
            nombre_max_long.append(nom2)
            nombre_max_long.append(", ")
        if long3 == maxlong:
            nombre_max_long.append(nom3)
            nombre_max_long.append(", ")


        return render_template('largonombre.html', resultado1="".join(nombre_max_long),resultado2=maxlong)
    return render_template('largonombre.html')

if __name__ == '__main__':
    app.run(debug=True)