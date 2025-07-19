# 🚀 Complete Setup Guide

This guide will walk you through setting up the Docker AI Link Summarizer project from scratch.

## 📋 Prerequisites

Before you begin, make sure you have:

- [ ] Git installed on your computer
- [ ] Docker and Docker Compose installed
- [ ] A GitHub account
- [ ] An OpenAI account with API access

## 🔑 Step 1: Get Your OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to **API Keys** section
4. Click **"Create new secret key"**
5. Copy the key (it starts with `sk-`)
6. **Important**: Save this key securely - you won't see it again!

## 📁 Step 2: Create Your Project Directory

```bash
# Create and enter project directory
mkdir docker-ai-link-summarizer
cd docker-ai-link-summarizer

# Create templates directory
mkdir templates
```

## 📄 Step 3: Create All Project Files

Copy the following files from the artifacts into your project directory:

### Root Directory Files:
- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies  
- `Dockerfile` - Docker configuration
- `docker-compose.yml` - Docker Compose setup
- `.env.example` - Environment template
- `.gitignore` - Git ignore rules
- `LICENSE` - MIT license
- `README.md` - Project documentation

### Templates Directory:
- `templates/index.html` - Web UI template

Your final structure should look like:
```
docker-ai-link-summarizer/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── templates/
    └── index.html
```

## 🔐 Step 4: Set Up Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env file and add your OpenAI API key
# Replace 'your-openai-api-key-here' with your actual key
echo "OPENAI_API_KEY=sk-your-actual-key-here" > .env
```

## 🧪 Step 5: Test Locally

```bash
# Build and run with Docker Compose
docker-compose up --build

# Wait for the container to start, then open:
# http://localhost:3000
```

Test by entering a URL (like a news article) and clicking "Summarize".

## 📚 Step 6: Initialize Git Repository

```bash
# Initialize git repository
git init

# Add all files (except those in .gitignore)
git add .

# Make your first commit
git commit -m "Initial commit: Link Summarizer with dark mode"
```

## 🐙 Step 7: Create GitHub Repository

### Option A: Using GitHub Web Interface

1. Go to [GitHub](https://github.com)
2. Click the **"+"** icon → **"New repository"**
3. Name it `docker-ai-link-summarizer`
4. **Don't** initialize with README (we already have one)
5. Click **"Create repository"**

### Option B: Using GitHub CLI (if installed)

```bash
gh repo create docker-ai-link-summarizer --public --source=. --remote=origin --push
```

## 🚀 Step 8: Push to GitHub

```bash
# Add GitHub as remote origin
git remote add origin https://github.com/undergroundpost/docker-ai-link-summarizer.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## 🎉 Step 9: Verify Everything Works

1. **Check GitHub**: Visit your repository URL
2. **Clone test**: Try cloning in a different directory
3. **Documentation**: Make sure README displays properly
4. **Environment**: Verify `.env` is not in the repository

## 🔧 Step 10: Customize for Your Needs

### Update README.md:
- Repository URLs are already set for undergroundpost/docker-ai-link-summarizer
- Add actual screenshots (replace placeholder URLs)
- Update any custom descriptions if needed

### Customize the App:
- Modify colors in `templates/index.html`
- Change the app title or description
- Add your own features

## 🌐 Step 11: Optional - Deploy to Production

### Railway:
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway deploy
```

### Heroku:
```bash
# Install Heroku CLI and login
heroku create your-app-name
heroku config:set OPENAI_API_KEY=your-key
git push heroku main
```

### DigitalOcean App Platform:
1. Connect your GitHub repository
2. Set environment variable `OPENAI_API_KEY`
3. Deploy automatically

## 🛠️ Troubleshooting

### Common Issues:

**Port 3000 already in use:**
```bash
# Change port in docker-compose.yml
ports:
  - "8080:5000"  # Use port 8080 instead
```

**OpenAI API errors:**
- Verify your API key is correct
- Check your OpenAI account has credits
- Ensure the key has proper permissions

**Docker issues:**
```bash
# Clean up Docker
docker-compose down
docker system prune -f
docker-compose up --build
```

**Git push issues:**
- Make sure you've set up SSH keys or use HTTPS
- Verify repository name and username are correct

## 📈 Next Steps

1. **Star the repository** if you found it useful
2. **Create issues** for bugs or feature requests  
3. **Fork and contribute** improvements
4. **Share with others** who might find it useful

## 💡 Pro Tips

- **Monitor API usage** in your OpenAI dashboard
- **Set up billing alerts** to avoid unexpected charges
- **Keep your API key secure** - never commit it to Git
- **Consider rate limiting** for production deployments
- **Add monitoring** and error tracking for production use

---

🎉 **Congratulations!** You now have a fully functional, GitHub-hosted Docker AI Link Summarizer!

Need help? Create an issue in the repository or check the troubleshooting section above.
