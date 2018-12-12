from flask import Flask, request
import urllib
import json


app = Flask(__name__)


@app.route('/', methods=['POST'])

def index():
#    webhook = json.loads(request.body)
 #   print (webhook['data']['id'])
#    return "idleboost"
    print ("-----\n")
    print (request.is_json)
    content = request.get_json()
    print (content)
    print ()
    print (content["id"])
    return 'JSON posted'


if __name__ == "__main__":
    app.run(debug=True, port=4996)