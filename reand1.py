@app.route('/hello/<name>')
def hello(name=None):
    return render_template('rend.html', name=name)