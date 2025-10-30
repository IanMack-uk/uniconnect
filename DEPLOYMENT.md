# 🚀 Deployment Guide: connect.vaccin8.io

## Quick Deployment to Railway

### Step 1: Prepare Repository
```bash
# Initialize git repository (if not already done)
git init
git add .
git commit -m "Initial commit: UNI Connect AdSense app"

# Push to GitHub (create repo first)
git remote add origin https://github.com/yourusername/uni-connect.git
git push -u origin main
```

### Step 2: Deploy to Railway
1. **Visit**: https://railway.app/
2. **Sign up** with GitHub account
3. **Click "Deploy from GitHub repo"**
4. **Select your repository**
5. **Railway will auto-detect** Python and deploy

### Step 3: Configure Custom Domain
1. **In Railway dashboard** → Settings → Domains
2. **Add custom domain**: `connect.vaccin8.io`
3. **Copy the CNAME record** Railway provides
4. **Add CNAME to vaccin8.io DNS**:
   ```
   Type: CNAME
   Name: connect
   Value: [railway-provided-value]
   TTL: 300
   ```

### Step 4: Environment Variables
In Railway dashboard → Variables, add:
```
ENVIRONMENT=production
ADSENSE_PUBLISHER_ID=ca-pub-9219208012298253
ADSENSE_TEST_MODE=false
SHOW_FALLBACK_ADS=false
```

### Step 5: Verify Deployment
- **Check health**: https://connect.vaccin8.io/adsense-status
- **Test pages**: https://connect.vaccin8.io/
- **Verify ads.txt**: https://connect.vaccin8.io/ads.txt

## AdSense Setup Process

### Step 1: Add Site to AdSense
1. **Login**: https://www.google.com/adsense/
2. **Sites** → Add site → `connect.vaccin8.io`
3. **Wait for approval** (1-14 days)

### Step 2: Create Ad Units
After approval:
1. **Ads** → By ad unit → Display ads
2. **Create two ad units**:
   - "UNI Connect Home Sidebar"
   - "UNI Connect Mentors Inline"
3. **Copy the slot IDs** (10-digit numbers)

### Step 3: Update Configuration
In Railway → Variables, update:
```
ADSENSE_HOME_SLOT_ID=your-real-home-slot-id
ADSENSE_MENTORS_SLOT_ID=your-real-mentors-slot-id
```

## Troubleshooting

### Common Issues:
- **DNS propagation**: Can take up to 24 hours
- **SSL certificate**: Railway handles automatically
- **AdSense approval**: Ensure good content and traffic

### Health Check:
```bash
curl https://connect.vaccin8.io/adsense-status
```

Should return `"production_ready": true` when fully configured.

## Timeline Estimate:
- **Deployment**: 10 minutes
- **DNS setup**: 1-24 hours  
- **AdSense approval**: 1-14 days
- **Total**: 1-15 days for full setup
