from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        resp: Response = await call_next(request)
        # Allow Google AdSense domains + self
        csp = (
            "default-src 'self'; "
            "script-src 'self' https://pagead2.googlesyndication.com https://googleads.g.doubleclick.net https://www.googletagservices.com 'unsafe-inline'; "
            "img-src 'self' https: data:; "
            "style-src 'self' 'unsafe-inline'; "
            "connect-src 'self' https://googleads.g.doubleclick.net https://pagead2.googlesyndication.com https://ep1.adtrafficquality.google; "
            "frame-src https://googleads.g.doubleclick.net https://pagead2.googlesyndication.com https://www.googletagservices.com; "
            "frame-ancestors 'none'; "
            "base-uri 'self'; "
            "form-action 'self'"
        )
        resp.headers["Content-Security-Policy"] = csp
        resp.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        resp.headers["X-Content-Type-Options"] = "nosniff"
        resp.headers["X-Frame-Options"] = "DENY"
        resp.headers["X-XSS-Protection"] = "0"
        return resp
