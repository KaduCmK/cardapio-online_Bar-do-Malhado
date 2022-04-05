from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comidas')
def comidas():
    return render_template('comidas.html')

@app.route('/bebidas')
def bebidas():
    return render_template('bebidas.html')

if __name__ == '__main__':
    app.run(debug=False)