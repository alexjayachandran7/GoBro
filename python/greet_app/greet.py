from flask import Flask, request, jsonify

app = Flask(__name__)

def greet(name):
    return f"Hello, {name}!"

@app.route("/")
def home():
    return "Greet API is running 🚀"

@app.route("/greet", methods=["GET"])
def greet_api():
    name = request.args.get("name", "Guest")
    message = greet(name)
    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(debug=True)