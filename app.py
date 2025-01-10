from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

data = [
    {"id": 1, "name": "Produkt A", "price": 100},
    {"id": 2, "name": "Produkt B", "price": 200},
    {"id": 3, "name": "Produkt C", "price": 300},
    {"id": 4, "name": "Produkt D", "price": 400},
    {"id": 5, "name": "Produkt E", "price": 500},
]

@app.route("/")
def index():
    return render_template("index.html", data=data)

@app.route("/add", methods=["POST"])
def add_data():
    new_id = len(data) + 1
    new_name = request.form.get("name")
    new_price = request.form.get("price")
    data.append({"id": new_id, "name": new_name, "price": float(new_price)})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")