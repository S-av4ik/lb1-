from app import app


def client():
    return app.test_client()
