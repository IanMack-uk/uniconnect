# UNI Connect — FastAPI + Google AdSense

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

uvicorn app.main:app --reload
```

Open http://localhost:8000

## AdSense Configuration

### Publisher Details
- **Publisher ID**: ca-pub-9219208012298253
- **Dev uses**: data-adtest="on" (automatically applied on localhost)
- **ads.txt**: Must be served from domain root when deployed
- **Revenue**: All net ad revenue → UNI Music Scholarships (beta)

### NPA/PA Behavior
- **Default**: Non-Personalised Ads (NPA) until user consent
- **After consent**: Personalised Ads (PA) with cookie-based targeting
- **Cookie banner**: Toggles NPA→PA without page reload

### Production Setup
1. **Deploy to production domain**
2. **Replace placeholder slot IDs** (1234567890, 0987654321) with real Google AdSense slot IDs
3. **Verify /ads.txt** is accessible at domain root
4. **Submit for AdSense review**

## Features
- **Advanced Fallback System**: Shows branded scholarship ads when AdSense unavailable
- **GDPR-Compliant**: NPA default, consent-aware PA switching
- **Environment Detection**: Auto-applies data-adtest="on" for localhost
- **CSP Optimized**: Allows all required AdSense domains
- **Scholarship Focus**: All net ad revenue → UNI Music Scholarships

## API Endpoints
- `/` - Home page with sidebar ad
- `/mentors` - Mentors page with inline ad  
- `/privacy` - Privacy policy and AdSense disclosure
- `/ads.txt` - Google AdSense verification file
- `/adsense-status` - Lightweight status endpoint

## Testing
```bash
# Check AdSense configuration
curl http://localhost:8000/adsense-status

# Verify ads.txt
curl http://localhost:8000/ads.txt

# Run tests
pytest -q
```
