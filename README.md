# UNI Connect — FastAPI + Google AdSense

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Copy and configure environment variables
cp .env.example .env
# Edit .env with your real AdSense slot IDs

uvicorn app.main:app --reload
```

Open http://localhost:8000

## Configuration

### Environment Variables
```bash
# Google AdSense Configuration
ADSENSE_PUBLISHER_ID=ca-pub-9219208012298253  # Your publisher ID
ADSENSE_HOME_SLOT_ID=1234567890              # Replace with real slot ID
ADSENSE_MENTORS_SLOT_ID=0987654321           # Replace with real slot ID

# Environment
ENVIRONMENT=development                       # development, staging, production

# Cookie Consent
COOKIE_CONSENT_ENABLED=true                   # Enable interactive cookie consent

# Testing
ADSENSE_TEST_MODE=false                       # Set to true for test ads
```

### Production Setup
1. **Get Real Ad Slot IDs**: Create ad units in Google AdSense console
2. **Update Environment**: Set `ENVIRONMENT=production` and `ADSENSE_TEST_MODE=false`
3. **Configure Slots**: Replace placeholder slot IDs with real ones from Google
4. **Test Ads**: Use `/adsense-status` endpoint to verify configuration

## Features
- **Dynamic Ad Configuration**: Environment-based ad slot management
- **Interactive Cookie Consent**: GDPR-compliant consent with accept/reject options
- **Test Mode Support**: Use `data-adtest="on"` for development testing
- **Production Ready**: Environment detection and proper ad loading
- **Scholarship Focus**: All ad revenue directed to UNI Music Scholarships

## API Endpoints
- `/` - Home page with sidebar ad
- `/mentors` - Mentors page with inline ad  
- `/privacy` - Privacy policy and AdSense disclosure
- `/ads.txt` - Google AdSense verification file
- `/adsense-status` - Development endpoint for configuration check

## Testing
```bash
# Check AdSense configuration
curl http://localhost:8000/adsense-status

# Verify ads.txt
curl http://localhost:8000/ads.txt

# Run tests
pytest -q
```
