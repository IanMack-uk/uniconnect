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
        {
            "name": "Alexandra Rodriguez", 
            "role": "Senior Mix Engineer @ Abbey Road Studios",
            "graduation": "Music Technology '15",
            "expertise": "Audio Production, Mixing, Mastering",
            "bio": "Demo profile: Grammy-nominated engineer showcasing how mentorship platforms could connect students with industry professionals in audio production."
        },
        {
            "name": "Samuel Thompson", 
            "role": "Composer & Music Director",
            "graduation": "Music Composition '12", 
            "expertise": "Film Scoring, TV Music, Orchestration",
            "bio": "Demo profile: Emmy-winning composer example showing how platforms could facilitate connections between students and media scoring professionals."
        },
        {
            "name": "Jamie Liu", 
            "role": "Live Sound Engineer & Tour Manager",
            "graduation": "Music Business '18",
            "expertise": "Live Sound, Tour Production, Artist Management", 
            "bio": "Demo profile: Live music industry professional example demonstrating how mentorship platforms could provide career insights and networking opportunities."
        },
        {
            "name": "Dr. Maria Santos", 
            "role": "Music Education Director",
            "graduation": "Music Education '08",
            "expertise": "K-12 Music Education, Curriculum Development",
            "bio": "Demo profile: Music educator example showing how platforms could connect students interested in teaching careers with experienced professionals."
        },
        {
            "name": "David Chen", 
            "role": "Music Business Executive",
            "graduation": "Music Business '10",
            "expertise": "Artist Development, Music Marketing, Digital Strategy",
            "bio": "Demo profile: Music industry executive example illustrating how platforms could provide business mentorship and industry insights to students."
        },
        {
            "name": "Rebecca Johnson", 
            "role": "Professional Violinist & Educator", 
            "graduation": "Performance '14",
            "expertise": "Classical Performance, Chamber Music, Private Teaching",
            "bio": "Demo profile: Classical performer example demonstrating how mentorship platforms could support performance majors with audition preparation and career development."
        }
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

@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse(request, "about.html")

@app.get("/privacy")
def privacy(request: Request):
    return templates.TemplateResponse(request, "privacy.html")

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
