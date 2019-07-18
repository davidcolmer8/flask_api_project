import pytest 

def test_getUUID(client):
    resp=request.get("/uuid")
    assert resp.status_code == 200