from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Address:
    def __init__(self,data):
        self.id = data['id']

        self.address = data['address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM addresses;"
        results = connectToMySQL('emails').query_db(query)

        addresses = []
        for row in results:
            addresses.append(cls(row))
        return addresses

    @classmethod
    def save(cls,data):
        query = "INSERT INTO addresses (address, created_at, updated_at) VALUES (%(address)s, NOW(),NOW())"
        results = connectToMySQL('emails').query_db(query,data)
        return results
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM addresses WHERE id = %(id)s;"
        return connectToMySQL('emails').query_db(query,data)

    @staticmethod
    def validate_address(address):
        is_valid = True
        if not EMAIL_REGEX.match(address['address']):
            flash('Invalid Email Address!')
            is_valid = False
        return is_valid