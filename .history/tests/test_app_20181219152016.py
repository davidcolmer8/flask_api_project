import pytest 

def test_getUUID():
    resp=client.get("/uuid")
    assert resp.status_code == 200