I'll help you refactor the project to better handle environment variables. Let's create the necessary files and update the documentation.

1. First, let's create a `.env.example` file:

```plaintext:/Users/arslan/Documents/Jobs/Turing/Chat_bot/marscode/AI__Chatbot/.env.example
# Django Settings
SECRET_KEY=your_django_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

# Google Gemini API
GOOGLE_API_KEY=your_gemini_api_key_here
```

2. Update the README.md with clear setup instructions:

```markdown:/Users/arslan/Documents/Jobs/Turing/Chat_bot/marscode/AI__Chatbot/README.md
<h1 align="center" id="title">AI Chatbot with Django</h1>

<p id="description" align="center">Django | Gemini API | AI Studio</p>

<h2>🛜 Project Setup Instructions</h2>

### Prerequisites
- Python 3.10.12
- Poetry (Python package manager)
- PostgreSQL
- Google Gemini API key

### 1. Clone the Repository
```bash
git clone git@github.com:TheHormat/AI__Chatbot.git
cd AI__Chatbot
```

### 2. Environment Setup

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Configure your environment variables:
   - Open the `.env` file in your text editor
   - Update the following variables:

   **Django Settings:**
   - `SECRET_KEY`: Generate a new Django secret key
   - `DEBUG`: Set to "True" for development, "False" for production
   - `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

   **Database Settings:**
   - `DB_NAME`: Your PostgreSQL database name
   - `DB_USER`: Your PostgreSQL username
   - `DB_PASSWORD`: Your PostgreSQL password
   - `DB_HOST`: Database host (usually "localhost")
   - `DB_PORT`: Database port (usually "5432")

   **Google Gemini API:**
   - `GOOGLE_API_KEY`: Your Gemini API key (see below for instructions)

### 3. Getting a Google Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key
5. Paste the key in your `.env` file as `GOOGLE_API_KEY`

### 4. Install Dependencies
```bash
poetry install
poetry shell
```

### 5. Database Setup
```bash
python manage.py migrate
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

<h2>🫦 Additional Resources</h2>
<p>Check out our detailed blog post: <a href="https://thehormat.medium.com/ai-chatbot-with-django-c45d34b73051">AI Chatbot with Django</a></p>

### Troubleshooting

If you encounter any issues:
1. Ensure all environment variables are properly set in `.env`
2. Verify PostgreSQL is running
3. Confirm your Gemini API key is valid
4. Make sure you're in the Poetry virtual environment

### Security Notes
- Never commit your `.env` file to version control
- Keep your API keys and credentials secure
- Use strong passwords for your database
```

3. Add `.env` to your `.gitignore` if it's not already there:

```plaintext:/Users/arslan/Documents/Jobs/Turing/Chat_bot/marscode/AI__Chatbot/.gitignore
# ... existing entries ...
.env
*.pyc
__pycache__/
```

These changes provide:
1. A template for environment variables
2. Clear documentation for setup
3. Step-by-step instructions for obtaining API keys
4. Security best practices
5. Troubleshooting guidance

The existing settings.py file already handles the environment variables correctly, so no changes are needed there.