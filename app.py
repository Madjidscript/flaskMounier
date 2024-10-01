from flask import Flask, render_template,request
import datetime
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/heure")
def heure():
    date= datetime.datetime.now()
    h = date.hour
    m = date.minute
    s = date.second
    return render_template("heure.html", heure=h,minute=m,second=s)



liste_eleves=[
        {"nom":"yaya","prenom":"madjid","rang":"1er","classe":"2c"},
        {"nom":"kone","prenom":"issa","rang":"2emme","classe":"2c"},
        {"nom":"konan","prenom":"abraham","rang":"1er","classe":"2a"},
        {"nom":"toure","prenom":"tidiane","rang":"2em","classe":"2a"},
        {"nom":"coulibaly","prenom":"ousmane","rang":"1er","classe":"tc"},
        {"nom":"diarra","prenom":"aboubacar","rang":"2eme","classe":"tc"},
    ]
@app.route("/eleves")
def eleves():
    classes= request.args.get("c")
    if classes :
       eleves_select= [ele for ele in liste_eleves if ele["classe"]==classes]
    else:
        eleves_select=[]
    return render_template("eleves.html",eleves=eleves_select)
   
if __name__ == '__main__':
    app.run(debug=True)
