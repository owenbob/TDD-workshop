from tests.Basetest import BaseTestCase
from tests.utilities import update_user, expected_query_after_update

class DeleteUser(BaseTestCase):

    def test_updateuser_mutation(self):

        execute_update_mutation = self.client.execute(update_user) 
           
        assert execute_update_mutation == expected_query_after_update