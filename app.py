from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home_get():
    return render_template('index.html')

@app.route('/Registraion')
def re_get():
    return render_template('Registraion.html')


@app.route('/Login')
def Login_get():
    return render_template('Login.html')


if __name__ == "__main__":
    app.run(debug=True)