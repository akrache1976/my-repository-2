from flask import Flask, render_template

app = Flask (__name__)  

@app.route('/')
def head():
    first="This is my first condition experience"
    return render_template("index.html", message = False )

@app.route('/mohammed')
def header():
    name = ["Jhon", "James", "Paul", "Nina"]
    return render_template("body.html", object = name)


if __name__=="__main__":
    #app.run(debug=True)
    app.run(hot='0.0.0.0', port=80)
   
