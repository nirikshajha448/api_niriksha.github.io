from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path = "")
auth = HTTPBasicAuth()

users = [
    {
        'id': 1,
        'name': u'Astha',
        'experience': u'3 yrs.',  
    },
    {
        'id': 2,
        'name': u'Aditya',
        'experience': u'4 yrs.', 
    },
    {
        'id': 3,
        'name': u'Divya',
        'experience': u'2 yrs.', 
    },
    {
        'id': 4,
        'name': u'Deepak',
        'experience': u'4 yrs.', 
    },
    {
        'id': 5,
        'name': u'Gaurav',
        'experience': u'3 yrs.', 
    },
    {
        'id': 6,
        'name': u'Ishita',
        'experience': u'5 yrs.', 
    },
    {
        'id': 7,
        'name': u'Joy',
        'experience': u'3 yrs.', 
    },
    {
        'id': 8,
        'name': u'Karan',
        'experience': u'5 yrs.', 
    },
    {
        'id': 9,
        'name': u'Maya',
        'experience': u'2 yrs.', 
    },
    {
        'id': 10,
        'name': u'Shradha',
        'experience': u'3 yrs.', 
    }
]
# GET-METHOD

@app.route('/users', methods=['GET'])
def get_tasks():
    return jsonify({'users': users})
#curl -i http://localhost:5000/users

if __name__ == '__main__':
    app.run(debug=True)

# POST-METHOD



@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or not 'name' in request.json:
        abort(400)
    task = {
        'id': users[-1]['id'] + 1,
        'name': request.json['name'],
        'experience': request.json.get('experience', "")
    }
users.append(user)
    return jsonify({'user': user}), 201

# PUT-METHOD

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != unicode:
        abort(400)
    if 'experience' in request.json and type(request.json['experience']) is not unicode:
        abort(400)
    user[0]['name'] = request.json.get('name', user[0]['name'])
    user[0]['experience'] = request.json.get('experience', user[0]['experience'])
    return jsonify({'user': user[0]})

    #DELETE-METHOD


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_task(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    users.remove(user[0])
    return jsonify({'result': True})

    # AUTHORIZATION

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog
    
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)