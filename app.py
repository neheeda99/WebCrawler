from flask import Flask, render_template, request,session

from DBConnection import Db

app = Flask(__name__)
app.secret_key="aa"


@app.route('/')
def hello_world():
    return render_template('login_index.html')
@app.route('/login_post', methods=['post'])
def login_post():
    uname = request.form['textfield']
    psword = request.form['textfield2']
    qry="select * from login where uname='"+uname+"' and password='"+psword+"'"
    db=Db()
    res=db.selectOne(qry)
    print(qry)
    if res is not None:

        return '''<script>alert('Login Successfully');window.location='/userhome'</script>'''

    else:
        return '''<script>alert('Invalid user');window.location='/'</script>'''


@app.route('/user_reg')
def user_reg():
    return render_template('user_reg.html')
@app.route('/user_reg_post',methods=["post"])
def user_reg_post():
    name=request.form["textfield"]
    place=request.form["textfield3"]
    email=request.form["textfield6"]
    phone=request.form["textfield7"]
    password=request.form["password"]
    d=Db()
    q1="insert into login(uname,password)values('"+email+"','"+password+"')"
    lid=d.insert(q1)
    q="insert into user(name,email,phone,place,lid)values('"+name+"','"+email+"','"+phone+"','"+place+"','"+str(lid)+"')"
    d.insert(q)
    return '''<script>alert('success');window.location='/user_reg'</script>'''
@app.route('/userhome')
def userhome():
    return render_template('user_home.html')
@app.route('/crwalering')
def crwalering():
    return render_template('crwaler.html')
@app.route('/crwqler_post',methods=["post"])
def crwqler_post():
    import cgi
    from bs4 import BeautifulSoup
    import urllib3
    from urllib.request import urlopen
    import json
    import re

    name=request.form["keyw"]
    url = "http://s.taobao.com/search?q=" + name
    page = urlopen(url)
    soup = BeautifulSoup(page)
    print(soup)
    return soup
if __name__ == '__main__':
    app.run()
