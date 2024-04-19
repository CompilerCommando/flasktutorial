from flask import Flask, render_template

app = Flask(__name__)

#Create a route

@app.route('/')
def index():
    name_list = ["Kevin", "Amylia", "John"]
    sentence = "This is <strong>Bold</strong> Text!"
    return render_template("user.html",
                            names=name_list,
                            sentence=sentence)


#localhost:5000/user/kevin
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)
