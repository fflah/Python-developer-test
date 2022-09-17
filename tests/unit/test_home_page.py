def test_home_page(client):
    response = client.get('/')
    print(response.data)
    assert response.status_code == 200
    assert b"Get Data From jambi.antaranews.com" in response.data
    assert b"Get Data" in response.data
    assert b"Result" in response.data