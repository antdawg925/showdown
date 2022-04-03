import json
import random
from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.m_pirate import Pirate
from flask_app.models.m_ninja import Ninja
import jsonpickle


@app.route('/')
def the_game():
    michelangelo = Ninja("Michelangelo" ,100,8,85)
    jack_sparrow = Pirate("Jack Sparrow",100,8,85)

    session['ninja'] = jsonpickle.encode(michelangelo)
    session['pirate'] = jsonpickle.encode(jack_sparrow)

    return render_template('page.html' , jack_sparrow=jack_sparrow, michelangelo=michelangelo)



# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#                                                 START THE BATTLE 
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@app.route('/run/game')
def run_game():
#     # session variable 'has started' to say whether game is started or not yet

    coin = random.randint(0,1)
    print(coin)
    if(coin == 0):
        # print(phrases['Jack'][random.randint(1,4)])
        return redirect('/pirate/bonus')

    if ( coin == 1 ):
        # print(phrases['Michelangelo'][random.randint(1,4)])
        return redirect('/ninja/bonus')



# ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ


#                                                       INITIATES FOLLOW-UP ATTACKS
# YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY

@app.route('/keep/fighting')
def keep_fighting():
    coin = random.randint(0,1)
    print(coin)
    if(coin == 1):
        # print(phrases['Jack'][random.randint(1,4)])
        return redirect ('/pirate/strike')

    if(coin == 0):
        # print(phrases['Michelangelo'][random.randint(1,4)])
        return redirect('/ninja/strike')
            


# # ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ


#                                         !!!!!!!!!!!!!!!!! ANNOUNCE THE WINNER !!!!!!!!!!!!!!!!  
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

@app.route('/ninja/won')
def ninja_won():
    print('The Ninja Won!!')
    # session['winner'] = 'The Ninja Won'
    # redirect to a ninja won page!!
    return render_template('ninja_won.html')

@app.route('/pirate/won')
def pirate_won():
    print('The Pirate Won!!')
    # return to a pirate won page!
    return render_template('pirate_won.html')

# ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
            
 

