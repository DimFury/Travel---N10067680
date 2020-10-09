from flask import Blueprint, render_template, request, session

mainbp = Blueprint('main',__name__)

@mainbp.route('/')
def index():
    return render_template('index.html')

# @mainbp.route('/login', methods=['GET','POST'])
# def login():
#     session['email']=request.values.get('email')
#     return render_template('login.html')

# @mainbp.route('/logout')
# def logout():
#     if 'email' in session:
#         session.pop('email', None)
#         return 'Session has been cleared'
