
from flask_restful import Resource
from flask import jsonify, request
from flask_jwt_extended import  jwt_required,\
                                get_jwt_identity

from coinApp.main.models import User, Transaction, Account
#import json
from bson.objectid import ObjectId


# Import the database object from coinApp module
from coinApp import mongo,app,errorHandler


class TransactionResource(Resource):
    """
        Transaction API
        POST -> new
        GET -> retrieve
    """
    @jwt_required
    def post(self):
        data = request.get_json()

        try:
            user = User.objects.get(id = ObjectId(get_jwt_identity()))
            data['value'] = round(float(data['value']),6)
            if data['value'] > 0:
                origin = Account.objects.get(id = ObjectId(data['origin']))
                target = Account.objects.get(id = ObjectId(data['target']))
                data['originBalance'] = origin.getBalance()

                if data['originBalance'] >= data['value']:
                    data['originBalance'] = round(data['originBalance'] - data['value'],6)
                    data['targetBalance'] = round(target.getBalance() + data['value'],6)
                    transaction = Transaction(**data)
                    transaction = transaction.save()
                    origin.transactions.append(transaction)
                    target.transactions.append(transaction)
                    origin.save()
                    target.save()
                else:
                    return errorHandler(code = 400, message = "Saldo insuficiente");
            else:
                return errorHandler(code = 400, message = "Error de precision");
        except Exception as e: # catch *all* exceptions
            return errorHandler(code = 400, debug = e);

        return {'status': 'Success', 'user': user.toJson() }, 201

    @jwt_required
    def get(self):
        try:
            user = User.objects.get(id = ObjectId(get_jwt_identity()))

            if user:
                return user.toJson()
            else:
                return errorHandler(code = 404)

        except Exception as e: # catch *all* exceptions
            return errorHandler(code = 400, debug = e)

    def put(self):
        pass
    def delete(self):
        pass
