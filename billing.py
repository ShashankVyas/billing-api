# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from flask import jsonify, Flask, abort
from flask import Request, Response, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/api/v1/billing/total", methods=['GET'])
def calculatetotal():

    if 'qty' in request.args:
        qty = int(request.args['qty'])
        return_str = {
                'id': 0,
                'qty': qty
            }

        return jsonify(return_str), 200
    else:
        error_str = {
            'status' : 500,
            'errorMessage' : "Quantity is not present in the input params"
        }
        return jsonify(error_str), 500

    if 'price' in request.args:
        qty = int(request.args['price'])
        return_str = {
                'id': 0,
                'price': qty
            }

        return jsonify(return_str), 200
    else:
        error_str = {
            'status' : 500,
            'errorMessage' : "Price is not present in the input params"
        }
        return jsonify(error_str), 500


# Press the green button in the gutter to run the script.
app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
