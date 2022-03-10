from flask import Flask, request, render_template, redirect, url_for
import employees as api

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('birthdays'))

@app.route('/birthdays')
def birthdays():
    return render_template('birthdays.html', **locals())


##############
##   APIs   ##
##############

@app.route('/get_birthdays', methods=['GET'])
def get_birthdays(month=None):
    month = request.args.get('month')
    employees = get_employees()
    birthdays = api.get_birthdays(int(month), employees)
    return birthdays


##############
##  Helper  ##
##############
def get_employees():
    return [
        {
            'id':1,
            'first_name': 'Maurice',
            'last_name': 'Materise',
            'birthday': '5/16/1993'
        },
        {
            'id':2,
            'first_name': 'Larkin',
            'last_name': 'Materise',
            'birthday': '7/4/2019'
        },
        {
            'id':3,
            'first_name': 'Smalls',
            'last_name': 'Materise',
            'birthday': '3/15/2013'
        },
        {
            'id':4,
            'first_name': 'Rasmus',
            'last_name': 'Asplund',
            'birthday': '12/3/1997'
        },
        {
            'id':5,
            'first_name': 'Dylan',
            'last_name': 'Cozens',
            'birthday': '2/9/2001'
        },
        {
            'id':6,
            'first_name': 'Peyton',
            'last_name': 'Krebs',
            'birthday': '1/26/2001'
        },
        {
            'id':7,
            'first_name': 'Jeff',
            'last_name': 'Skinner',
            'birthday': '5/16/1992'
        },
        {
            'id':8,
            'first_name': 'Tage',
            'last_name': 'Thompson',
            'birthday': '10/30/1997'
        },
        {
            'id':5,
            'first_name': 'Alex',
            'last_name': 'Tuch',
            'birthday': '5/10/1996'
        },
        {
            'id':9,
            'first_name': 'Josh',
            'last_name': 'Allen',
            'birthday': '5/21/1996'
        },
        {
            'id':10,
            'first_name': 'Stefon',
            'last_name': 'Diggs',
            'birthday': '11/29/1993'
        },
        {
            'id':11,
            'first_name': 'Jerry',
            'last_name': 'Hughes',
            'birthday': '8/13/1988'
        },
        {
            'id':12,
            'first_name': 'Micah',
            'last_name': 'Hyde',
            'birthday': '12/31/1990'
        },
        {
            'id':13,
            'first_name': 'Jordan',
            'last_name': 'Poyer',
            'birthday': '4/25/1991'
        },
        {
            'id':14,
            'first_name': 'Mitch',
            'last_name': 'Morse',
            'birthday': '4/21/1992'
        },
        {
            'id':15,
            'first_name': 'Dion',
            'last_name': 'Dawkins',
            'birthday': '4/26/1994'
        },
        {
            'id':16,
            'first_name': 'Gabriel',
            'last_name': 'Davis',
            'birthday': '4/1/1999'
        },
        {
            'id':17,
            'first_name': 'Matt',
            'last_name': 'Milano',
            'birthday': '7/28/1994'
        },
        {
            'id':18,
            'first_name': 'Don',
            'last_name': 'Granato',
            'birthday': '8/11/1967'
        },
        {
            'id':19,
            'first_name': 'Sean',
            'last_name': 'McDermott',
            'birthday': '3/21/1974'
        }
    ]
