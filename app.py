from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, world! UwUr"

@app.route("/index")
def index():
    titulo= "IEVN1001"
    listado=["Python", "Flask", "HTML", "CSS", "JavaScript"]
    return render_template('index.html', titulo=titulo, listado=listado)


@app.route("/aporb")
def aporb():
    return render_template('aporb.html')

@app.route("/resultado", methods=['POST'])
def resultado():
    n1 = request.form.get("a")
    n2 = request.form.get("b")
    return "La multiplicación de {} y {} es {}.".format(n1, n2, int(n1)*int(n2))


@app.route("/distancia", methods=['POST', 'GET'])
def distancia():
    disti = " "

    if request.method == 'POST':

        x1 = request.form.get("x1")
        y1 = request.form.get("y1")
        x2 = request.form.get("x2")
        y2 = request.form.get("y2")

        x1 = float(x1)
        x2 = float(x2)
        y1 = float(y1)
        y2 = float(y2)

        disti = (((x2 - x1)**2 + (y2 - y1)**2)**0.5)
    return render_template('distancia.html', disti=disti)

@app.route("/figuras", methods=['GET', 'POST'])
def figuras():
    resultado = " "
    area = request.form.get("area") 

    if request.method == 'POST':

        if area == "cuadrado":
            lado = request.form.get("lado", 0)
            lado = float(lado)

            resultado = lado * lado

        elif area == "triangulo":
            base = request.form.get("base", 0)
            base = float(base)
            altura = request.form.get("altura", 0)
            altura = float(altura)

            resultado = (base * altura)/2

        elif area == "circulo":
            radio = request.form.get("radio", 0)
            radio = float(radio)

            resultado = 3.1416 * (radio **2)

        elif area == "rectangulo":
            base = request.form.get("base", 0)
            base = float(base)
            altura = request.form.get("altura", 0)
            altura = float(altura)

            resultado = base * altura

        elif area == "pentagono":
            perimetro = request.form.get("perimetro", 0)
            perimetro = float(perimetro)
            apotema = request.form.get("apotema", 0)
            apotema = float(apotema)

            resultado = perimetro * apotema /2

    return render_template("figuras.html", resultado=resultado, area=area)

@app.route("/holi")
def func():
    return "<h1>Holiiii</h1>"

@app.route("/adios/<string:user>")
def user(user):
    return "<h1>Bai, {}!</h1>".format(user)

@app.route("/square/<int:num>")
def square(num):
    return "<h1>El cuadrado de {} es {}</h1>".format(num, num**2)

@app.route("/repeat/<string:text>/<int:times>")
def repeat(text, times):
    return "<h1>" + " ".join([text] * times) + "</h1>"

@app.route('/suma/<float:a>/<float:b>')
def suma(a, b):
    return "<h1>La suma de {} y {} es {}</h1>".format(a, b, a + b)

@app.route("/prueba")
def func12():
    return


if __name__=='__main__':
    app.run(debug=True)
