import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from app.config import settings
from app.middleware import SecurityHeadersMiddleware

app = FastAPI(title="UNI Connect (Demo)")
app.add_middleware(SecurityHeadersMiddleware)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Debug endpoint to check static files
@app.get("/debug")
def debug_info():
    import os
    return {
        "cwd": os.getcwd(),
        "static_exists": os.path.exists("app/static"),
        "css_exists": os.path.exists("app/static/styles.css"),
        "js_exists": os.path.exists("app/static/adsense-manager.js"),
        "static_files": os.listdir("app/static") if os.path.exists("app/static") else []
    }

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {
            "adsense_publisher_id": settings.adsense_publisher_id,
            "adsense_slot_id": settings.adsense_home_slot_id,
            "adsense_test_mode": settings.adsense_test_mode,
            "cookie_consent_enabled": settings.cookie_consent_enabled,
            "environment": settings.environment,
            "show_fallback_ads": settings.show_fallback_ads,
            "production_ready": settings.is_production_ready(),
        },
    )

@app.get("/mentors")
def mentors(request: Request):
    demo_mentors = [
        {"name": "Alex R.", "role": "Mix Engineer @ Studio One"},
        {"name": "Sam T.", "role": "Composer for TV"},
        {"name": "Jamie L.", "role": "Live Sound Tech @ VenueX"},
    ]
    return templates.TemplateResponse(
        request,
        "mentors.html",
        {
            "mentors": demo_mentors,
            "adsense_publisher_id": settings.adsense_publisher_id,
            "adsense_slot_id": settings.adsense_mentors_slot_id,
            "adsense_test_mode": settings.adsense_test_mode,
            "cookie_consent_enabled": settings.cookie_consent_enabled,
            "environment": settings.environment,
            "show_fallback_ads": settings.show_fallback_ads,
            "production_ready": settings.is_production_ready(),
        },
    )

@app.get("/privacy")
def privacy(request: Request):
    return templates.TemplateResponse(
        request,
        "privacy.html",
        {},
    )

@app.get("/ads.txt")
def ads_txt():
    return FileResponse("ads.txt", media_type="text/plain")

@app.get("/health")
def health_check():
    """Simple health check endpoint"""
    return {"status": "healthy", "service": "UNI Connect"}

@app.get("/adsense-status")
def adsense_status():
    """Development endpoint to check AdSense configuration"""
    return {
        "publisher_id": settings.adsense_publisher_id,
        "home_slot_id": settings.adsense_home_slot_id,
        "mentors_slot_id": settings.adsense_mentors_slot_id,
        "test_mode": settings.adsense_test_mode,
        "environment": settings.environment,
        "cookie_consent_enabled": settings.cookie_consent_enabled,
        "show_fallback_ads": settings.show_fallback_ads,
        "production_ready": settings.is_production_ready(),
        "status": "production" if settings.is_production_ready() else "development",
        "next_steps": [] if settings.is_production_ready() else [
            "Set ENVIRONMENT=production",
            "Set ADSENSE_TEST_MODE=false", 
            "Replace placeholder slot IDs with real Google AdSense slot IDs",
            "Deploy to a real domain (not localhost)"
        ]
    }

@app.get("/test-ads")
def test_ads(request: Request):
    """Simple test page to debug ad loading"""
    return templates.TemplateResponse(
        request,
        "test-ads.html",
        {
            "adsense_publisher_id": settings.adsense_publisher_id,
            "adsense_slot_id": settings.adsense_home_slot_id,
            "adsense_test_mode": settings.adsense_test_mode,
            "cookie_consent_enabled": settings.cookie_consent_enabled,
            "environment": settings.environment,
        },
    )
