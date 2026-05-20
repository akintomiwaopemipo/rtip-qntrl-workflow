from typing import Any, cast

from pydantic import BaseModel


class AppBaseModel(BaseModel):

    def multipart(self) -> dict[str, tuple[None, str]]:

        data: dict[str, Any] = self.model_dump(
            exclude_none=True
        )

        custom_fields = cast(
            dict[str, Any],
            data.pop("custom_fields", {})
        )

        data.update(custom_fields)

        return {
            str(key): (None, str(value))
            for key, value in data.items()
        }