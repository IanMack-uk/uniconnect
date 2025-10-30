#!/bin/bash

# UNI Connect Deployment Script
echo "🚀 Deploying UNI Connect to connect.vaccin8.io"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit: UNI Connect AdSense app"
else
    echo "📦 Git repository exists, committing changes..."
    git add .
    git commit -m "Update: $(date)"
fi

# Check production configuration
echo "🔍 Checking production configuration..."
if [ -f ".env.production" ]; then
    echo "✅ Production environment file found"
else
    echo "❌ Production environment file missing"
    exit 1
fi

# Validate required files
required_files=("requirements.txt" "railway.json" "ads.txt" "DEPLOYMENT.md")
for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file found"
    else
        echo "❌ $file missing"
        exit 1
    fi
done

echo ""
echo "🎯 Ready for deployment!"
echo ""
echo "Next steps:"
echo "1. Push to GitHub: git remote add origin <your-repo-url> && git push -u origin main"
echo "2. Deploy on Railway: https://railway.app/"
echo "3. Configure DNS: Add CNAME record for connect.vaccin8.io"
echo "4. Add to AdSense: https://www.google.com/adsense/"
echo ""
echo "📖 See DEPLOYMENT.md for detailed instructions"
