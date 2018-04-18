#imports
from graphene.test import Client
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from unittest import TestCase

from models.models import User,Story,Base,db_session
from schema.schema import schema
from app import engine


#class definitions
class BaseTestCase(TestCase): 
#Setup method
    def setUp(self):
        Base.metadata.create_all(engine)
        self.client = Client(schema)


    def tearDown(self):
        engine.dispose()
