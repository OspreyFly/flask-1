from flask import Flask, render_template, request, flash, redirect
import requests

app = Flask(__name__)
app.secret_key = "secretKey"

def convertCurrency(form_data):
    from_currency = form_data.get("from")
    to_currency = form_data.get("to")
    amount = form_data.get("amount")

    if not from_currency or not to_currency or not amount:
        flash("Input valid currencies and amount", "error")
        return None

    # Perform verification
    url = "https://api.exchangerate.host/symbols"
    response = requests.get(url)
    data = response.json()
    valid_currencies = set(data.get("symbols", {}).keys())

    if not (from_currency in valid_currencies and to_currency in valid_currencies):
        flash("Please enter valid three-letter currencies", "error")
        return None

    # Proceed with conversion
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}&places=2"
    response = requests.get(url)

    if response.status_code != 200:
        flash("Failed to retrieve exchange rate data", "error")
        return None

    data = response.json()
    return data

@app.route("/gohome", methods=["POST"])
def sendThem():
    return redirect("/forex")

@app.route("/forex")
def serveForm():
    return render_template("converter.html")

@app.route("/submit", methods=["POST"])
def convert():
    form_data = request.form
    data = convertCurrency(form_data)

    if data is not None:
        from_currency = form_data.get("from")
        to_currency = form_data.get("to")
        amount = form_data.get("amount")

        if from_currency == to_currency:
            result = float(amount)
        else:
            result = data.get("result")

        return redirect(f"/results/{result}?curr={to_currency}")
    else:
        return redirect("/forex")

@app.route("/results/<float:result>")
def showResult(result):
    curr = request.args.get("curr", "")
    currency_symbols = {
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥",
    }
    symbol = currency_symbols.get(curr, "")

    return render_template("results.html", result=result, symbol=symbol)

if __name__ == "__main__":
    app.run(debug=True)
