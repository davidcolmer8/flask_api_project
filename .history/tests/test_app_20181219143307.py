import pytest 

def test_getUUID(client):
    resp=client.get("/uuid")
    