import pytest 
import factory
from pytest_factoryboy import register

def test_getUUID(client):
    resp=client.get("/uuid")
    assert resp.status_code == 200