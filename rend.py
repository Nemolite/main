from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/param/<name>")
def hello(name=None):
	#return render_template('rend.html')
    #return "Hello World!"
    return render_template('rend.html', name=name)


if __name__ == "__main__":
    app.run()


