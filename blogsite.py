from app import app

# to ensure "flask db migrate -m "users table"" can detect the defined schema
from app import models 

# from flask_script import Shell

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', debug=True)