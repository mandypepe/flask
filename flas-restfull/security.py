from werkzeug.security import  safe_str_cmp
from user import User
users = [
   User(1,'mandy','asdf')
]

username_mapping = {u.username: u for u in users }

#     {
#     'mandy': {
#         'id': 1,
#         'user': 'mandy',
#         'password': 'asdf'
#     }
# }

userid_mapping = {u.id: u for u in users}

###
# 1: {
#     'id': 1,
#     'user': 'mandy',
#     'password': 'asdf'}
# }
# ###
#



def authenticate(username, password):
    user = username_mapping.get(username, None)
    #if user and user.password == password:
    if user and safe_str_cmp(user.password,password):

        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
