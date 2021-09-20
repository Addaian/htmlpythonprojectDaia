from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
    class Users:
        def __init__(self, name, email, password):
            self.name = name
            self.email = email
            self.email = password

        def function(email):
            check1 = 0
            a = (int(s) for s in email.split())
            for x in len(a):
                if a[x] == '@' and check1 == 0:
                   check1 = 1
                if a[x] == '.' and check1 ==1:
                    check2 = 1
            if check2 == 1:
                print("true")
            if check2 == 0:
                print("false")

        def function(password):
            if len(password) >= 6 and len(password) <= 12:
                a = (int(s) for s in password().split())
                for x in len(a):
                    if 97 <= ord(a[x]) <= 122:
                        check1 = 1
                    if 65 <= ord(a[x]) <= 90:
                        check2 = 1
                if check1 and check2 == 1:
                    print("true")
                else:
                    print("false")



