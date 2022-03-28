from flask import Flask, render_template, redirect, session, request 

app = Flask(__name__)
app.secret_key = "counter"
# our index route will handle rendering our form
@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 1
    else:    
        session["count"] += 1
    return render_template("index.html")

@app.route('/counter' , methods=['POST'])
def count():
    print("Got Post Info")
    if request.form["add_btn"]=="add":
        session["count"] += 1
    elif request.form["add_btn"]=="rest":
        session["count"] = 0

    return redirect("/")

@app.route('/destory')
def destroy():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)  