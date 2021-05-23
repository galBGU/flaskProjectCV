from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = '123456'


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

@app.route('/assignment9', methods=['POST', 'GET'])
def assignment9():
    users_list = [
        {'Name': "Gal Shaked", 'ID':"311306351"},
        {'Name': "Or Cohen", 'ID': "123456789"},
        {'Name': "Noa Levi", 'ID': "102030405"},
        {'Name': "Amir Gat", 'ID': "111111111"},
        {'Name': "Haim Cohen", 'ID': "900000000"}
        ]

    name= ''
    ID=''
    current_method = request.method
    in_suers_list = False
    search_all = False
    searched = False

    if 'username' in session:
        user_name, password = session['username'], session['password']
    else:
        user_name=''
        password=''

    if current_method=='GET':
        if request.args:
            searched= True
            name = request.args['name']
            ID = request.args['ID']
            if name== '' and ID == '':
                search_all= True
            for user in users_list:
                if name in user.values() or ID in user.values():
                    in_suers_list = True
                    name = user.get('Name')
                    ID = user.get('ID')
            if not in_suers_list:
                name= 'user not found'
                ID= ''

    elif current_method == 'POST':
        if request.form:
            user_name = request.form['username']
            password = request.form['password']
        session['username'] = user_name
        session['password'] = password

    return render_template('assignment9.html',
                           parameters= request.args,
                           name=name,
                           id=ID,
                           user_name=user_name,
                           password=password,
                           current_method=current_method,
                           users_list= users_list,
                           search_all = search_all,
                           searched= searched
                           )

@app.route('/logout')
def logout():
    session.pop('username')
    session.pop('password')
    return redirect(url_for('assignment9'))


if __name__ == '__main__':
    app.run(debug=True)


