
import datetime
from coinApp import Document,\
                    StringField,\
                    EmailField,\
                    ReferenceField,\
                    ListField,\
                    DateTimeField,\
                    FloatField,\
                    DecimalField,\
                    mongo

from werkzeug.security import   generate_password_hash,\
                                check_password_hash

import json


class User(Document):
    #_id         = StringField(primary_key=True)
    username    = StringField(unique=True,required=True)
    firstname   = StringField(required=True)
    lastname    = StringField(required=True)
    email       = EmailField(unique=True,required=True)
    password    = StringField(required=True)
    accounts    = ListField(ReferenceField('Account'))
    createdAt   = DateTimeField(default=datetime.datetime.utcnow,required=True)


    def toJson(self):
        return dict(
            id          = str(self.id),
            username    = self.username,
            firstname   = self.firstname,
            lastname    = self.lastname,
            email       = self.email,
            createdAt   = self.createdAt.strftime("%d/%m/%Y"),
            accounts    = self.getAccounts()
        )

    def getAccounts(self):
        res = []
        for account in self.accounts:
            res.append(account.toJson())
        return res

    def hashPassword(self, password):
        self.password = generate_password_hash(password)

    def verifyPassword(self, password):
        return check_password_hash(self.password, password)

class Account(Document):
    #_id         = StringField(primary_key=True)
    description = StringField(required=True)
    transactions= ListField(ReferenceField('Transaction'))
    user        = ReferenceField('User', reverse_delete_rule=mongo.DENY)
    createdAt   = DateTimeField(default=datetime.datetime.utcnow,required=True)

    def getTransactions(self):
        res = []
        for transaction in self.transactions:
            res.append(transaction.toJson())

        return res

    def toJson(self):
        return dict(
            id          = str(self.id),
            createdAt   = self.createdAt.strftime("%d/%m/%Y"),
            transactions= self.getTransactions(),
            balance     = self.getBalance(),
            description = self.description
        )

    def toMinJson(self):
        return dict(
            id          = str(self.id),
            description = self.description
        )

    def getBalance(self):
        if len(self.transactions) > 0:
            return self.transactions[-1].getMyBalance(self)

        return 0


class Transaction(Document):
    #_id        = StringField(primary_key=True)
    origin          = ReferenceField(   'Account',\
                                        reverse_delete_rule=mongo.DENY,\
                                        required=True)
    originBalance   = FloatField(required=True, min = 0)
    target          = ReferenceField(   'Account',\
                                        reverse_delete_rule=mongo.DENY,\
                                        required=True)
    targetBalance   = FloatField(required=True, min = 0)
    value           = FloatField(required=True, min = 0)
    description     = StringField()
    createdAt       = DateTimeField(default=datetime.datetime.utcnow,required=True)

    def toJson(self):
        return dict(
            id              = str(self.id),
            createdAt       = self.createdAt.strftime("%d/%m/%Y %H:%M:%S"),
            origin          = self.origin.toMinJson(),
            target          = self.target.toMinJson(),
            originBalance   = self.originBalance,
            targetBalance   = self.targetBalance,
            value           = self.value
        )

    def getMyBalance(self, account):
        if self.origin == account:
            return self.originBalance

        return self.targetBalance
