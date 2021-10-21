from flask import Flask, render_template, request, redirect, url_for, flash
from handlers import create, decode, check

app = Flask(__name__)
app.secret_key = b'_5#y2L"G!@#$ddc6Q4z\n\xec]/' # Used for sessions.

@app.route("/", methods=['POST', 'GET'])
def index():
  secret = ""
  password = ""
  if request.method == 'POST':
      secret = request.form.get("secret")
      password = request.form.get("password")
  pagetitle = "Generate link for secret"
  return render_template("index.html",
                            secret = secret,
                            password = password,
                            mytitle=pagetitle,
                            mycontent="Hello Senz")

@app.route("/submit", methods=['POST'])
def submit():
    secret = request.form.get("secret")
    password = request.form.get("password")
    if request.method == 'POST' and secret != "" and password != "":
        pagetitle = "Secret link generated"

        save = create.Save(secret, password)
        save.createFile()
        return render_template("submit.html",
                            mytitle=pagetitle,
                            mycontent=secret,
                            password=password,
                            uid=save.uid,
                            date = save.date)
    else:
      if secret == "":
        flash('Secret is missing')
      if password == "":
        flash('Password is missing')
      return redirect(url_for("index"), code=307)

@app.route("/sec", methods=['GET'])
def sec():
    chk = check.Check(request.args['uid'])
    result = chk.checkExist()
    if chk.checkExist() == True:
      return render_template("sec.html", 
                          uid = request.args['uid'],
                          mytitle = "Reveal secret")
    else:
      flash("Secret might be destroyed")
      return redirect(url_for("index"))

@app.route("/get", methods=['POST'])
def get():
  if request.method == 'POST':
    uid = request.form.get('uid')
    password = request.form.get('password')
    date = request.form.get('date')
    secret = decode.Get(uid, password, date)
    if secret.decrypt() == False:
      flash("Incorrect credentials or secret might be destroyed")
      return redirect(url_for("index"))
    elif secret.decrypt() != False:
      result = secret.decrypt()
      secret.destroy()
      return render_template("get.html",
                      secret = result,
                      mytitle = "Retrieve Secret")
    else:
      flash("Method not allowed")
      return redirect(url_for("index"))
