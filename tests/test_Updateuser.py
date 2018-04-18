from graphene.test import Client
from schema import schema



def test_updateuser_mutation():
    client = Client(schema)
    execute_update_mutation = client.execute(
        '''mutation{
     updateUsername(email:"dkamara@gmail.com",firstName:"jacks",lastName:"dick"){
    user{
      firstName
      lastName
      username
      email
      password
    }
    
  }   
}
        ''')
        
    assert execute_update_mutation == {
    "data": {
    "updateUsername": {
      "user": {
        "firstName": "jacks",
        "lastName": "dick",
        "username": "dkamara",
        "email": "dkamara@gmail.com",
        "password": "123455"
      }
    }
  }
}
                
  
