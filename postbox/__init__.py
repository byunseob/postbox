from flask import Flask, make_response, jsonify

from postbox.util.custom_json_encoder import CustomJsonEncoder


def create_app():
    app = Flask(__name__)
    app.json_encoder = CustomJsonEncoder

    from postbox.api.mail import mail_bp

    app.register_blueprint(mail_bp)

    @app.route('/health', methods=['GET'])
    def health():
        response = make_response(jsonify({'status': 'healthy'}))
        response.headers['Content-Type'] = 'application/json'
        return response

    # register_error_handler(app)

    return app
