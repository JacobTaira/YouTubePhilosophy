from flask import Flask


# set up website and define routes
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY'] = 'adsfasdfa asdfasdfa'

    from .views import views # <-- [file name] import [Blueprint name]
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    #app.register_blueprint(auth, url_prefix='/')

    return app