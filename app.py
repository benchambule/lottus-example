from flask import Flask, request, json, Response
import lottusapp
import lottus

app = Flask(__name__)

lottus_app = lottusapp.get_lottus_app()


@app.route('/ussdapp/json/', methods=['POST', 'GET'])
def ussd_json_api():
    js = json.dumps(request.json)
    req_dict = json.loads(js)
    print(req_dict)

    resp = lottus_app.process_request(req_dict)
    resp = lottus.create_window_response(resp)
    print(resp)

    return Response(json.dumps(resp), status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=True)