import os

from flask import Flask, request
from flask_caching import Cache
from werkzeug.exceptions import BadRequest


def create_app(env: str) -> Flask:
    app = Flask(__name__)
    app.config['CACHE_TYPE'] = 'simple'
    cache = Cache(app)

    @cache.memoize(timeout=5)
    def reverse_user(user: str) -> str:
        return user[::-1]

    @app.route('/test', methods=['POST'])
    def test():
        if not request.is_json:
            raise BadRequest('Invalid content type')

        try:
            body = request.get_json()
        except Exception:
            raise BadRequest('Invalid JSON format')

        if not isinstance(body, dict):
            raise BadRequest('Body is not dict')

        user = body.get('user')
        if user is None:
            raise BadRequest('Missed argument: user')

        return reverse_user(user)

    return app


if __name__ == '__main__':
    app = create_app("development")
    port = int(os.environ.get('PORT', 8080))
    app.run(host="0.0.0.0", port=port)
