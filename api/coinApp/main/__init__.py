# Main __init__
from coinApp.main.models import *
from coinApp.main.userResources import *
from coinApp.main.accountResources import *
from coinApp.main.transactionResources import *
from coinApp import api


api.add_resource(UserLogin, '/auth/obtain')
api.add_resource(TokenRefresh, '/auth/refresh')
api.add_resource(Users, '/users')
api.add_resource(UserResource, '/user')

api.add_resource(AccountResource, '/account/<string:account>')
api.add_resource(AccountsResource, '/accounts')
api.add_resource(TransactionResource, '/transaction')
