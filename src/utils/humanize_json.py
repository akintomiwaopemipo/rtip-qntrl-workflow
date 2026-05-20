from typing import Any


def humanize_json(data: Any) -> str:
    result: list[str] = []

    for key, value in data.items():
        readable_key = ''.join(
            f' {char}' if char.isupper() else char
            for char in key
        ).strip().title()

        result.append(f"{readable_key}: {value}")

    return "<br/><br/>".join(result)