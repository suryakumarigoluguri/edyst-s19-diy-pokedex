from flask import Flask,json,render_template,jsonify

app = Flask(__name__)
@app.errorhandler(404)
@app.route('/api/pokemon/<int:id>')
def index(id):
    if (id>=1 and id<=9):
        id=str(id)
        pk={"1" :{"id" : 1,"name": "bulbasaur",
        "sprite":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"},
        "2" :{"id" : 2,"name": "ivysaur",
        "sprite":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png"},
        "3" :{"id" : 3,"name": "venusaur",
        "sprite":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png"},
        "4" :{"id" : 4,"name": "charmander",
        "sprite":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png"},
        "5" :{"id" : 5,"name": "charmeleon",
        "sprite":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/5.png"},
        "6" :{"id" : 6,"name": "charizard",
        "sprite":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png"},
        "7" :{"id" : 7,"name": "squirtle",
        "sprite":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png"},
        "8" :{"id" : 8,"name": "wartortle",
        "sprite":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/8.png"},
        "9" :{"id" : 9,"name": "blastoise",
        "sprite":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png"}}
        return json.dumps(pk[id])
    else:
        return jsonify({"you sent":request.get_json()}),200
if __name__ == '__main__':
    app.run(host='localhost', port=8006, debug=True)