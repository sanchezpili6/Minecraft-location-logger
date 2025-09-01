from flask import Flask
from flask_cors import CORS

from api.world_routes import world_blueprint
from api.location_routes import location_blueprint


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(world_blueprint)
    app.register_blueprint(location_blueprint)

    return app


app = create_app()

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=3000, debug=True)