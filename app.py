from flask import Flask, redirect, url_for, render_template, request, session, jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = '123456'





def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='ex10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


##assignment10 page
from blueprints.pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)








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



#--------------------------------
#--------assignment 11-----------

@app.route('/assignment11/', defaults={'database': 'users'})
@app.route('/assignment11/<database>')
def assignment11users(database):
    if database == 'users':
        query = "SELECT * FROM users order by NAME"
        query_result = interact_db(query=query, query_type='fetch')
        response = {}
        if len(query_result) !=0:
           response = query_result

        response = jsonify(response)
        return response
    else:
        return {}


@app.route('/assignment11/users/selected/', defaults={'SOME_USER_ID': '0'})
@app.route('/assignment11/users/selected/<int:SOME_USER_ID>')
def userID(SOME_USER_ID):
    if SOME_USER_ID == '0':
        query = "SELECT * FROM users WHERE ID='1'"
        query_result = interact_db(query=query, query_type='fetch')
        response = query_result[0]
        response = jsonify(response)
        return response

    query = "SELECT * FROM users WHERE ID='%s'" % SOME_USER_ID
    query_result = interact_db(query=query, query_type='fetch')

    response = {}
    if len(query_result) != 0 and SOME_USER_ID!=0:
        response = query_result[0]
        response = jsonify(response)
        return response
    else:
        error = 'The user is not exist'
        error = jsonify(error)
        return error


#--------assignment 11-----------
#--------------------------------



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

print(mydb)


if __name__ == '__main__':
    app.run(debug=True)


