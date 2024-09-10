from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/hi/<b>')
def fun(b):
    return 'hai all friends'+b

@app.route('/greater/<int:a>/<int:b>/<int:c>')
def fun1(a,b,c):
    if a>b and a>c:

        return 'greatest number is:'+str(a)
    elif b>a and b>c:

        return 'greatest number is:'+str(b)
    else :

        return 'greatest number is:'+str(c)

@app.route('/rev/<int:a>')
def fun2(a):
    reverse = 0

    while a > 0:
        digit = a % 10
        reverse = (reverse * 10) + digit
        a = a // 10
    return 'reverse is'+str(reverse)

@app.route('/reverse/<int:a>')
def fun3(a):
    # reverse_number=""
    # for i in str(a)[::-1]:
    #     reverse_number=reverse_number + str(i)
        return 'reverse of number is :'+a[::-1]

@app.route('/new')
def new():
    return render_template('new.html') 
@app.route('/',methods=['POST','GET'])
def firstpage():
    if request.method=="POST":
        name1=request.form["name"]
        place1=request.form["place"]
        print(name1,place1)

    return render_template('1stpage.html')
@app.route('/2ndpage')
def secondpage():
    return render_template('2ndpage.html')

@app.route('/bill',methods=['POST','GET'])
def bill():
    chrg=''
    if request.method=="POST" :
        unit=int(request.form["unit"])  
        if unit<=100:
            chrg="no charges"
        elif unit<=200:  
            chrg=(unit-100)*5

        else:
            chrg=(unit-200)*10+500
    return render_template('bill.html',chrg=chrg) 

@app.route('/city',methods=['POST','GET'])
def city():
    mmt=''
    if request.method=="POST":
        city=request.form["city"]
        if city=="Delhi":
            mmt="Red Fort"
        elif city=="agra":
            mmt="Taj Mahal"
        elif city=="jaipur":
            mmt="Jal Mahal"

        else:
            print('no monument found')            
    return render_template('city.html',mmt=mmt) 


@app.route('/date',methods=['POST','GET'])
def date():
    day=''
    if request.method=="POST":
        date=int(request.form["date"])
        if date==1:
            day='sunday'
        elif date==2:
            day='monday' 
        elif date==3:
            day='tuesday' 
        elif date==4:
            day='wednesday' 
        elif date==5:
            day='thursday'
        elif date==6:
            day='friday' 
        elif date==7:
            day='saturday' 

        else:
            day='invalid id'  
    return render_template('day.html',day=day) 
    
@app.route('/costprice',methods=['POST','GET'])
def costprice():
    tax=''
    if request.method=="POST":
        costprice=int(request.form["costprice"])
        if costprice > 100000:
            tax_percentage = 0.15 * costprice
            tax=tax_percentage
        elif costprice > 50000:
            tax_percentage = 0.10 * costprice
            tax=tax_percentage
        else:
            tax_percentage = 0.05 * costprice
            tax="tax:",tax_percentage
    return render_template('costprice.html',tax=tax) 
       
@app.route('/bonus',methods=['POST','GET'])
def bonus():
    bonus_amount=''
    if request.method=="POST":
        year=int(request.form["year"])
        salary=int(request.form["salary"])
        if year >5:
            bonus_amount = 0.05 * salary
           
        else:
            bonus_amount = 'You are not eligible'

    return render_template('bonus.html',bonus_amount=bonus_amount)

@app.route('/lastdigit',methods=['POST','GET'])
def lastdigit():
    lastnum=''
    if request.method=="POST":
        lastdigit=int(request.form["lastdigit"])
        if lastdigit % 3 == 0:
            lastnum="The last digit of the number is divisible by 3."
        else:
            lastnum="The last digit of the number is not divisible by 3."
    return render_template('lastdigit.html',lastnum=lastnum)

    
app.run()
 