from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = 'secret'

@app.route("/")
def home():
    return redirect(url_for("specialday"))

@app.route("/special_day", methods=["POST", "GET"])
def specialday():
    if request.method == "POST":
        opt = request.form.get("response")
        if opt == "yes":
            return redirect(url_for("see_this"))    
    return render_template("specialday.html")  # Make sure this matches your actual template filename

@app.route("/want_to_see_this",methods=["POST","GET"])
def see_this():
    return render_template("seethis.html")

@app.route("/message", methods=["POST"])
def message():
    return render_template("last.html")

# Add this route to handle music continuation
@app.route("/continue_music")
def continue_music():
    return redirect(url_for("see_this"))

if __name__ == "__main__":
    app.run(debug=True)