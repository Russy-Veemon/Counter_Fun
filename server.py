from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'OWNOWbrownCOW1983'

@app.route('/')
def home():
    return redirect('/home')

@app.route('/home')
def count():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] +=1
    return render_template("counter.html")

@app.route('/plustwo')
def plustwo():
    session["count"] +=2
    return render_template("counter.html")

@app.route('/userplus', methods=['POST'])
def user_plus():
    session['count'] += int(request.form['add_this_many'])
    #this creates an immutable dictionary, I have to take the integer value form the dictionary and add it to the session count
    return render_template("counter.html")

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/home')

@app.route('/<path:path>')
def not_found(path):
    return redirect('/home')


if __name__ == '__main__':
    app.run(debug=True)