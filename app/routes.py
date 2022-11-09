from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Felix_Yang'}
    posts = [
        {
            'author': {'username': 'Felix_Yang'},
            'body': 'Beautiful day in portland!'
        },
        {
            'author': {'username': 'Nancy_Yang'},
            'body': 'I am a student in primary school!'
        }
    ]

    return render_template('index.html', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if request.method == 'POST':
    #     if request.form.get('username') == 'Felix' and request.form.get('password') == '111':
    #         return redirect(url_for('index'))
    #     else:
    #         flash('Wrong username or password, please login again!')

    # use flaskWTF validation
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
        
    return render_template('login.html', title='Sign In', form=form)