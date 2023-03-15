from flask import Flask, render_template, request, redirect, url_for
from functions import type_matchup, get_pokemon, get_pokemon_fun_fact

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/matchup', methods=['POST'])
def matchup():
    pokemon1 = request.form['pokemon1'].lower()
    pokemon2 = request.form['pokemon2'].lower()

    pokemon1_info = get_pokemon(pokemon1)
    pokemon2_info = get_pokemon(pokemon2)

    if pokemon1_info is None or pokemon2_info is None:
        error_message = 'One or more of the entered Pokemon does not exist.'
        return render_template('index.html', error_message=error_message)

    matchup_result, pokemon1_sprite, pokemon2_sprite = type_matchup(pokemon1, pokemon2)
    fun_fact = get_pokemon_fun_fact(pokemon1)
    return render_template('matchup.html', pokemon1=pokemon1.capitalize(),
                           pokemon2=pokemon2.capitalize(), matchup_result=matchup_result,
                           pokemon1_sprite=pokemon1_sprite, pokemon2_sprite=pokemon2_sprite,
                           fun_fact=fun_fact)

@app.route('/try_again')
def try_again():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
