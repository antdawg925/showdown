import json
import random
from flask import Flask, render_template, request, redirect, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.m_pirate import Pirate
from flask_app.models.m_ninja import Ninja
import jsonpickle



#                                        CHECK IF NINJA OR PIRATE GET A SPEED BONUS
#  # YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY

@app.route('/ninja/bonus')
def check_ninja_bonus():
    michelangelo = jsonpickle.decode(session['ninja'])
    pizza = random.randint( 1,10 )
    if ( pizza > 4 ):
        bonus = random.randint( 3,12 )

        michelangelo.strength += bonus
        session['ninja'] = jsonpickle.encode(michelangelo)

        return render_template('ninja_bonus.html', bonus=bonus)
    return redirect('/ninja/lunge')
    

# # ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ


#                                            INITIAL ATTACK, CAN POTENTIALLY BE DODGED
#  # YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
@app.route('/ninja/lunge')
def ninja_lunge ():
    # print(phrases['Jack'][random.randint(1,4)])
    jack_sparrow = jsonpickle.decode(session['pirate'])
    michelangelo = jsonpickle.decode(session['ninja'])

    prob= random.randint(1,10)
    if (prob >= 5):
        return redirect ('/ninja/strike')
    else: 
        jack_sparrow.health -= michelangelo.strength
        session['pirate'] = jsonpickle.encode(jack_sparrow)

    return redirect('/pirate/dodge')
# ------------------------------------------------------------------------------------
@app.route('/pirate/dodge')
def pirateDodge ():
    jack_sparrow = jsonpickle.decode(session['pirate'])
    michelangelo = jsonpickle.decode(session['ninja'])

    dodge= random.randint(5,15)
    if(dodge<=jack_sparrow.strength):
        jack_sparrow.health -=0
        return render_template('p_dodge.html')
    else:
        jack_sparrow.health -= michelangelo.strength
        session['pirate'] = jsonpickle.encode(jack_sparrow)

    return redirect('/keep/fighting')

# # ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ


#                                             STRIKE PIRATE FOR DAMAGE
#  YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY

@app.route('/ninja/strike')
def ninja_strike ():
    jack_sparrow = jsonpickle.decode(session['pirate'])
    michelangelo = jsonpickle.decode(session['ninja'])

    jack_sparrow.health -= michelangelo.strength/(jack_sparrow.shield)

    if jack_sparrow.health <= 0:
            return redirect('/ninja/won')
    session['pirate'] = jsonpickle.encode(jack_sparrow)
    session['ninja'] = jsonpickle.encode(michelangelo)

    return render_template('n_strike.html' , jack_sparrow=jack_sparrow, michelangelo=michelangelo)

# # ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ

@app.route('/ninja_stats')
def ninja_stats():

    michelangelo = jsonpickle.decode(session['ninja'])

    return render_template('/n_stats.html', michelangelo=michelangelo)