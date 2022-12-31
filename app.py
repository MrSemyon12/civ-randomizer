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

    elif 'command' in keys:
        command = request.form['command']
        if command == 'Invert':
            civs.update(invertCivs(civs))
        elif command == 'Standart':
            civs.update(standartCivs())
        elif command == 'Randomize':
            players = int(request.form['players'])
            choice = int(request.form['choice'])
            result.clear()
            result.update(randomizeCivs(civs, players, choice))

    return render_template('index.html', civs=civs, result=result)


@app.route('/author')
def author():
    return render_template('author.html')


if __name__ == '__main__':
    app.run(debug=False)
