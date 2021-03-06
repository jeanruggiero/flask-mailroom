import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('all'))


@app.route('/donations/')
def all():

    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/add_donation/', methods=["GET", "POST"])
def add_donation():
    """
    Add a new donation from an existing donor.
    """
    if request.method == "POST":
        print(request.form['donor'])
        Donation(value=int(request.form['amount']), donor=request.form['donor']).save()
        return redirect(url_for('all'))
    else:
        donors = Donor.select()
        return render_template('add_donation.jinja2', donors=donors)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

