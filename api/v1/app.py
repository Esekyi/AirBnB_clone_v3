from flask import Flask, Blueprints
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """
    This function will be called after each request
    to close the database connection.
    
    Args:
        exception: An optional exception object if one occurred.
    """
    storage.close()


if __name__ == "__main__":
    host = os.getenc("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=port, threaded=True)
