# 🔗 Docker AI Link Summarizer

A fun, AI-powered web application that instantly summarizes any webpage using OpenAI's GPT-3.5. Built with Flask and Docker for easy deployment.

## ✨ Features

- 🤖 **AI-Powered Summaries** - Uses OpenAI GPT-3.5 for intelligent content summarization
- 🎨 **Beautiful UI** - Modern glassmorphism design with smooth animations
- 🌙 **Dark Mode** - Toggle between light and dark themes
- 📱 **Responsive Design** - Works perfectly on desktop and mobile
- ⚡ **Real-time Processing** - Loading animations and error handling
- 🐳 **Docker Ready** - Containerized with production-ready Gunicorn server
- 🛡️ **Robust Error Handling** - Graceful handling of invalid URLs and API errors

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/undergroundpost/docker-ai-link-summarizer.git
   cd docker-ai-link-summarizer
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-openai-key-here
   ```

3. **Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

4. **Open your browser**
   ```
   http://localhost:3000
   ```

## 🛠️ Development Setup

### Local Development (without Docker)

1. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variable**
   ```bash
   export OPENAI_API_KEY=your-key-here
   ```

3. **Run the Flask app**
   ```bash
   python app.py
   ```

4. **Access at** `http://localhost:5000`

### Project Structure

```
docker-ai-link-summarizer/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
├── gunicorn.conf.py      # Gunicorn production server config
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore rules
├── README.md            # Project documentation
└── templates/
    └── index.html       # Web UI template
```

## 🎨 Screenshots

### Light Mode
![Light Mode](https://via.placeholder.com/600x400/667eea/ffffff?text=Light+Mode)

### Dark Mode
![Dark Mode](https://via.placeholder.com/600x400/1a1a2e/ffffff?text=Dark+Mode)

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

### Docker Configuration

The application runs on port 5000 inside the container and is mapped to port 3000 on your host machine. You can change this in `docker-compose.yml`:

```yaml
ports:
  - "YOUR_PORT:5000"
```

## 🌐 Usage

1. **Enter a URL** - Paste any webpage URL (news articles, blog posts, documentation)
2. **Click Summarize** - The AI will extract and summarize the content
3. **Read the Summary** - Get a concise 2-3 paragraph summary
4. **Toggle Dark Mode** - Click the sun/moon icon for theme switching

### Supported Content Types

- News articles
- Blog posts
- Documentation pages
- Research papers
- Product pages
- Wikipedia articles

## 🔧 API Reference

### POST /summarize

Summarizes the content of a given URL.

**Request Body:**
```json
{
  "url": "https://example.com/article"
}
```

**Response:**
```json
{
  "success": true,
  "title": "Article Title",
  "summary": "AI-generated summary...",
  "url": "https://example.com/article"
}
```

## 🚀 Deployment

### Docker Deployment

```bash
# Build and run
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

### Production Considerations

- ✅ Uses production-ready Gunicorn WSGI server
- Set up reverse proxy (nginx) for additional performance
- Configure proper environment variables
- Monitor API usage and costs
- Implement rate limiting
- Scale workers based on traffic

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Important Notes

- **API Costs**: This app uses OpenAI's API which charges per token. Monitor your usage.
- **Rate Limits**: OpenAI has rate limits on API calls. The app handles errors gracefully.
- **Content Extraction**: Some websites may block automated content extraction.

## 🙏 Acknowledgments

- OpenAI for providing the GPT-3.5 API
- Flask framework for the web application
- Beautiful Soup for web scraping
- Docker for containerization

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/undergroundpost/docker-ai-link-summarizer/issues) page
2. Create a new issue with detailed information
3. Make sure to include error logs and steps to reproduce
