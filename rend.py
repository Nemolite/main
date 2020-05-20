from flask import Flask
from flask import render_template
from flask import request



app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def reder():
	temp = request.data
    print(temp)
	return render_template('inx.html',temp)
    

if __name__ == "__main__":
    app.run()


