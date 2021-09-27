from flask import Flask, render_template


class Users:
    def __init__(self, fname, lname, email, password):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password

    def email_func(self, email):
        check1 = 0
        check2 = 0
        a = [self.email.split()]
        for x in a:
            if a[x] == '@' and check1 == 0:
                check1 = 1
            if a[x] == '.' and check1 == 1:
                check2 = 1
        if check2 == 1:
            return "correct"
        if check2 == 0:
            return "change password"

    def password_func(self, password):
        if 6 <= len(self.password) <= 12:
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


myUser = Users("adrian", "dai", "adandian3@gmail.com", "12345")
print(myUser.fname, myUser.lname)
myUser.email_func("adandian3@gmail.com")
print(myUser.fname, myUser.lname)

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
