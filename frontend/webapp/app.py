from flask_bcrypt import Bcrypt

from app_utils import create_app

if __name__ == "__main__":
    app = create_app()
    bcrypt = Bcrypt(app)
    app.run(debug=True, port=5000)
