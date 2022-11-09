from app import app
from flask import render_template
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
    return render_template('login.html', title='Sign In', form=form)

    
