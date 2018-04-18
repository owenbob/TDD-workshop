import sys
import os
sys.path.append(os.getcwd())

from tests.Basetest import BaseTestCase
from models.models import db_session, User
from fixtures.user_fixtures import (
    user_mutation_query, user_mutation_response,
    user_get_query, user_get_query_reponse,
    users_email_firstname, users_email_firstname_reponse,
    get_users_usernames, users_usernames_reponse
)


class TestUser(BaseTestCase):

    def test_create_user(self):
        execute_query = self.client.execute(
            user_mutation_query,
            context_value={'session': db_session})
        
        expected_responese = user_mutation_response
        self.assertEqual(execute_query, expected_responese)
    
    def test_query_user(self):
        user = User(
            username="patrick",
            email="patrick.wal@gmail.com",
            password="pato1234",
            first_name="Patrick",
            last_name="Rickson"
        )
        db_session.add(user)
        db_session.commit()

        execute_query = self.client.execute(
            user_get_query, context_value={'session': db_session})
        response = user_get_query_reponse
        self.assertEqual(execute_query, response)
    
    def test_query_users_usernames(self):
        user = User(
            username="patrick",
            email="patrick.wal@gmail.com",
            password="pato1234",
            first_name="Patrick",
            last_name="Rickson"
        )
        db_session.add(user)
        db_session.commit()

        execute_query = self.client.execute(
            get_users_usernames, context_value={'session': db_session})
        response = users_usernames_reponse
        self.assertEqual(execute_query, response)
    
    def test_query_users_email_firstname(self):
        user = User(
            username="patrick",
            email="patrick.wal@gmail.com",
            password="pato1234",
            first_name="Patrick",
            last_name="Rickson"
        )
        db_session.add(user)
        db_session.commit()

        execute_query = self.client.execute(
            users_email_firstname, context_value={'session': db_session})
        response = users_email_firstname_reponse
        self.assertEqual(execute_query, response)
