from flask import Flask,json,render_template,jsonify

app = Flask(__name__)

@app.route('/api/pokemon/<int:id>')

def index(id):
    if (id>=1 and id<152):
        pk=json.load(open('pokemon_data.json'))
        return json.dumps(pk[id-1])
    else:
        return ("The request can't be handled")
if __name__ == '__main__':
    app.run(host='localhost', port=8006, debug=True)
