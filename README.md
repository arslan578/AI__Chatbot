<h1 align="center" id="title">AI Chatbot with Django</h1>

<p id="description" align="center">Django | Gemini API | AI Studio</p>

<h2>🫦 Medium Link</h2>
<p><a href="https://thehormat.medium.com/ai-chatbot-with-django-c45d34b73051">Here is a great blog post for this great repo</a></p>

<h2>🚀 Project Setup Guide</h2>

### Prerequisites
- Python 3.8 or higher
- Poetry (Python package manager)

### 1. Install Poetry
If you haven't installed Poetry yet, run:
```bash
# For Unix/macOS/WSL
curl -sSL https://install.python-poetry.org | python3 -

# For Windows PowerShell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### 2. Clone the Repository
```bash
git clone git@github.com:TheHormat/AI__Chatbot.git
cd AI__Chatbot
```

### 3. Set Up Poetry Environment
```bash
# Configure Poetry to create virtual environment in project directory (optional)
poetry config virtualenvs.in-project true

# Install project dependencies
poetry install

# Activate the virtual environment
poetry shell
```

### 4. Update Dependencies (if needed)
```bash
poetry update
```

### 5. Configure Environment Variables
Create a `.env` file in the project root and add your configuration:
```env
GEMINI_API_KEY=your_api_key_here
DEBUG=True
```

### 6. Run the Development Server
```bash
python manage.py migrate  # Apply database migrations
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

<h2>📝 Additional Commands</h2>

```bash
# Add new dependencies
poetry add package_name

# Update specific package
poetry update package_name

# Show installed packages
poetry show

# Export dependencies to requirements.txt (if needed)
poetry export -f requirements.txt --output requirements.txt
```

<h2>🔧 Troubleshooting</h2>

1. If `poetry shell` doesn't work, ensure you're in the project directory and Poetry is properly installed
2. Verify Poetry installation: `poetry --version`
3. If you encounter any issues, try removing and reinstalling Poetry

<h2>📚 Project Structure</h2>

```
AI__Chatbot/
├── manage.py
├── pyproject.toml    # Poetry configuration
├── poetry.lock      # Locked dependencies
└── ...
```

<h2>🤝 Contributing</h2>

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<h2>🔐 Environment Setup</h2>

### 1. Create Environment File
Copy the example environment file and update it with your values:
```bash
cp .env.example .env
```

### 2. Get Google Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click on "Get API Key"
4. Create a new API key or use an existing one
5. Copy the API key
6. Paste it in your `.env` file for the `GEMINI_API_KEY` variable

### 3. Configure Environment Variables
Update the following variables in your `.env` file:

```env
# Generate a new Django secret key or use the existing one
SECRET_KEY=your_django_secret_key_here

# Database credentials (if using PostgreSQL)
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password

# Add your Gemini API key
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Generate Django Secret Key
You can generate a new Django secret key using Python:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Copy the output and paste it as your `SECRET_KEY` in the `.env` file.