from flask import Flask,render_template,request,url_for

app = Flask(__name__)
credits_list = [25,25,25,24,25,24,22,16] 


@app.route("/",methods=["GET","POST"])
def index():
    if(request.method=="POST"):
        n = int(request.form["semn"])
        total=0
        credit_total=0
        for i in range(0,n):
            gpa = request.form["sem"+str(i+1)]
            total = total + (credits_list[i]*float(gpa))
            credit_total+=credits_list[i]
        result = total/credit_total
        return render_template("index.html",result=result)
    return render_template("index.html")

if(__name__=="__main__"):
    app.run(debug=True)
