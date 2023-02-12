from flask import Flask, render_template, redirect, url_for
from forms import UserInput
from forms import Nexti
from forms import Budget

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
income=0
living=0
state=0
transport=0
insurance=0
Meal_Plan=0
loan=0
interest=0
total=0





@app.route('/', methods=('GET', 'POST'))
def index():
    form = UserInput()
    if form.validate_on_submit():
        if form.state.data=='In-state':
            state=3,812
        else:
            state==17,936
        if form.housing.data=='On Campus':
            housing=9000
        elif form.housing.data=='Off Campus':
            housing=9000
        else:
            housing=0
        if form.insurance.data=='No':
            insurance=2704
        else:
            insurance=0
        if form.meal_plan.data=='Yes':
            Meal_Plan=3,858
        else:
            Meal_Plan=0

       
        return redirect(url_for('next'))
    return render_template('index.html', form=form)

@app.route('/next/', methods=('GET', 'POST'))
def next():
    form=Nexti()
    if form.validate_on_submit():
        return redirect(url_for('spend')) 
    return render_template('next.html', form=form)
@app.route('/spend/', methods=('GET', 'POST'))
def spend():
    form=Budget()
    if form.validate_on_submit():
        return render_template('amounts.html')  
    return render_template('amounts.html', form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4600)