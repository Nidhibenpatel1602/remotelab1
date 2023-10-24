from ariadne import QueryType, ObjectType, gql, make_executable_schema
from ariadne.asgi import GraphQL

# Create a QueryType for your GraphQL queries
query = QueryType()
stock = ObjectType("Stock")

stock_data = {
    "Insta": {
        "historical_price_data": [150.0, 155.0, 160.0, 165.0, 170.0],
        "highest_price": 170.0,
        "lowest_price": 150.0,
        "trading_volume": 1000000,
    },
    "Facebook": {
        "historical_price_data": [2200.0, 2250.0, 2300.0, 2350.0, 2400.0],
        "highest_price": 2400.0,
        "lowest_price": 2200.0,
        "trading_volume": 500000,
    },
    
}

@query.field("stockInfo")
def resolve_stock_info(*_, name):
    stock_info = stock_data.get(name)
    if stock_info:
        return {
            "name": name,
            "historical_price_data": stock_info["historical_price_data"],
            "highest_price": stock_info["highest_price"],
            "lowest_price": stock_info["lowest_price"],
            "trading_volume": stock_info["trading_volume"],
        }
    return None

# Define your GraphQL schema
type_defs = gql("""
    type Stock {
        name: String
        historical_price_data: [Float]
        highest_price: Float
        lowest_price: Float
        trading_volume: Float
    }

    type Query {
        hello: String
        stockInfo(name: String): Stock
    }
""")

schema = make_executable_schema(type_defs, query, stock)






# Create a GraphQL application
app = GraphQL(schema, debug=True)




if __name__ == "__main__":
    from uvicorn import run
    run(app , port=5000)