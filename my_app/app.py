from flask import Flask
# from my_app.views.relay_routes import views_app
from flask_restx import Api
from my_app.controllers.relay_routes import relay_ns
from my_app.controllers.dg_routes import dgip_ns

app=Flask(__name__)
# app.register_blueprint(views_app)
api = Api(app, 
          version='1.0', 
          title='Relay API', 
          description='API for controlling relays and digital inputs')


api.add_namespace(relay_ns)
api.add_namespace(dgip_ns)


if __name__ == '__main__':
    app.run(debug=True)
