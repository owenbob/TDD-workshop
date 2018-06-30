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
        user {
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
        user {
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
        user {
            edges {
            node {
                username
            }
            }
        }
    }
'''

user_get_query_reponse = {
    "data": {
        "user": {
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

users_email_firstname_reponse = {
    "data": {
        "user": {
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

users_usernames_reponse = {
    "data": {
        "user": {
        "edges": [
            {
                "node": {
                    "username": "patrick"
                }
            }
        ]
        }
    }
}