from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        resp: Response = await call_next(request)
        # Allow Google AdSense domains & inline styles required by Google
        csp = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' "
                "https://pagead2.googlesyndication.com "
                "https://googleads.g.doubleclick.net "
                "https://www.googletagservices.com "
                "https://fundingchoicesmessages.google.com; "
            "style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data: "
                "https://pagead2.googlesyndication.com "
                "https://tpc.googlesyndication.com "
                "https://googleads.g.doubleclick.net; "
            "connect-src 'self' "
                "https://pagead2.googlesyndication.com "
                "https://googleads.g.doubleclick.net "
                "https://fundingchoicesmessages.google.com; "
            "frame-src "
                "https://googleads.g.doubleclick.net "
                "https://tpc.googlesyndication.com "
                "https://www.google.com "
                "https://google.com "
                "https://fundingchoicesmessages.google.com; "
            "frame-ancestors 'none'; "
            "base-uri 'self'; "
            "form-action 'self'; "
            "upgrade-insecure-requests"
        )
        resp.headers["Content-Security-Policy"] = csp
        resp.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        resp.headers["X-Content-Type-Options"] = "nosniff"
        resp.headers["X-Frame-Options"] = "DENY"
        resp.headers["X-XSS-Protection"] = "0"
        return resp
