from flask import Flask, render_template, url_for
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/entretenimiento')
def entretenimiento():
    return render_template('entretenimiento.html')
@app.route('/ventas')
def ventas():
    return render_template('ventas.html')

if __name__=="__main__":
    app.run(debug=True)