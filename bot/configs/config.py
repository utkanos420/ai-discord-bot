from pydantic_settings import BaseSettings, SettingsConfigDict
from openai import OpenAI


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


class BotSettings(BaseConfig):

    # token will be installed with pydantic from .env
    discord_bot_token: str = "xxx"

    # using default prefix if not set in .env
    discord_bot_prefix: str = "!"


class OpenAISettings(BaseConfig):

    # token will be installed with pydantic from .env
    openai_gemini_token: str = "xxx"

    # using default value for debugging
    openai_debug_version: str = "Gemini 2 flash lite"


class IgmurSettings(BaseConfig):

    # client-id is a token to download photo from discord for openai to open it
    igmur_client_token: str = "xxx"


bot_settings = BotSettings()
openai_settings = OpenAISettings()
igmur_settings = IgmurSettings()


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openai_settings.openai_gemini_token,
)



