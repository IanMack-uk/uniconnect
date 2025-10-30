#!/bin/bash

echo "📦 Pushing UNI Connect to GitHub..."

# You'll need to replace this URL with your actual GitHub repo URL
GITHUB_REPO_URL="https://github.com/yourusername/uni-connect.git"

echo "⚠️  IMPORTANT: Update GITHUB_REPO_URL in this script first!"
echo "   Current URL: $GITHUB_REPO_URL"
echo ""
read -p "Have you updated the GitHub repo URL? (y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Please update the GITHUB_REPO_URL variable in this script first"
    exit 1
fi

# Add remote origin
git remote add origin $GITHUB_REPO_URL

# Push to GitHub
echo "🚀 Pushing to GitHub..."
git push -u origin main

echo "✅ Code pushed to GitHub!"
echo "📋 Next: Deploy on Railway at https://railway.app/"
