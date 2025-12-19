from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    emi = total = interest = None

    if request.method == "POST":
        loan = float(request.form["loan"])
        rate = float(request.form["rate"]) / 100 / 12
        months = int(request.form["years"]) * 12

        emi = loan * rate * (1 + rate) ** months / ((1 + rate) ** months - 1)
        total = emi * months
        interest = total - loan

        emi = round(emi, 2)
        total = round(total, 2)
        interest = round(interest, 2)

    return render_template(
        "index.html",
        emi=emi,
        total=total,
        interest=interest
    )

if __name__ == "__main__":
    app.run()
