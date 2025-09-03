from flask import Flask
from products.controllers.product_controller import product_controller
from db.db import db
from flask_cors import CORS
from config import Config

app = Flask(__name__)
app.secret_key = 'secret123'
app.config.from_object(Config)
db.init_app(app)

# Registrando el blueprint del controlador de productos
app.register_blueprint(product_controller)
CORS(app, supports_credentials=True)

@app.get("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run()
