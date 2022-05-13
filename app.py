from flask import Flask, jsonify, request, render_template
from example_blueprint import example_blueprint


app = Flask(__name__)


# register blueprint from example_bluprint.py
app.register_blueprint(example_blueprint)


@app.route('/')                                             # Home Page
def home():
    return "Hello! Welcome to Flask API!"


# make a function which give the number is armstrong or not!
@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n > 0):
        digit = n % 10
        sum += digit**order
        n = n//10

    if (sum == copy_n):
        print(f"{copy_n} is an armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": True,
            "Server IP": "122.234.213.53"
        }
    else:
        print(f"{copy_n} is not an armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": False,
            "Server IP": "122.234.213.53"
        }
    return jsonify(result)


# Hndling Query strings

@app.route("/qs")
def qs():

    if request.args:
        req = request.args
        return " ".join(f"{k}: {v} " for k, v in req.items())

    return "No query"



# by defalut GET Method use here
@app.route('/person/')
def hello():
    # dd = {'Name':'Akshat','Blood': 'O+','id' : 14}
    # od = collections.OrderedDict(dd)
    # od['Name'] = 'Akshat'
    # od['Age'] = 23
    # od['Address'] = 'India'
    # od['Id'] = 74
    # return dd

    # return jsonify({'Name': 'Akshat', 'Age': 23, 'Address': 'India', 'Id': 4}, {'Hello': 'Hii', 'City': 'Pune', 'id': 23, 'Name': 'green'})

    # the data return in the form of Dict.
    return jsonify(id=23, account='premium', username='Hello', validity='200 days', name='Jaadu')


# POST Method without HTML File and with the help of test.py

@app.route('/login', methods=['POST'])
def login():
    # print(request)
    uname = request.form['uname']
    if uname == "ayush":
        return "Welcome %s" % uname
    elif uname == "akshat":
        return "Welcome %s" % uname
    else:
        return "User Name not found"


# POST Method with HTML File

@app.route('/name', methods =["GET","POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 
       return "".join(f"Your Name is {first_name} {last_name}")
    #    return "Your name is " + first_name  +  last_name 
    return render_template("login.html")




#   for the config file

# app.config["SERVER_NAME"] = "localhost"
# app.config["SECRET_KEY"] = "HG78IU"
# print(app.config["SECRET_KEY"])


# if app.config["ENV"] == "production":
#     app.config.from_object("config.ProductionConfig")
# else:
#     app.config.from_object("config.DevelopmentConfig")


# print(f'ENV is set to: {app.config["ENV"]}')
# app.config.from_object("config.DevelopmentConfig")
# print(app.config)


# PUT Method




# Error Handling

@app.errorhandler(404)
def handle_404(_error):
    return jsonify({'Error 404': 'Page Not Found'}), 404     # 404 error not found


@app.errorhandler(500)
def handle_500(_error):
    # if there is a internal server error
    return jsonify({'Error 500 ': 'Internal Server Error'}), 500

88
@app.errorhandler(405)
def handle_500(_error):
    return jsonify({'Error 405': 'Method Not Allowed'}), 405      # method not allowed

# @app.errorhandler(304)
# def handle_304(_error):
#     return jsonify({'Error 304': 'Not Found'}), 304       # TypeError

if __name__ == '__main__':
    app.run(debug=True)
