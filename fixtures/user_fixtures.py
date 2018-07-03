user_mutation_query = '''
    mutation {
        createUser(username: "patrick", email: "patrick.wal@gmail.com", password: "pat1234", firstName: "Patrick", lastName: "Rickson") {
            user {
            username
            email
            firstName
            lastName
        }
    }
}
'''

user_mutation_response = {
    "data": {
        "createUser": {
        "user": {
            "username": "patrick",
            "email": "patrick.wal@gmail.com",
            "firstName": "Patrick",
            "lastName": "Rickson"
        }
        }
    }
}

user_get_query = '''
    {
        users{
            edges {
            node {
                username
                email
                firstName
                lastName
            }
            }
        }
    }
'''

users_email_firstname = '''
    {
        users {
            edges {
            node {
                email
                firstName
            }
            }
        }
    }
'''

get_users_usernames = '''
 {
  users {
    edges {
      node {
            username
           }
          }
        }
  }
'''

user_get_query_response = {
    "data": {
        "users": {
        "edges": [
            {
            "node": {
                "username": "patrick",
                "email": "patrick.wal@gmail.com",
                "firstName": "Patrick",
                "lastName": "Rickson"
            }
            }
        ]
        }
    }
}

users_email_firstname_response = {
    "data": {
        "users": {
        "edges": [
            {
                "node": {
                    "email": "patrick.wal@gmail.com",
                    "firstName": "Patrick"
                }
            }
        ]
        }
    }
}

users_usernames_response = {
                                "data": {
                                    "users": {
                                    "edges": [
                                        {
                                        "node": {
                                            "username": "patrick"
                                        }
                                        },
                                        {
                                        "node": {
                                            "username": "jcole"
                                        }
                                        }
                                    ]
                                    }
                                }
                                }