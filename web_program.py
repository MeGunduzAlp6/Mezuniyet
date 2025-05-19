from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def web_skin():
    return render_template("web_skin.html")

@app.route('/iklim_degisikligi')
def iklim_degisikligi():
    return render_template("iklim_degisikligi.html")

@app.route('/iklim_degisikligi2')
def iklim_degisikligi2():
    return render_template("iklim_degisikligi2.html")

@app.route('/iklim_degisikligi3')
def iklim_degisikligi3():
    return render_template("iklim_degisikligi3.html")

@app.route('/iklim_degisikligi4')
def iklim_degisikligi4():
    return render_template("iklim_degisikligi4.html")

if __name__ == "__main__":
    app.run(debug=True)
