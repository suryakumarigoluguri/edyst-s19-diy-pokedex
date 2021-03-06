from flask import Flask,json,render_template,jsonify

app = Flask(__name__)
@app.errorhandler(404)
def not_found(e):
   return render_template("404.html"), 404

@app.route('/api/pokemon/<int:id>')

def index(id):
    if (id>=1 and id<=151):
        a=json.load(open('pokemon_data.json'))
        pk={"pokemon":a[id-1]}    
        return json.dumps(pk)
    else:
        return render_template("404.html"), 404
        abort(404)
if __name__ == '__main__':
    app.run(host='localhost', port=8006, debug=True)
