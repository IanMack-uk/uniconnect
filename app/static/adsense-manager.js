// AdSense and Cookie Consent Manager
class AdSenseManager {
    constructor(config) {
        this.config = config;
        this.cookieConsentGiven = this.getCookieConsent();
        this.init();
    }
    
    getCookieConsent() {
        return localStorage.getItem('uni_cookie_ads') === 'accept';
    }

    init() {
        console.log('AdSenseManager initializing...');
        
        if (this.config.cookieConsentEnabled) {
            this.setupCookieConsent();
        }
        
        // Show fallback ads if enabled (works in all environments now)
        if (this.config.showFallbackAds) {
            console.log('Fallback ads enabled - will show if AdSense fails');
            this.setupFallbackDetection();
            
            // Force show fallbacks after a short delay if we're not in production
            if (!this.config.productionReady) {
                console.log('Not production ready - will force show fallbacks');
                setTimeout(() => {
                    console.log('Forcing fallback ads due to non-production environment');
                    this.showAllFallbackAds();
                }, 2000);
            }
        }
        
        if (this.cookieConsentGiven || !this.config.cookieConsentEnabled) {
            this.enableAds();
        }
    }

    setupCookieConsent() {
        // The new cookie banner is handled inline in base.html
        // This method is kept for compatibility but the banner logic is now in the template
        console.log('Cookie consent setup - handled by inline script in base.html');
        
        // Listen for consent changes to update ad behavior
        this.monitorConsentChanges();
    }
    
    monitorConsentChanges() {
        // Check for consent changes periodically
        setInterval(() => {
            const currentConsent = this.getCookieConsent();
            if (currentConsent !== this.cookieConsentGiven) {
                this.cookieConsentGiven = currentConsent;
                console.log('Consent changed to:', currentConsent);
                if (currentConsent) {
                    this.enableAds();
                }
            }
        }, 1000);
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
        console.log('enableAds() called, showFallbackAds:', this.config.showFallbackAds);
        
        if (window.adsbygoogle) {
            const ads = document.querySelectorAll('.adsbygoogle');
            console.log('Found', ads.length, 'ad slots');
            
            if (ads.length === 0) {
                console.log('No ad slots found! Make sure .adsbygoogle elements exist in DOM');
                return;
            }
            
            ads.forEach((ad, index) => {
                console.log(`Processing ad slot ${index + 1}:`, ad);
                // Check if already processed by AdSense or our fallback system
                if (!ad.dataset.adsbygoogleStatus && !ad.dataset.fallbackAd && !ad.dataset.adsenseProcessed) {
                    try {
                        console.log('Loading ad slot', index + 1, 'with client:', ad.dataset.adClient);
                        
                        // Mark as being processed to prevent duplicate calls
                        ad.dataset.adsenseProcessed = 'true';
                        
                        (adsbygoogle = window.adsbygoogle || []).push({});
                        
                        // Add fallback detection for all environments if enabled
                        if (this.config.showFallbackAds) {
                            console.log(`Scheduling fallback check for ad slot ${index + 1}`);
                            this.scheduleAdCheck(ad, index + 1);
                        }
                    } catch (e) {
                        console.log('AdSense error:', e);
                        if (this.config.showFallbackAds) {
                            console.log(`Showing immediate fallback for ad slot ${index + 1} due to error`);
                            this.showFallbackAd(ad, index + 1);
                        }
                    }
                } else {
                    console.log(`Ad slot ${index + 1} already processed or has fallback`);
                }
            });
        } else {
            console.log('AdSense script not loaded');
            if (this.config.showFallbackAds) {
                console.log('Showing fallback ads because AdSense script failed to load');
                this.showAllFallbackAds();
            }
        }
    }

    getFallbackAdDesigns() {
        return [
            {
                background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                title: '🎓 Support Music Education',
                subtitle: 'Help fund UNI Music Scholarships',
                note: 'Your visit makes a difference!'
            },
            {
                background: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
                title: '🎵 Connect with Alumni',
                subtitle: 'Join our music mentorship network',
                note: 'Real ads support our mission'
            },
            {
                background: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
                title: '🎶 Music Opportunities',
                subtitle: 'Discover careers in music industry',
                note: 'Powered by community support'
            },
            {
                background: 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
                title: '🎤 Alumni Network',
                subtitle: 'Connect, learn, and grow together',
                note: 'Supporting the next generation'
            }
        ];
    }

    showFallbackAd(adElement, slotNumber) {
        const designs = this.getFallbackAdDesigns();
        const design = designs[(slotNumber - 1) % designs.length];
        
        adElement.innerHTML = `
            <div class="uni-fallback-ad" style="background: ${design.background}; 
                        color: white; 
                        padding: 20px; 
                        text-align: center; 
                        border-radius: 12px;
                        min-height: 200px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                        cursor: pointer;
                        transition: transform 0.2s ease;"
                 onmouseover="this.style.transform='scale(1.02)'"
                 onmouseout="this.style.transform='scale(1)'"
                 onclick="console.log('Fallback ad clicked - slot ${slotNumber}')">
                <h3 style="margin: 0 0 10px 0; font-size: 18px; font-weight: bold;">${design.title}</h3>
                <p style="margin: 0 0 10px 0; opacity: 0.9; font-size: 14px;">${design.subtitle}</p>
                <small style="opacity: 0.7; font-size: 12px;">${design.note}</small>
            </div>
        `;
        
        // Mark as fallback ad
        adElement.dataset.fallbackAd = 'true';
        console.log('Showing fallback ad for slot', slotNumber, 'with design:', design.title);
    }

    setupFallbackDetection() {
        // Set up global error handlers for AdSense
        window.addEventListener('error', (e) => {
            if (e.target && e.target.src && e.target.src.includes('googlesyndication')) {
                console.log('AdSense script failed to load, showing fallbacks');
                if (this.config.showFallbackAds) {
                    setTimeout(() => this.showAllFallbackAds(), 500);
                }
            }
        });
        
        // Check for AdSense availability after page load
        setTimeout(() => {
            if (!window.adsbygoogle) {
                console.log('AdSense not available after timeout, showing fallbacks');
                this.showAllFallbackAds();
            } else {
                // Even if AdSense is available, check if ads actually loaded
                console.log('AdSense available, checking if ads loaded...');
                setTimeout(() => this.checkAndShowFallbacks(), 1000);
            }
        }, 1000);
        
        // Additional aggressive fallback check
        setTimeout(() => {
            console.log('Aggressive fallback check - ensuring ads are visible');
            this.checkAndShowFallbacks();
        }, 3000);
    }

    scheduleAdCheck(adElement, slotNumber) {
        // Multiple checks at different intervals - more aggressive timing
        const checkTimes = [1000, 2500, 4000];
        
        checkTimes.forEach(delay => {
            setTimeout(() => {
                if (!this.isAdLoaded(adElement) && !adElement.dataset.fallbackAd) {
                    console.log(`Ad slot ${slotNumber} still empty after ${delay}ms, showing fallback`);
                    this.showFallbackAd(adElement, slotNumber);
                }
            }, delay);
        });
    }

    isAdLoaded(adElement) {
        // Check if ad has loaded content
        const hasContent = adElement.innerHTML.trim() !== '';
        const hasIframe = adElement.querySelector('iframe') !== null;
        const hasGoogleAd = adElement.querySelector('[id*="google_ads"]') !== null;
        const isMarkedFilled = adElement.dataset.adsbygoogleStatus === 'done';
        const isFallbackAd = adElement.dataset.fallbackAd === 'true';
        
        // If it's already a fallback ad, consider it "loaded"
        if (isFallbackAd) {
            return true;
        }
        
        // For real AdSense ads, check if they have actual ad content
        const hasRealAdContent = hasIframe || hasGoogleAd || (hasContent && !isFallbackAd);
        
        console.log(`Ad check - hasContent: ${hasContent}, hasIframe: ${hasIframe}, hasGoogleAd: ${hasGoogleAd}, isFallback: ${isFallbackAd}, realContent: ${hasRealAdContent}`);
        
        return hasRealAdContent;
    }

    checkAndShowFallbacks() {
        const ads = document.querySelectorAll('.adsbygoogle');
        console.log('Checking if ads loaded...');
        ads.forEach((ad, index) => {
            if (!this.isAdLoaded(ad) && !ad.dataset.fallbackAd) {
                console.log(`Ad slot ${index + 1} didn't load, showing fallback`);
                this.showFallbackAd(ad, index + 1);
            }
        });
    }

    showAllFallbackAds() {
        const ads = document.querySelectorAll('.adsbygoogle');
        console.log(`Showing fallback ads for ${ads.length} ad slots`);
        ads.forEach((ad, index) => {
            if (!ad.dataset.fallbackAd && !ad.dataset.adsenseProcessed) {
                this.showFallbackAd(ad, index + 1);
            }
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
        
        // Test fallback system
        if (window.adsenseConfig.showFallbackAds) {
            console.log('Fallback ads enabled, running tests...');
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
        if (window.adsenseConfig.showFallbackAds) {
            window.adsenseManager.testAds();
        }
    }
}
