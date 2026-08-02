from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    app_version: str

    host: str
    port: int

    debug: bool

    ai_provider: str

    # API keys (match keys present in .env)
    google_api_key: str = ""
    openai_api_key: str = ""
    openai_admin_key: str = ""
    gemini_api_key: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()