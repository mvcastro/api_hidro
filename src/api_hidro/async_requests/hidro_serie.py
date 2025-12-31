import asyncio
from datetime import datetime
from typing import Literal, cast

from api_hidro.sync_request import http_get_sync
from api_hidro.token_authentication import token_auth
from api_hidro.types import JSONList
from api_hidro.utils import flatten_concatenation

TipoDeEstacao = Literal["Chuva", "Cota", "Vazao"]


async def __retorna_serie_anual(
    api_token: str,
    codigoestacao: int,
    tipo_estacao: TipoDeEstacao,
    data_inicial: str,
    data_final: str,
) -> JSONList:
    headers = {"Authorization": f"Bearer {api_token}"}
    url = f"https://www.ana.gov.br/hidrowebservice/EstacoesTelemetricas/HidroSerie{tipo_estacao}/v1"
    params: dict[str, int | str | float | bool | None] = {
        "Código da Estação": codigoestacao,
        "Tipo Filtro Data": "DATA_LEITURA",
        "Data Inicial (yyyy-MM-dd)": data_inicial,
        "Data Final (yyyy-MM-dd)": data_final,
    }
    data = await asyncio.to_thread(http_get_sync, url, headers, params)

    return cast(JSONList, data["items"])


async def __retorna_serie_historica(
    codigoestacao: int, tipo_estacao: TipoDeEstacao, data_inicial: str, data_final: str
) -> JSONList | None:
    """Retorna Série Histórica da estação escolhida

    Args:
        codigoestacao (int): Código da estação
        tipo_estacao (TipoDeEstacao): Tipos -> 'Chuva', 'Cota', 'Vazao'
        data_inicial (str): Data no formato YYYY-MM-DD
        data_final (str): Data no formato YYYY-MM-DD

    Returns:
        JSONList: Série histórica no formato JSON
    """

    with token_auth as api_token:
        dt_inicial = datetime.strptime(data_inicial, "%Y-%m-%d").date()
        dt_final = datetime.strptime(data_final, "%Y-%m-%d").date()

        result = await asyncio.gather(
            *[
                __retorna_serie_anual(
                    api_token,
                    codigoestacao,
                    tipo_estacao,
                    f"{ano}-01-01",
                    f"{ano}-12-31",
                )
                for ano in range(dt_inicial.year, dt_final.year + 1)
            ]
        )

        data = [json_obj for json_obj in result if json_obj]

    return flatten_concatenation(data)


def retorna_serie_historica(
    codigoestacao: int, tipo_estacao: TipoDeEstacao, data_inicial: str, data_final: str
) -> JSONList | None:
    """Retorna Série Histórica da estação escolhida

    Args:
        codigoestacao (int): Código da estação
        tipo_estacao (TipoDeEstacao): Tipos -> 'Chuva', 'Cota', 'Vazao'
        data_inicial (str): Data no formato YYYY-MM-DD
        data_final (str): Data no formato YYYY-MM-DD

    Returns:
        JSONList: Série histórica no formato JSON
    """

    return asyncio.run(__retorna_serie_historica(
        codigoestacao, tipo_estacao, data_inicial, data_final
    ))