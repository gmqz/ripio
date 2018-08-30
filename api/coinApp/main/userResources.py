from flask_restful import Resource
from flask_jwt_extended import  JWTManager,\
                                jwt_required,\
                                create_access_token,\
                                get_jwt_identity,\
                                jwt_refresh_token_required
# from werkzeug.security import   generate_password_hash,\
#                                 safe_str_cmp,\
#                                 check_password_hash

from flask import jsonify, request
from coinApp.main.models import User, Account, Transaction
import json
from bson.objectid import ObjectId


# Import the database object from coinApp module
from coinApp import mongo,app,errorHandler

jwt = JWTManager(app)


class UserLogin(Resource):
    """
        UserLogin Resource
        POST -> login
    """
    def post(self):
        data = request.get_json()
        try:
            user = User.objects.get(username = data['username'])
        except Exception as e: # catch *all* exceptions
            return errorHandler(code = 400, message = "Las credenciales no son válidas!", debug = e)

        if user and user.verifyPassword(data['password']):
            ret = {'access_token': create_access_token(identity=str(user.id))}
            return ret, 200

        return errorHandler(code = 400, message = "Las credenciales no son válidas!");


class TokenRefresh(Resource):
    """
        TokenRefresh Resource
        POST -> generate new token
    """
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}


class UserResource(Resource):
    """
        UserResource Resource
        POST -> new user
        GET -> retrieve user
    """
    def post(self):
        data = request.get_json()
        initialFunds = round(float(data['funds']),6)
        del data['funds']
        try:
            user = User(**data)
            user.hashPassword(user.password)
            user.save()
            # Se crea una cuenta automaticamente con fines practicos para el testing
            # y porque no llego con el CRUD de cuentas :) sorry
            # Además se le asigna una fondo inicial para agilizar el testing
            account = Account()
            account.description = "Cuanta de prueba - " + user.username
            account.user = user
            account = account.save()

            initialTransaction = Transaction()
            initialTransaction.origin = account
            initialTransaction.target = account
            initialTransaction.originBalance = initialFunds
            initialTransaction.targetBalance = initialFunds
            initialTransaction.value = initialFunds
            initialTransaction.save()
            account.transactions.append(initialTransaction)
            account = account.save()
            
            user.accounts.append(account)
            user.save()

        except Exception as e: # catch *all* exceptions
            strError = str(e)
            message = ''
            if strError.find("username_1 dup") > -1:
                message = "El nombre de usuario ya está en uso"
            elif strError.find("email_1 dup") > -1:
                message = "El email ya está en uso"

            return errorHandler(code = 400, message = message, debug = e);

        return {'status': 'Success'}, 201

    @jwt_required
    def get(self):
        try:
            user = User.objects.get(id = ObjectId(get_jwt_identity()))
        except Exception as e: # catch *all* exceptions
            return errorHandler(code = 404, debug = e)

        return user.toJson()

    def put(self):
        pass
    def delete(self):
        pass


class Users(Resource):
    """
        Users Resource
        Solo activo a findes practicos para el testing
        GET -> retrieve all users
    """
    def get(self):
        try:
            res = []
            for user in User.objects:
                res.append(user.toJson())
            return res

        except Exception as e: # catch *all* exceptions
            return errorHandler(code = 400, debug = e)
