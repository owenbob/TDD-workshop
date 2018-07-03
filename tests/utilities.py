query_users = '''{ 
            users{
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
            '''

expected_response_query_users = {
  "data": {
    "users": {
      "edges":[ {
          "node": {
            "firstName": "jacks",
            "lastName": "dick",
            "username": "jcole",
            "email": "dkam@gmail.com",
            "password": "1234"    
          }
      }
      ]
    }
  }
}


update_user = '''
    mutation{
        updateUser(email:"dkam@gmail.com",firstName:"Jonah"){
        user{
        lastName
        username
        email
        password
        }   
    }   
    }
    '''

expected_query_after_update = {
        "data": {
        "updateUser": {
        "user": {
            "lastName": "dick",
            "username": "jcole",
            "email": "dkam@gmail.com",
            "password": "1234"
        }
        }
    }              
    }


delete_user = '''
mutation{
        deleteUser(email:"dkam@gmail.com"){
        user{
        firstName
        lastName
        username
        password
        }  
    }   
    }
            '''


expected_query_after_delete = {
        "data": {
        "deleteUser": {
            "user": {
        "firstName": "jacks",
        "lastName": "dick",
        "username":"jcole",
        "password":"1234" 
      }
     }
    }
    }



            