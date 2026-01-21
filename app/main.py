from flask import Flask, jsonify
from .database import is_url_malicious

app = Flask(__name__)


@app.route(
    "/urlinfo/1/<hostname_and_port>/<path:original_path_and_query>", methods=["GET"]
)
def url_lookup(hostname_and_port, original_path_and_query):
    # 1. Ask our database if the URL is bad
    is_bad = is_url_malicious(hostname_and_port, original_path_and_query)

    # 2. Prepare the response
    # We provide a boolean 'is_safe' and a clear string 'action'
    response = {
        "url_checked": f"{hostname_and_port}/{original_path_and_query}",
        "is_safe": not is_bad,
        "action": "BLOCK" if is_bad else "ALLOW",
    }

    # 3. Return as JSON with HTTP 200 (OK)
    return jsonify(response), 200


if __name__ == "__main__":
    # Run the server on port 5000
    app.run(host="0.0.0.0", port=5000)
