from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__) 
CORS(app)

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if id and request.method == 'Get':
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})
   elif id and request.method == 'DELETE':
       for user in users['users_list']:
           if user['id'] == id:
               users['users_list'].pop(user)
   return users

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

def gen_id():
  return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = gen_id()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True, user = userToAdd)
      resp.status_code = 201 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp
   elif request.method == 'DELETE':
      userToDelete = request.get_json()
      for user in users['users_list']:
           if user['id'] == userToDelete['id]:
               users['users_list'].remove(user)
               resp = jsonify(success=True)
               resp.status_code = 200
               return resp
      resp = jsonify(success=False)
      
                
               

