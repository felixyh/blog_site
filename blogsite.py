from app import app, db

# # to ensure "flask db migrate -m "users table"" can detect the defined schema
from app import models 

# from app.models import User, Post

# # from flask_script import Shell

# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User, 'Post': Post}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)