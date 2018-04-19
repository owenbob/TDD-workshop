import sys
import os
sys.path.append(os.getcwd())

from graphene.test import Client
from unittest import TestCase

from models.models import User,Story,Base,engine,db_session
from schema.schema import schema



#class definitions
class BaseTestCase(TestCase): 
#Setup method
    def setUp(self):
        Base.metadata.create_all(engine)
        db_session.commit()
        self.client = Client(schema)


    def tearDown(self):
        db_session.remove()
        Base.metadata.drop_all(bind=engine)
