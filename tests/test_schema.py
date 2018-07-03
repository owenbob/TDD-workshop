from tests.Basetest import BaseTestCase
from tests.utilities import (
    query_users,
    expected_response_query_users
)


class QueryTest(BaseTestCase):
    def test_user_query(self):
        execute_query = self.client.execute(query_users)
        assert execute_query == expected_response_query_users

                
  
