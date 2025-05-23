from pydantic_settings import BaseSettings, SettingsConfigDict


# Clase de configuración que hereda de BaseSettings.
class Settings(BaseSettings):
    database_url: str
    model_config = SettingsConfigDict(
        env_file=".env",
    )


# Cargará las variables definidas en .env.
settings = Settings()
