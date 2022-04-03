import json
import random
import math
from flask import Flask, render_template, request, redirect, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.m_pirate import Pirate
from flask_app.models.m_ninja import Ninja
import jsonpickle


#                                        CHECK IF NINJA OR PIRATE GET A SPEED BONUS
#  # YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY

@app.route('/pirate/bonus')
def check_pirate_bonus( ):
    jack_sparrow = jsonpickle.decode(session['pirate'])
    
    rum = random.randint( 1,10 )
    if ( rum > 4 ):
        bonus = random.randint( 3,12 )
        # decode the pickle to access this 
        jack_sparrow.strength += bonus
        session['pirate'] = jsonpickle.encode(jack_sparrow)

        return render_template('pirate_bonus.html', bonus=bonus)
    return redirect('/pirate/lunge')
    

# # ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ



#                                            INITIAL ATTACK, CAN POTENTIALLY BE DODGED
#  # YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
@app.route('/pirate/lunge')
def pirate_lunge ():
    # print(phrases['Jack'][random.randint(1,4)])
    jack_sparrow = jsonpickle.decode(session['pirate'])
    michelangelo = jsonpickle.decode(session['ninja'])

    prob= random.randint(1,10)
    if (prob >= 5):
        return redirect('/ninja/dodge')
    else: 
        michelangelo.health -= jack_sparrow.strength
        session['ninja'] = jsonpickle.encode(michelangelo)
        return redirect('/keep/fighting')

    
# ------------------------------------------------------------------------------------
@app.route('/ninja/dodge')
def ninjaDodge ():
    jack_sparrow = jsonpickle.decode(session['pirate'])
    michelangelo = jsonpickle.decode(session['ninja'])

    dodge= random.randint(5,15)
    if(dodge<=michelangelo.strength):
        michelangelo.health -=0
        print(' Gotta be quicker than that DUUDDDEE!!!')
        return render_template('n_dodge.html')
    else:
        michelangelo.health -= jack_sparrow.strength
        session['ninja'] = jsonpickle.encode(michelangelo)

        
    return redirect('/keep/fighting')

# # ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ

#                                             STRIKE PIRATE FOR DAMAGE
#  # YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY

@app.route('/pirate/strike')
def pirate_strike ():
    jack_sparrow = jsonpickle.decode(session['pirate'])
    michelangelo = jsonpickle.decode(session['ninja'])

    michelangelo.health -= jack_sparrow.strength/(michelangelo.shield)

    if michelangelo.health <= 0:
            return redirect('/ninja/won')
    
    session['ninja'] = jsonpickle.encode(michelangelo)
    session['pirate'] = jsonpickle.encode(jack_sparrow)

    return render_template('p_strike.html', jack_sparrow=jack_sparrow, michelangelo=michelangelo)

# # ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ



@app.route('/pirate_stats')
def pirate_stats():

    jack_sparrow = jsonpickle.decode(session['pirate'])

    return render_template('/p_stats.html', jack_sparrow=jack_sparrow)