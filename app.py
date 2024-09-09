from flask import Flask

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
app.run()
