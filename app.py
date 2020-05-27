from flask import Flask, render_template, url_for #import module Flask Framwork dan render template dari html atau jinja

app = Flask(__name__) #berfungsi untuk memanggil App File

@app.route('/') #python decorator di dalam funtion untuk memberitahu browser bahwa ini page pertama yang di reques
def home(): #funtion
    return render_template('home.jinja') #asumsikan file home.jinja ini adalah file home.html 

@app.route('/flask')
def flask():
    return render_template('flask.jinja')

if __name__=='__main__': #harus di definisikan supaya source code nya run
    app.run(debug=True) #debug True untuk mempermudah jika ada error dan bisa di perbaiki langsung di browser
