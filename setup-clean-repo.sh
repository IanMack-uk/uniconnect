#!/bin/bash

echo "🚀 Setting up clean UNI Connect repository..."

# Repository details
GITHUB_USERNAME="IanMack-uk"
NEW_REPO_NAME="uniconnect"
GITHUB_REPO_URL="https://github.com/$GITHUB_USERNAME/$NEW_REPO_NAME.git"

echo "📋 Repository Details:"
echo "   Username: $GITHUB_USERNAME"
echo "   Repository: $NEW_REPO_NAME"
echo "   URL: $GITHUB_REPO_URL"
echo ""

echo "⚠️  IMPORTANT: Create the GitHub repository first!"
echo "   1. Go to: https://github.com/new"
echo "   2. Repository name: $NEW_REPO_NAME"
echo "   3. Description: UNI Connect - Alumni networking app with Google AdSense"
echo "   4. Make it Public"
echo "   5. Don't initialize with README"
echo "   6. Click 'Create repository'"
echo ""

read -p "Have you created the GitHub repository '$NEW_REPO_NAME'? (y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Please create the GitHub repository first, then run this script again"
    exit 1
fi

# Add remote and push
echo "🔗 Adding remote origin..."
git remote add origin $GITHUB_REPO_URL

echo "🚀 Pushing to GitHub..."
git push -u origin main

echo ""
echo "✅ Clean repository created successfully!"
echo "🔗 Repository: $GITHUB_REPO_URL"
echo ""
echo "📋 Next steps:"
echo "1. Update Railway to use new repository: $GITHUB_REPO_URL"
echo "2. Delete old repository: https://github.com/$GITHUB_USERNAME/unialumniapp"
echo "3. Test deployment with clean commit history"
