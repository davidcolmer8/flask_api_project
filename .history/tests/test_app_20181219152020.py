import pytest 

def test_getUUID():
    resp=req.get("/uuid")
    assert resp.status_code == 200