from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contactList')
def contactList():
    return render_template('users list.html')


@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html', hobbies=['Listen to music', 'Play on harmonica', 'Solve crosswords','Travel', 'Bake'])
    #return render_template('assignment8.html', hobbies=['Listen to music'])
if __name__ == '__main__':
    app.run(debug=True)

