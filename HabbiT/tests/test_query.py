from unittest import TestCase, mock
from api_habbi.queries.queries import filter_query
from api_habbi.models.models import House, HouseInfo
from api_habbi.config.config import database

class TestFilterQuery(asynctest.TestCase):
    @mock.patch.object(database, 'fetch_all')
    async def test_filter_query(self, mock_fetch_all):
        items = House(name="Example Name",
                      city="Example City",
                      year=2023)

        response = HouseInfo(address="address",
                             city="city",
                             name="name",
                             description="description",
                             price=10)

        expected_response = [
            {"address": "address",
             "city": "city",
             "name": "name",
             "description": "description",
             "price": 10}
        ]

        mock_fetch_all.return_value = expected_response

        result = await filter_query(items)

        self.assertEqual(result, [response])
