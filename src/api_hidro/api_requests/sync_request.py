from typing import Any

import requests

from api_hidro.types import JSONObject


def http_get_sync(
    url: str, headers: dict[str, Any], params: JSONObject
) -> dict[str, Any]:
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        response.raise_for_status()

    return response.json()
