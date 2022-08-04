from flask import Flask, render_template, url_for, request, redirect
from randomizer import initializeCivs, invertCivs, standartCivs, randomizeCivs

app = Flask(__name__)

civs = initializeCivs()
picked = civs
result = {}

@app.route('/', methods=['POST', 'GET'])
def index():
    keys = request.form.keys()

    if 'civ' in keys:
        civName = request.form['civ']
        civs[civName] = not civs[civName]
          
    else:
        command = request.form['command']
        if command == 'Invert':
            civs.update(invertCivs(civs))
        elif command == 'Standart':
            civs.update(standartCivs())
        elif command == 'Randomize':
            players = request.form['players']
            choice = request.form['choice']
            result.update(randomizeCivs(civs, players, choice))

    return render_template('index.html', civs=civs, result=result)


if __name__ == '__main__':
    app.run(debug=True)
