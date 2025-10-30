from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from typing import Optional

class Settings(BaseSettings):
    model_config = ConfigDict(env_prefix="")
    
    # Google AdSense Configuration
    adsense_publisher_id: str = "ca-pub-9219208012298253"
    adsense_home_slot_id: str = "1234567890"  # Replace with real slot ID
    adsense_mentors_slot_id: str = "0987654321"  # Replace with real slot ID
    
    # Environment Configuration
    environment: str = "production"  # development, staging, production
    domain: str = "connect.vaccin8.io"  # Your deployment domain
    
    # Cookie Consent Configuration
    cookie_consent_enabled: bool = True
    
    # AdSense Testing & Fallbacks
    adsense_test_mode: bool = False  # Set to True to use test ads
    show_fallback_ads: bool = False  # Set to True to show development placeholders
    
    # Production validation
    def is_production_ready(self) -> bool:
        """Check if configuration is ready for production AdSense"""
        return (
            self.environment == "production" and
            not self.adsense_test_mode and
            self.adsense_home_slot_id not in ["1234567890", "0987654321"] and
            self.adsense_mentors_slot_id not in ["1234567890", "0987654321"]
        )

settings = Settings()
