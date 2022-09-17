from app.helper import helper
from unittest import TestCase

def test_scrape(client):
    response = helper.Scrape()
    assert response['status'] == True