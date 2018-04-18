
# from schema import schema
from tests.Basetest import BaseTestCase



class QueryTest(BaseTestCase):
    def test_user_query(self):
        execute_query = self.client.execute(
            '''{ 
            user{
                edges{
                    node{
                        firstName
                        lastName
                        username
                        email
                        password
                        }
                    }
                } 
                }
            ''')
        
        assert execute_query == {
  "data": {
    "user": {
      "edges": []
    }
  }
}

                
  
