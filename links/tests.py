from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase
from hackernews.schema import schema
from .models import Link


class LinkModelTest(TestCase):

    def test_create_and_save_link(self):
        first_link = Link()
        first_link.url = 'https://www.howtographql.com'
        first_link.description = 'The Fullstack Tutorial for GraphQL'
        second_link = Link()
        second_link.url = 'https://twitter.com/jonatasbaldin'
        second_link.description = 'The Jonatas Baldin Twitter'

        first_link.save()
        second_link.save()
        links = Link.objects.all()

        self.assertEqual(links.count(), 2)
        self.assertEqual(links[0].url, 'https://www.howtographql.com')
        self.assertEqual(links[1].url, 'https://twitter.com/jonatasbaldin')


class LinkGraphQLTest(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def test_smoke_test_query(self):
        response = self.query(
            '''
            query {
                links {
                    id
                    url
                    description
                }
            }
            ''',
            op_name='links'
        )

        self.assertResponseNoErrors(response)

    def test_mutation_link(self):
        response = self.query(
            '''
            mutation {
                createLink (
                    url: "https://example.com",
                    description: "An example"
                ) {
                    id
                    url
                    description
                }
            }
            ''',
            op_name='createLink'
        )

        self.assertResponseNoErrors(response)
