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

@app.route("/distancia", methods=['POST'])
def distancia():
    x1 = request.form.get("x1")
    y1 = request.form.get("y1")
    x2 = request.form.get("x2")
    y2 = request.form.get("y2")
    return "<h1>La distancia entre los puntos es {}</h1>".format((((x2-x1)**2)((y2-y1)**2)*(1/2)))

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
