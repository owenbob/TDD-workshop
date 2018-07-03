
from tests.Basetest import BaseTestCase
from tests.utilities import delete_user, expected_query_after_delete

class DeleteUser(BaseTestCase):

    def test_deleteuser_mutation(self):

        execute_delete_mutation = self.client.execute(delete_user)
            
        assert execute_delete_mutation == expected_query_after_delete