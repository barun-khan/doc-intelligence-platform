import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
class Config:
    """Configuration class that reads environment variables"""

    # LLM Configuration
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

    # LangSmith Configuration
    LANGSMITH_API_KEY = os.getenv ("LANGSMITH_API_KEY")
    LANGSMITH_PROJECT = os.getenv ("LANGSMITH_PROJECT", "doc-intelligence-platform")

    # App Configuration
    APP_ENV = os.getenv ("APP_ENV", "development")
    APP_SECRET_KEY = os.getenv("DATABASE_URL", "")

    @classmethod
    def validate(cls):
        """Validate that all required environment variables are set"""
        required_vars = ["ANTHROPIC_API_KEY", "LANGSMITH_API_KEY"]

        for var in required_vars:
            if not getattr(cls, var):
                raise ValueError (f"Missing required environment variable: {var}")
            
        return True
    
# Create a single instance to use throughout the app
config = Config()