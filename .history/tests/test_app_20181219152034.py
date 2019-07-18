import pytest 
import requests

def test_getUUID():
    resp=request.get("/uuid")
    assert resp.status_code == 200