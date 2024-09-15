from flask import Flask, render_template, request
from graph import QuadraticFunc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jk6jr1uj7jr#ekl3gh'

@app.route('/')
def load_index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def info():
    try:
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        c = float(request.form.get('c'))
        qf = QuadraticFunc(a, b, c)
        w = qf.f_kwadratowa()
    except:
        w = "Tylko liczby!!!"
    return render_template("index.html", blad1=w)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)