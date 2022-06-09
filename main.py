from flask import Flask, request, render_template,url_for
from base import Base,Session,engine
from Models.Models import ToDo

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello_world():
    return render_template('mainPage.html',msg="")

@app.route('/list', methods=['get', 'post'])
def add():
    if request.method == 'POST':
        title = request.form.get("title")
        if title == '':
            return render_template('mainPage.html',msg="Title should not be empty")
        else:
            description = request.form.get("description")
            session = Session()
            todo = ToDo(title,description)
            session.add(todo)
            session.commit()
    else:
        title = request.args.get("title")
        description = request.args.get("description")
    return render_template('mainPage.html',msg = "Information Saved")

@app.route('/showList',methods=['get','post'])
def showList():
    session = Session()
    return render_template('table.html',lists = session.query(ToDo))

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    #app.run()
    app.run(host="0.0.0.0", debug=True)

