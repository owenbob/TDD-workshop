import sys
import os
sys.path.append(os.getcwd())

from tests.Basetest import BaseTestCase
from models.models import db_session, User
from fixtures.user_fixtures import (
    user_mutation_query, 
    user_mutation_response,
)


class TestUser(BaseTestCase):

    def test_create_user(self):
        execute_query = self.client.execute(
            user_mutation_query,
            context_value={'session': db_session})
        
        expected_responese = user_mutation_response
        self.assertEqual(execute_query, expected_responese)
