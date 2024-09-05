from fastapi.testclient import TestClient

# def test_get_products(client: TestClient):
#     response = client.get("/produtos")
#     body = response.json()
#     assert response.status_code == 200
#     #assert body["chave"] == "valor"

def test_create_products(client: TestClient):
    response = client.get("/produtos")
    body = response.json()
    assert response.status_code == 200
    assert body = '''{
  "produto": "Celular",
  "preco": 4120
}'''