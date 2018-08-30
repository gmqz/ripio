
from flask_restful import Resource
from flask import jsonify, request
from flask_jwt_extended import  jwt_required,\
                                get_jwt_identity

from coinApp.main.models import User, Account
#import json
from bson.objectid import ObjectId


# Import the database object from coinApp module
from coinApp import mongo,app,errorHandler


class AccountResource(Resource):
    """
        AccountResource Resource
        POST -> new account
        GET -> retrieve a account
    """
    @jwt_required
    def post(self):

        try:
            user = User.objects.get(id = ObjectId(get_jwt_identity()))
            account = Account()
            account.user = user
            account = account.save()
            user.accounts.append(account)
            user.save()
        except Exception as e: # catch *all* exceptions
            return errorHandler(code = 400, debug = e);

        return {'status': 'Success'}, 201

    @jwt_required
    def get(self,account):
        try:
            account = Account.objects(id = ObjectId(account)).first()

            if account:
                return account.toJson()
            else:
                return errorHandler(code = 404)

        except Exception as e: # catch *all* exceptions
            return errorHandler(code = 400, debug = e)

    def put(self):
        pass
    def delete(self):
        pass

class AccountsResource(Resource):
    """
        AccountsResource Resource
        GET -> retrieve all account
    """
    @jwt_required
    def get(self):
        try:
            res = []
            for account in Account.objects:
                res.append(account.toMinJson())
            return res

        except Exception as e: # catch *all* exceptions
            return errorHandler(code = 400, debug = e)
