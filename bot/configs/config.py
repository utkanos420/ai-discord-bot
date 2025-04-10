from pydantic_settings import BaseSettings, SettingsConfigDict
from openai import OpenAI


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


class BotSettings(BaseConfig):

    # token will be installed with pydantic from .env
    discord_bot_token: str = "xxx"

    # using default prefix if not set in .env
    discord_bot_prefix: str = "!"


class OpenRouterGeminiSettings(BaseConfig):

    # token will be installed with pydantic from .env
    gemini_token: str = "xxx"

    # using default value for debugging
    gemini_debug_version: str = "Google: Gemini Flash 2.0 Experimental (free)"


class ImgurSettings(BaseConfig):

    # client-id is a token to download photo from discord for openai to open it
    imgur_client_token: str = "xxx"


bot_settings = BotSettings()
gemini_settings = OpenRouterGeminiSettings()
imgur_settings = ImgurSettings()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=gemini_settings.gemini_token,
)



