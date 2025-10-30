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
            "graduation": "UNI Music Technology '15",
            "expertise": "Audio Production, Mixing, Mastering",
            "bio": "Grammy-nominated engineer who has worked with major artists including Taylor Swift and Ed Sheeran. Passionate about mentoring the next generation of audio professionals."
        },
        {
            "name": "Samuel Thompson", 
            "role": "Composer & Music Director",
            "graduation": "UNI Music Composition '12", 
            "expertise": "Film Scoring, TV Music, Orchestration",
            "bio": "Emmy-winning composer for Netflix originals and HBO series. Specializes in helping students transition from academic composition to professional media scoring."
        },
        {
            "name": "Jamie Liu", 
            "role": "Live Sound Engineer & Tour Manager",
            "graduation": "UNI Music Business '18",
            "expertise": "Live Sound, Tour Production, Artist Management", 
            "bio": "Currently touring with major acts including Billie Eilish and The Weeknd. Offers insights into the live music industry and career development strategies."
        },
        {
            "name": "Dr. Maria Santos", 
            "role": "Music Education Director",
            "graduation": "UNI Music Education '08",
            "expertise": "K-12 Music Education, Curriculum Development",
            "bio": "Award-winning music educator who built one of Iowa's top high school music programs. Mentors students interested in music education careers."
        },
        {
            "name": "David Chen", 
            "role": "Music Business Executive",
            "graduation": "UNI Music Business '10",
            "expertise": "Artist Development, Music Marketing, Digital Strategy",
            "bio": "VP of A&R at Universal Music Group. Helps students understand the modern music industry landscape and develop business acumen."
        },
        {
            "name": "Rebecca Johnson", 
            "role": "Professional Violinist & Educator", 
            "graduation": "UNI Performance '14",
            "expertise": "Classical Performance, Chamber Music, Private Teaching",
            "bio": "Principal violinist with the Chicago Symphony Orchestra. Mentors performance majors on audition preparation and professional development."
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
