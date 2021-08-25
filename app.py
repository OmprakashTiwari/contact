import smtplib
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def first():
    return render_template("contact.html")

@app.route('/detail',methods=['GET','POST'])
def data():
    
    if (request.method=="POST"):
        
        x=request.form['name']
        y=request.form['ph']
        z=request.form['Emailid']
        v=request.form['gn']
        w=request.form['msg']
        
        xyz=x+y+z+v+w
        sub=(f"Thank you {x} for Interest we will help you regarding this query")
        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login("omprakashec1052@gmail.com","Omprakash@238")
        server.sendmail("omprakashec1052@gmail.com", z,sub)
        
        return render_template("contact.html",op=xyz)
if __name__=='__main__':
    app.run()