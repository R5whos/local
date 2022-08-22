from flask import Flask, render_template, jsonify, redirect
app = Flask(__name__, template_folder='template')


@app.route('/home', methods=["GET"])
def index():
    return render_template("index.html")
@app.route('/', methods=["GET"])
def redis():
    return redirect("/home", code=302)

@app.route('/mix', methods=["GET"])
def mix():
    return render_template("mix.html")

@app.route('/anonim', methods=["GET"])
def anonim():
    return render_template("anonim.html")

@app.route('/faq', methods=["GET"])
def faq():
    return render_template("faq.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
app.run(debug=True)