from flask import Flask
import os 

app = Flask(__name__)

route = os.getenv("ROUTE")

@app.route(f"/{route}")
def hello():
    msg = os.getenv("MSG")
    return f"Server said: {msg}"