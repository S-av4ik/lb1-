from app import app, __version__


def client():
    return app.test_client()


def test_health():
    r = client().get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok", "version": __version__}
