import os
import logging
from flask import Flask, jsonify
from .database import is_url_malicious

# Initialize Flask App
app = Flask(__name__)

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint for monitoring (Kubernetes/Liveness)."""
    return jsonify({"status": "healthy"}), 200


# Define routes to handle requests with or without a path.
@app.route(
    "/urlinfo/1/<hostname_and_port>",
    defaults={"original_path_and_query": ""},
    methods=["GET"],
)
@app.route(
    "/urlinfo/1/<hostname_and_port>/<path:original_path_and_query>", methods=["GET"]
)
def url_lookup(hostname_and_port: str, original_path_and_query: str):
    """
    Main endpoint to verify if a URL is safe.
    """
    try:
        is_bad = is_url_malicious(hostname_and_port, original_path_and_query)

        # Build the checked URL string for the response
        checked_url = f"{hostname_and_port}/{original_path_and_query}"
        checked_url = checked_url.strip("/")

        response = {
            "url_checked": checked_url,
            "is_safe": not is_bad,
            "action": "BLOCK" if is_bad else "ALLOW",
        }

        logger.info(f"Check: {checked_url} - Result: {response['action']}")
        return jsonify(response), 200

    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": "Internal Error", "msg": str(e)}), 500


if __name__ == "__main__":
    # Support for dynamic port assignment (Common in Docker environments)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
