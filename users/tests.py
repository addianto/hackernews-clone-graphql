from graphene_django.utils.testing import GraphQLTestCase
from hackernews.schema import schema


class UsersSchemaTest(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def test_query(self):
        response = self.query(
            '''
            query {
                users {
                    username
                    password
                    email
                }
            }
            ''',
            op_name='users'
        )

        self.assertResponseNoErrors(response)

    def test_mutation(self):
        response = self.query(
            '''
            mutation {
                createUser (
                    username: "example",
                    password: "example123",
                    email: "example@example.com"
                ) {
                    user {
                        username
                        password
                        email
                    }
                }
            }
            ''',
            op_name='createUser'
        )

        self.assertResponseNoErrors(response)
