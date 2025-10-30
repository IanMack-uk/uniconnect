// AdSense and Cookie Consent Manager
class AdSenseManager {
    constructor(config) {
        this.config = config;
        this.cookieConsentGiven = this.getCookieConsent();
        this.init();
    }

    init() {
        console.log('AdSenseManager initializing...');
        
        if (this.config.cookieConsentEnabled) {
            this.setupCookieConsent();
        }
        
        // Only show fallback ads if explicitly enabled
        if (this.config.showFallbackAds && this.config.environment === 'development') {
            console.log('Development mode: showing fallback ads immediately');
            setTimeout(() => {
                this.showAllFallbackAds();
            }, 1000);
        }
        
        if (this.cookieConsentGiven || !this.config.cookieConsentEnabled) {
            this.enableAds();
        }
    }

    setupCookieConsent() {
        const banner = document.getElementById('cookie-banner');
        const acceptBtn = document.getElementById('cookie-accept');
        const rejectBtn = document.getElementById('cookie-reject');

        if (!this.cookieConsentGiven && banner) {
            banner.style.display = 'block';
        }

        if (acceptBtn) {
            acceptBtn.addEventListener('click', () => {
                this.acceptCookies();
            });
        }

        if (rejectBtn) {
            rejectBtn.addEventListener('click', () => {
                this.rejectCookies();
            });
        }
    }

    acceptCookies() {
        this.setCookieConsent(true);
        this.hideCookieBanner();
        this.enableAds();
        
        // Reload ads if they were blocked
        this.reloadAds();
    }

    rejectCookies() {
        this.setCookieConsent(false);
        this.hideCookieBanner();
        this.disableAds();
    }

    enableAds() {
        // Enable AdSense ads
        if (window.adsbygoogle) {
            const ads = document.querySelectorAll('.adsbygoogle');
            console.log('Found', ads.length, 'ad slots');
            
            ads.forEach((ad, index) => {
                if (!ad.dataset.adsbygoogleStatus) {
                    try {
                        console.log('Loading ad slot', index + 1, 'with client:', ad.dataset.adClient);
                        (adsbygoogle = window.adsbygoogle || []).push({});
                        
                        // Add fallback for localhost/development
                        if (this.config.environment === 'development') {
                            setTimeout(() => {
                                if (!ad.innerHTML.trim() || ad.innerHTML === '') {
                                    this.showFallbackAd(ad, index + 1);
                                }
                            }, 3000);
                        }
                    } catch (e) {
                        console.log('AdSense error:', e);
                        if (this.config.environment === 'development') {
                            this.showFallbackAd(ad, index + 1);
                        }
                    }
                }
            });
        } else {
            console.log('AdSense script not loaded');
            if (this.config.environment === 'development') {
                this.showAllFallbackAds();
            }
        }
    }

    showFallbackAd(adElement, slotNumber) {
        adElement.innerHTML = `
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        color: white; 
                        padding: 20px; 
                        text-align: center; 
                        border-radius: 8px;
                        min-height: 200px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;">
                <h3 style="margin: 0 0 10px 0; font-size: 18px;">🎓 Development Ad Slot ${slotNumber}</h3>
                <p style="margin: 0 0 10px 0; opacity: 0.9;">Supporting UNI Music Scholarships</p>
                <small style="opacity: 0.7;">Real ads will appear in production</small>
            </div>
        `;
        console.log('Showing fallback ad for slot', slotNumber);
    }

    showAllFallbackAds() {
        const ads = document.querySelectorAll('.adsbygoogle');
        ads.forEach((ad, index) => {
            this.showFallbackAd(ad, index + 1);
        });
    }

    disableAds() {
        // Hide existing ads
        const ads = document.querySelectorAll('.adsbygoogle');
        ads.forEach(ad => {
            ad.style.display = 'none';
        });
    }

    reloadAds() {
        // Reload AdSense ads after consent
        const ads = document.querySelectorAll('.adsbygoogle');
        ads.forEach(ad => {
            ad.style.display = 'block';
        });
    }

    hideCookieBanner() {
        const banner = document.getElementById('cookie-banner');
        if (banner) {
            banner.style.display = 'none';
        }
    }

    getCookieConsent() {
        return localStorage.getItem('cookieConsent') === 'true';
    }

    setCookieConsent(consent) {
        localStorage.setItem('cookieConsent', consent.toString());
        this.cookieConsentGiven = consent;
    }

    // Production testing helper
    testAds() {
        if (this.config.environment === 'development') {
            console.log('=== AdSense Debug Info ===');
            console.log('Config:', this.config);
            console.log('Cookie Consent:', this.cookieConsentGiven);
            console.log('AdSense Script Loaded:', !!window.adsbygoogle);
            console.log('Ad Slots Found:', document.querySelectorAll('.adsbygoogle').length);
            
            const ads = document.querySelectorAll('.adsbygoogle');
            ads.forEach((ad, index) => {
                console.log(`Ad Slot ${index + 1}:`, {
                    client: ad.dataset.adClient,
                    slot: ad.dataset.adSlot,
                    testMode: ad.dataset.adtest,
                    hasContent: ad.innerHTML.trim() !== '',
                    status: ad.dataset.adsbygoogleStatus
                });
            });
            
            // Force show fallback ads after 2 seconds for demo
            setTimeout(() => {
                console.log('Checking for empty ads...');
                ads.forEach((ad, index) => {
                    if (!ad.innerHTML.trim() || ad.innerHTML === '') {
                        console.log(`Ad slot ${index + 1} is empty, showing fallback`);
                        this.showFallbackAd(ad, index + 1);
                    }
                });
            }, 2000);
        }
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, checking for adsenseConfig...');
    console.log('adsenseConfig:', window.adsenseConfig);
    
    if (window.adsenseConfig) {
        console.log('Creating AdSenseManager...');
        window.adsenseManager = new AdSenseManager(window.adsenseConfig);
        
        // Test in development
        if (window.adsenseConfig.environment === 'development') {
            console.log('Running ad tests...');
            window.adsenseManager.testAds();
        }
    } else {
        console.error('adsenseConfig not found!');
    }
});

// Also try immediate initialization in case DOM is already loaded
if (document.readyState === 'loading') {
    console.log('Document still loading, waiting for DOMContentLoaded...');
} else {
    console.log('Document already loaded, initializing immediately...');
    if (window.adsenseConfig) {
        window.adsenseManager = new AdSenseManager(window.adsenseConfig);
        if (window.adsenseConfig.environment === 'development') {
            window.adsenseManager.testAds();
        }
    }
}
