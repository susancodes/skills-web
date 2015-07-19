from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    # Return this as a strange
    # return "<html><body>This is the homepage.</body></html>"
    return render_template("index.html")
    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def application_form():
	return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def application():
	firstname = request.form.get("firstname")
	lastname = request.form.get("lastname")
	salaryreq = request.form.get("salaryreq")
	jobtype = request.form.get("jobtype")
	return render_template("application.html", firstname=firstname, lastname=lastname, salaryreq=salaryreq, jobtype=jobtype)



if __name__ == "__main__":
    app.run(debug=True)