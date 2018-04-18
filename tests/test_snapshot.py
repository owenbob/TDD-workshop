from graphene.test import Client
from schema.schema import schema
from tests.utilities import expected_query_after_update

def test_update(snapshot):
    client = Client(schema)

    snapshot.assert_match(client.execute(expected_query_after_update))