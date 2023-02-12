from flask_wtf import FlaskForm
from wtforms import (IntegerField, RadioField)
from wtforms.validators import InputRequired
class UserInput(FlaskForm):
        state = RadioField('Are you in-state or out-of-state?',
                       choices=['In-state', 'Out-of-State'],
                       validators=[InputRequired()])

        housing = RadioField('Where are you planning to live?',
                       choices=['On Campus', 'Off Campus','At Home'],
                       validators=[InputRequired()])
        transport = RadioField('Do you have a car',
                       choices=['Yes', 'No'],
                       validators=[InputRequired()])
        insurance = RadioField('Do you have insurance',
                       choices=['Yes', 'No'],
                       validators=[InputRequired()])
        meal_plan = RadioField('Do you have a meal plan',
                       choices=['Yes', 'No'],
                       validators=[InputRequired()])
class Nexti(FlaskForm):
        income = IntegerField('Income(Can include financial aid, scholorships and parental support)', validators=[InputRequired()])
        loan = RadioField('Do you have a loan? If yes what type of loan?',
                       choices=['No Loan', 'Subsidized Loan','Private Loan','Unsubsidized Loan'],
                       validators=[InputRequired()])
        interest_rate=IntegerField('Loan Interest Rate,Enter 0 if no loan.',validators=[InputRequired()])
        amount=IntegerField('Loan Amount, Enter 0 if no loan',validators=[InputRequired()])
        years=IntegerField('How many years left in college',validators=[InputRequired()])
        term=IntegerField('What is the loan term. Enter 0 if no loan',validators=[InputRequired()])

class  Budget(FlaskForm):
        entertainment = IntegerField('How much do you want to spend on entertainment', validators=[InputRequired()])

        clothing=IntegerField('How much do you want to spend on clothing',validators=[InputRequired()])
        food=IntegerField('How much do you want to spend on food',validators=[InputRequired()])
        things=IntegerField('How much do you want to spend on other things?',validators=[InputRequired()])
        invest=IntegerField('How much do you want to invest',validators=[InputRequired()])


        
        
