from flask import Flask, request, jsonify

app = Flask(__name__)

stocks = {
    1: {"name": "Apple Inc.", "symbol": "AAPL", "price": "2708.55B"},
    2: {"name": "Airbnb Inc", "symbol": "ABNB", "price": "77.27B"},
    3: {"name": "Exelixis Inc", "symbol": "EXEL", "price": "19B"},
    4: {"name": "Okta Inc", "symbol": "OKTA", "price": "69.82B"},
}



def generate_stocks_id():
    return max(stocks.keys()) + 1



@app.route("/stocks", methods=["POST"])
def create_stock():
    data = request.get_json()
    stock_id = generate_stocks_id()
    new_stock = {"name": data["name"], "symbol": data["symbol"], "price": data["price"]}
    stocks[stock_id] = new_stock
    return jsonify(new_stock), 201






@app.route("/stocks/<int:stock_id>", methods=["GET"])
def get_stock(stock_id):
    stock = stocks.get(stock_id)
    if stock is not None:
        return jsonify(stock)
    return "stock not found", 404

if __name__ == "__main__":
    app.run(port=5000, debug=True)