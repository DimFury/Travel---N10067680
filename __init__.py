from flask import Flask
from flask_bootstrap import Bootstrap



def create_app():
    print(__name__)
    app = Flask(__name__)
    app.secret_key = 'anythingyoulike'
    app.debug = True

    from . import views
    app.register_blueprint(views.mainbp)
    
    from . import authentication
    app.register_blueprint(authentication.bp)

    from . import destinations
    app.register_blueprint(destinations.bp)

    
    bootstrap = Bootstrap(app)
    return app
