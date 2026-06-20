import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class that reads environment variables"""

    # LLM Configuration
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

    # LangSmith Configuration
    LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
    LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT", "doc-intelligence-platform")
    LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING", "false")

    # App Configuration
    APP_ENV = os.getenv("APP_ENV", "development")
    APP_SECRET_KEY = os.getenv("DATABASE_URL", "")

    @classmethod
    def validate(cls):
        """Validate that all required environment variables are set"""
        required_vars = ["ANTHROPIC_API_KEY", "LANGSMITH_API_KEY"]

        for var in required_vars:
            if not getattr(cls, var):
                raise ValueError(f"Missing required environment variable: {var}")

        return True


# Create a single instance to use throughout the app
config = Config()

# Make LangSmith settings visible to the LangSmith wrapper,
# which reads these directly from the environment.
os.environ["LANGSMITH_TRACING"] = config.LANGSMITH_TRACING
os.environ["LANGSMITH_PROJECT"] = config.LANGSMITH_PROJECT
if config.LANGSMITH_API_KEY:
    os.environ["LANGSMITH_API_KEY"] = config.LANGSMITH_API_KEY