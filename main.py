import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/create/', methods=["GET", "POST"])
def update_donations():

    if request.method == "GET":
        return render_template('update.jinja2')

    else:

        # It should retrieve the donor from the database with the indicated name
        donor_name = Donor.select().where(Donor.name == request.form['Name']).get()

        # and create a new donation with the indicated donor and donation amount.
        Donation.update(value=request.form['Donation'])\
                .where(Donation.donor == donor_name)\
                .execute()

        # Then it should redirect the visitor to the home page.
        return redirect(url_for('home'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)
    

if __name__ == "__main__":
    # port = int(os.environ.get("PORT", 6738))
    # app.run(host='0.0.0.0', port=port)

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
