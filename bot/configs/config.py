from pydantic_settings import BaseSettings, SettingsConfigDict


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


bot_settings = BotSettings()
openai_settings = OpenAISettings()



