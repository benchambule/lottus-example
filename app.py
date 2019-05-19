from flask import Flask, request, json, Response
import lottusapp

app = Flask(__name__)

lottus_app = lottusapp.get_lottus_app()

@app.route('/ussdapp/json/', methods=['POST'])
def ussd_json_api():
    js = json.dumps(request.json)
    req_dict = json.loads(js)
    print(req_dict)

    resp = lottus_app.handle_request(req_dict)

    return Response(json.dumps(resp), status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run()