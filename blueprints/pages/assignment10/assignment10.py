from flask import Blueprint, render_template, request, redirect
import mysql
from app import interact_db

assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         static_url_path='/assignment10',
                         template_folder='templates')


#@assignment10.route('/assignment10')
#def index():
#    return render_template('assignment10.html')

@assignment10.route('/assignment10')
def users():
    query = "SELECT * FROM users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)


@assignment10.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        name = request.form['Name']
        id = request.form['ID']
        query = "INSERT INTO users(Name, ID) VALUES ('%s','%s')" % (name, id)
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10')
    return render_template('insert_user.html', req_method=request.method )


@assignment10.route('/update_user', methods=['GET', 'POST'])
def update_user():
    if request.method == 'POST':
        new_name = request.form['new_name']
        user_id = request.form['ID']
        query = "UPDATE users SET Name = '%s' WHERE ID = '%s'" % (new_name , user_id)
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10')
    return render_template('update_user.html', req_method=request.method)




@assignment10.route('/delete_user', methods=['POST'])
def delete_user():
    user_id = request.form['ID']
    query = "DELETE FROM users WHERE ID='%s';" % user_id
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')
