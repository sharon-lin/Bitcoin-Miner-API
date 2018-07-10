from flask import Flask
from flask_restful import Api, Resource, reqparse
from random import randint

app = Flask(__name__)
api = Api(app)

coins = 0

class Block(Resource):
    def get(self):
        global coins
        mined = randint(1, 1000000)*0.01
        coins += mined
        return "You have mined {} satoshi. There are currently {} satoshi.".format(mined, coins), 200

api.add_resource(Block, "/")

app.run(debug=True)
