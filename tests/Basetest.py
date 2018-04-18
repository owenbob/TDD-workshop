#imports
from graphene.test import Client
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from unittest import TestCase

from models import User,Story,Base,engine,db_session
from schema import schema



#class definitions
class BaseTestCase(TestCase): 
#Setup method
    def setUp(self):
        # self.test_engine = create_engine("sqlite:///test_db.sqlite")
        self.connection = self.test_engine.connect()
        self.transaction = self.connection.begin()
        Base.metadata.create_all(self.test_engine)
        self.client = Client(schema)


    def tearDown(self):
        self.transaction.rollback()
        self.connection.close()
        self.test_engine.dispose()
