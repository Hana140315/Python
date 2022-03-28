from flask import Flask, render_template, request
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    print("Got Post Info")
    print(request.form)
    name= request.form['name']
    Location= request.form['Location']
    language= request.form['Language']
    comment=request.form['Comment']
    
    return render_template("result.html", name_res=name, Location_res=Location, Language_res=language, Comment_res=comment)

    
if __name__ == "__main__":
    app.run(debug=True)
