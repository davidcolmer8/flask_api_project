import pytest 
import factor

def test_getUUID(client):
    resp=client.get("/uuid")
    assert resp.status_code == 200