from flask import Flask
app= Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello Hana"
if __name__=="__main__":
    app.run(debug=True)
@app.route('/dojo')

def index():
    return "Dojo!"

@app.route('/say/flask')
def index1():
    return "Hi Flask!"

@app.route('/say/<name>')
def index2(name):
    return ""+name


@app.route('/repeat/<count>/<name>')
def index3(count,name):
    count=int(count)
    return render_template("index.html", phrase=name, times=count)	# notice the 2 new named arguments!
if __name__=="__main__":
    app.run(debug=True)  