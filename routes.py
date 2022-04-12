from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
import sqlite3

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/savedetails', methods=['POST'])
def savedetails():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        with sqlite3.connect('employee.db') as con:
            cur = con.cursor()
            cur.execute('INSERT INTO Employees VALUES(NULL, ?, ?, ?)', (name, email, address))
            con.commit()
            msg="Data added Successfully"
            
            return render_template('success.html', msg=msg)

@app.route('/view')
def view():
    con = sqlite3.connect('employee.db')
    cur=con.cursor()
    cur.execute("SELECT * FROM Employees")
    rows=cur.fetchall()
    con.close()
    return render_template('view.html', rows=rows)
        
@app.route('/delete/<id>')
def deleteRecord(id):
    con = sqlite3.connect('employee.db')
    cur = con.cursor()
    cur.execute('DELETE FROM Employees WHERE id=?', (id,))
    con.commit()
    con.close()
    return redirect(url_for("view"))
    


if __name__=='__main__':
    app.run(debug=True)