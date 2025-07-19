import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify
from urllib.parse import urlparse

app = Flask(__name__)

def extract_content(url):
    """Extract text content from a webpage"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "aside"]):
            script.decompose()
        
        # Try to get the title
        title = soup.find('title')
        title_text = title.get_text().strip() if title else "No title found"
        
        # Get main content
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return {
            'title': title_text,
            'content': text[:5000],  # Limit to avoid token limits
            'success': True
        }
        
    except Exception as e:
        return {
            'title': '',
            'content': '',
            'success': False,
            'error': str(e)
        }

def summarize_content(content, title, api_key):
    """Summarize content using OpenAI API directly"""
    try:
        # Use direct API call instead of the OpenAI library
        url = "https://api.openai.com/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        prompt = f"Title: {title}\n\nContent: {content}\n\nPlease provide a clear and concise summary of this webpage in 2-3 well-structured paragraphs:"
        
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system", 
                    "content": "You are a helpful assistant that creates clear, informative summaries of web content. Focus on the main points and key information."
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            "max_tokens": 400,
            "temperature": 0.3
        }
        
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        summary = result['choices'][0]['message']['content'].strip()
        
        return {
            'summary': summary,
            'success': True
        }
        
    except Exception as e:
        return {
            'summary': '',
            'success': False,
            'error': str(e)
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    url = data.get('url', '').strip()
    
    # Validate URL
    try:
        result = urlparse(url)
        if not all([result.scheme, result.netloc]):
            return jsonify({'success': False, 'error': 'Please provide a valid URL'})
    except:
        return jsonify({'success': False, 'error': 'Invalid URL format'})
    
    # Get API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        return jsonify({'success': False, 'error': 'OpenAI API key not configured'})
    
    # Extract content
    extraction_result = extract_content(url)
    if not extraction_result['success']:
        return jsonify({'success': False, 'error': f"Failed to extract content: {extraction_result['error']}"})
    
    if not extraction_result['content'].strip():
        return jsonify({'success': False, 'error': 'No content found on the webpage'})
    
    # Summarize content
    summary_result = summarize_content(
        extraction_result['content'], 
        extraction_result['title'], 
        api_key
    )
    
    if not summary_result['success']:
        return jsonify({'success': False, 'error': f"Failed to generate summary: {summary_result['error']}"})
    
    return jsonify({
        'success': True,
        'title': extraction_result['title'],
        'summary': summary_result['summary'],
        'url': url
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)