from api.v1.views import app_views
import jsonify

@app_views.route("/status", methods=['GET'])
def index():
	return jsonify({"status": "OK"})
