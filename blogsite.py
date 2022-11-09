from app import app
from app import models
# from flask_script import Shell

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', debug=True)