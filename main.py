from flask import Flask, request
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)


@app.route('/abhishekk/callback')
def callback():
    # Capture request details
    log_data = {
        "method": request.method,
        "path": request.full_path,
        "headers": dict(request.headers),
        "arguments": request.args,
        "body": request.data.decode('utf-8')  # assuming the body data is utf-8 encoded
    }

    app.logger.info(f"Received request: {log_data}")

    code = request.args.get('code')
    # Here, you'd typically exchange the 'code' for an access token.
    return f"Received code: {code}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
