from config import env
 
 
 
class CorsMiddleware:
    """Middleware WSGI que agrega headers CORS y de seguridad."""
 
    def __init__(self, app):
        self.app = app
 
    def __call__(self, environ, start_response):
        method = environ.get('REQUEST_METHOD', 'GET')
 
        cors_headers = [
            ('Access-Control-Allow-Origin', env.CORS_ORIGIN),
            ('Vary', 'Origin'),
            ('Access-Control-Allow-Credentials', 'true'),
            ('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE, OPTIONS'),
            ('Access-Control-Allow-Headers', 'Content-Type, Authorization'),
            # Security headers básicos
            ('X-Content-Type-Options', 'nosniff'),
            ('X-Frame-Options', 'DENY'),
            ('Referrer-Policy', 'no-referrer'),
        ]
 
        # Preflight: responder 204 sin pasar a la app
        if method == 'OPTIONS':
            start_response('204 No Content', cors_headers)
            return [b'']
 
        def custom_start_response(status, headers, exc_info=None):
            headers.extend(cors_headers)
            return start_response(status, headers, exc_info)
 
        return self.app(environ, custom_start_response)
 
 
# ============================================================
# Versión 2: Django middleware
# ============================================================
 
class DjangoCorsMiddleware:
    """Middleware Django equivalente."""
 
    def __init__(self, get_response):
        self.get_response = get_response
 
    def __call__(self, request):
        # Preflight
        if request.method == 'OPTIONS':
            from django.http import HttpResponse
            response = HttpResponse(status=204)
            self._set_headers(response)
            return response
 
        response = self.get_response(request)
        self._set_headers(response)
        return response
 
    @staticmethod
    def _set_headers(response):
        response['Access-Control-Allow-Origin'] = env.CORS_ORIGIN
        response['Vary'] = 'Origin'
        response['Access-Control-Allow-Credentials'] = 'true'
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        # Security headers básicos
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['Referrer-Policy'] = 'no-referrer'
 
