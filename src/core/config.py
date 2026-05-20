from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


class Settings(BaseSettings):
    qntrl_client_id: str
    qntrl_client_secret: str
    qntrl_refresh_token: str
    qntrl_org_id: str
    qntrl_layout_id: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings() # pyright: ignore[reportCallIssue]