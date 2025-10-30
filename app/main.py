from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from app.config import settings
from app.middleware import SecurityHeadersMiddleware

app = FastAPI(title="UNI Connect (Demo)")
app.add_middleware(SecurityHeadersMiddleware)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

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
    """Lightweight status endpoint"""
    from datetime import datetime
    return {
        "publisher": "ca-pub-9219208012298253",
        "npa_default": True,
        "time": datetime.utcnow().isoformat() + "Z"
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
            "show_fallback_ads": settings.show_fallback_ads,
            "production_ready": settings.is_production_ready(),
        },
    )
