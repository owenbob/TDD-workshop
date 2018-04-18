update_user = '''
    mutation{
        updateUser(email:"dkamara@gmail.com",firstName:"Jonah"){
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
            "email": "dkamara@gmail.com",
            "password": "1234"
        }
        }
    }              
    }


delete_user = '''
mutation{
        deleteUser(email:"dkamara@gmail.com"){
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



            