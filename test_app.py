from app import app, __version__


def client():
    return app.test_client()


def test_health():
    r = client().get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok", "version": __version__}


def test_create_and_get():
    c = client()
    r = c.post("/tasks", json={"title": "Learn Git"})
    assert r.status_code == 201
    tid = r.get_json()["id"]
    assert c.get(f"/tasks/{tid}").get_json()["title"] == "Learn Git"


def test_create_empty_title():
    assert client().post("/tasks", json={"title": ""}).status_code == 400


def test_update_and_delete():
    c = client()
    tid = c.post("/tasks", json={"title": "x"}).get_json()["id"]
    assert c.put(f"/tasks/{tid}", json={"done": True}).get_json()["done"] is True
    assert c.delete(f"/tasks/{tid}").status_code == 204
    assert c.delete(f"/tasks/{tid}").status_code == 404


def test_not_found():
    assert client().get("/tasks/9999").status_code == 404
