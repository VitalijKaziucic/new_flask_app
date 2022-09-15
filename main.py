from flask import Flask, render_template, request
from year import check_year

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index1.html")


@app.route("/<name>")
def name(name):
    return render_template("index.html", name=name)


@app.route("/year")
def year():
    return render_template("index2.html")


@app.route("/check_year", methods=['GET', 'POST'])
def year_check():
    if request.method == "POST":
        data = request.form["year"]
        text = f"{data} metai yra keliamieji" if check_year(int(data)) else f"{data} metai yra nekeliamieji"
        return render_template("index4.html", txt=text)

    else:
        return render_template("index3.html")
