from app import app

def test_home():
    response.test_client().get("/")

    assert response.ststus_code=200
    assert response.data== b"HELLO WORLD!"
