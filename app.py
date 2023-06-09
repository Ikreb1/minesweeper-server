from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///minesweeper.db')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Player {self.name}>'

# Wrap the `db.create_all()` call with the application context
with app.app_context():
    db.create_all()

@app.route('/players', methods=['POST'])
def add_player():
    data = request.get_json()
    name = data['name']
    score = data['score']
    new_player = Player(name=name, score=score)
    db.session.add(new_player)
    db.session.commit()
    return jsonify({'message': 'Player added', 'id': new_player.id}), 201

# GET /players?num=5 example
@app.route('/players', methods=['GET'])
def get_players():
    try:
        # Gets the number of players from the request, defaults to 10 if not provided
        num_players = request.args.get('num', default=10, type=int)
        players = Player.query.order_by(Player.score.desc()).limit(num_players).all()
        output = []
        for player in players:
            player_data = {'id': player.id, 'name': player.name, 'score': player.score}
            output.append(player_data)
        return jsonify({"players": output}), 200

    except Exception as e:
        return str(e), 400

@app.route('/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    player = Player.query.get(player_id)
    player_data = {'id': player.id, 'name': player.name, 'score': player.score}
    return jsonify({"player": player_data})

@app.route('/players/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    player = Player.query.get(player_id)
    if player is None:
        return jsonify({"message": "Player not found"}), 404
    db.session.delete(player)
    db.session.commit()
    return jsonify({"message": f"Player {player_id} deleted"}), 200


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=int(port))
