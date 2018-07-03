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
        self.client = Client(schema)

        test_user =User(
            email='dkam@gmail.com',
            first_name='jacks',
            last_name='dick',
            username='jcole',
            password='1234'
            ) 
        db_session.add(test_user)
        db_session.commit()
       


    def tearDown(self):
        db_session.remove()
        Base.metadata.drop_all(bind=engine)
