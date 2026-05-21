from src.domain.models.app_base_model import AppBaseModel


class ApiError(AppBaseModel):
    error: str
    status_code: int | None = None