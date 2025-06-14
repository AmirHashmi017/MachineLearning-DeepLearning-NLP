from flask import Flask,render_template,request,jsonify
import sqlite3
app=Flask(__name__)

# Now Defining RESTfull APIs
# GET API to get list of tasks
@app.route("/")
def welcome():
    return render_template("to_do_list.html")

@app.route("/tasks",methods=["GET"])
def get_tasks():
    connection=sqlite3.connect("Todo_List.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    data=cursor.fetchall()
    connection.close()
    tasks=[{'Id':row[0],'Name':row[1],'Description':row[2]} for row in data]
    return jsonify(tasks)

@app.route("/tasks/<id>",methods=['GET'])
def get_tasks_by_id(id):
    connection=sqlite3.connect("Todo_List.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id=?",(id,))
    data=cursor.fetchall()
    connection.close()
    tasks=[{'Id':row[0],'Name':row[1],'Description':row[2]} for row in data]
    return jsonify(tasks)

@app.route("/tasks",methods=["POST"])
def Add_Task():
    if not request.json and not 'name' in request.json and not 'description' in request.json:
        return jsonify({'Error':'Please provide Name and Description.'})
    name=request.json['name']
    description=request.json['description']
    connection=sqlite3.connect("Todo_List.db")
    cursor=connection.cursor()
    cursor.execute('''INSERT INTO tasks(name,description) VALUES(?,?)''',(name,description))
    connection.commit()
    connection.close()
    return jsonify({'Success':'Task successfully added to list'})

@app.route("/tasks/<id>",methods=["PUT"])
def update_task(id):
    name=request.json['name'] if 'name' in request.json else ""
    description=request.json['description'] if 'description' in request.json else ""
    if name=="" or description=="":
        return jsonify({'Error':'Provide both name and description to update'})
    connection=sqlite3.connect("Todo_List.db")
    cursor=connection.cursor()
    cursor.execute('''UPDATE tasks SET name=?,description=? WHERE id=?''',(name,description,id))
    connection.commit()
    connection.close()
    return jsonify({'Success':'Successfully Updated Task'})

@app.route("/tasks/<id>",methods=['DELETE'])
def delete_task(id):
    connection=sqlite3.connect("Todo_List.db")
    cursor=connection.cursor()
    cursor.execute('''DELETE FROM tasks WHERE id=?''',id)
    rows_deleted=cursor.rowcount
    connection.commit()
    connection.close()
    return jsonify({'Success':f'{rows_deleted} deleted successfully'})






if __name__=="__main__":
    def setup_database():
        connection=sqlite3.connect("Todo_List.db")
        cursor=connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       description TEXT NOT NULL)''')
        connection.commit()
        connection.close()

    setup_database()
    app.run(debug=True)