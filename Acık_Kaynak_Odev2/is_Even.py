from flask import Flask, request
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

class CheckEven(Resource):
    def get(self, number):

        api_url = f'https://api.isevenapi.xyz/api/iseven/{number}'
        response = requests.get(api_url)

        if response.status_code == 200:
            result = response.json()
            return {'number': number, 'is_even': result['iseven']}, 200
        else:
            return {'message': 'Failed to retrieve data from external API'}, 500

api.add_resource(CheckEven, '/checkeven/<int:number>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6767)