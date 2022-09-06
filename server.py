from flask import Flask, render_template 

app= Flask(__name__)

#Ejercicio 1
@app.route('/')
def index():
    return render_template('index.html')



#ejercicio 2
@app.route('/<int:num>')
def index2(num):
    x= int(num/2)
    print(x)
    return render_template('index2.html', numero=num, numero2=int(x))


#Ejercicio 3
@app.route('/<int:num>/<int:num2>')
def index3(num,num2):
    x= int(num/2)
    y = int(num2/2)
    print(x)
    print(y)
    return render_template('index3.html', num=int(x), num2=int(y))




if __name__=="__main__":
    app.run(debug=True)
