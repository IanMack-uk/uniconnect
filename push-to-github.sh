#!/bin/bash

echo "📦 Pushing UNI Connect to GitHub as 'unialumniapp'..."

# Replace 'yourusername' with your actual GitHub username
GITHUB_USERNAME="yourusername"
GITHUB_REPO_URL="https://github.com/$GITHUB_USERNAME/unialumniapp.git"

echo "⚠️  IMPORTANT: Update your GitHub username!"
echo "   Current URL: $GITHUB_REPO_URL"
echo ""
read -p "Enter your GitHub username: " github_user
GITHUB_REPO_URL="https://github.com/$github_user/unialumniapp.git"
echo "   Updated URL: $GITHUB_REPO_URL"
echo ""

# Check if remote already exists
if git remote get-url origin >/dev/null 2>&1; then
    echo "🔄 Updating existing remote origin..."
    git remote set-url origin $GITHUB_REPO_URL
else
    echo "➕ Adding remote origin..."
    git remote add origin $GITHUB_REPO_URL
fi

# Switch to main branch
git branch -M main

# Push to GitHub
echo "🚀 Pushing to GitHub..."
git push -u origin main

echo "✅ Code pushed to GitHub!"
echo "📋 Next: Deploy on Railway at https://railway.app/"
echo "🔗 Repository: $GITHUB_REPO_URL"
