import asyncio
from datetime import datetime
from typing import Literal, cast

from api_hidro.api_requests.sync_request import http_get_sync
from api_hidro.errors import TimeSerieNotFoundError
from api_hidro.models.api_response_models import JSONAPIResponse, JSONList
from api_hidro.models.models import (
    DadosMesAnoChuva,
    DadosMesAnoCota,
    DadosMesAnoVazao,
)
from api_hidro.token_authentication import TokenAuthHandler
from api_hidro.utils import flatten_concatenation

TipoDeEstacao = Literal["Chuva", "Cotas", "Vazao"]


async def __retorna_serie_anual(
    token_auth: TokenAuthHandler,
    codigoestacao: int,
    tipo_estacao: TipoDeEstacao,
    data_inicial: str,
    data_final: str,
) -> JSONAPIResponse:
    with token_auth as api_token:
        headers = {"Authorization": f"Bearer {api_token}"}
        url = f"https://www.ana.gov.br/hidrowebservice/EstacoesTelemetricas/HidroSerie{tipo_estacao}/v1"
        params: dict[str, int | str | float | bool | None] = {
            "Código da Estação": codigoestacao,
            "Tipo Filtro Data": "DATA_LEITURA",
            "Data Inicial (yyyy-MM-dd)": data_inicial,
            "Data Final (yyyy-MM-dd)": data_final,
        }
        data = await asyncio.to_thread(http_get_sync, url, headers, params)

    return cast(JSONAPIResponse, data)


async def __retorna_serie_historica(
    token_auth: TokenAuthHandler,
    codigoestacao: int,
    tipo_estacao: TipoDeEstacao,
    data_inicial: str,
    data_final: str,
) -> JSONList | None:
    """Retorna Série Histórica da estação escolhida

    Args:
        codigoestacao (int): Código da estação
        tipo_estacao (TipoDeEstacao): Tipos -> 'Chuva', 'Cotas', 'Vazao'
        data_inicial (str): Data no formato YYYY-MM-DD
        data_final (str): Data no formato YYYY-MM-DD

    Returns:
        JSONList: Série histórica no formato JSON
    """

    dt_inicial = datetime.strptime(data_inicial, "%Y-%m-%d").date()
    dt_final = datetime.strptime(data_final, "%Y-%m-%d").date()

    if dt_final < dt_inicial:
        raise ValueError("Data final não pode ser menor que data inicial")

    result = await asyncio.gather(
        *[
            __retorna_serie_anual(
                token_auth,
                codigoestacao,
                tipo_estacao,
                f"{ano}-01-01",
                f"{ano}-12-31",
            )
            for ano in range(dt_inicial.year, dt_final.year + 1)
        ]
    )

    data = [json_obj.get("items") for json_obj in result if json_obj]

    return flatten_concatenation(data)


def retorna_serie_historica(
    token_auth: TokenAuthHandler,
    codigoestacao: int,
    tipo_estacao: TipoDeEstacao,
    data_inicial: str,
    data_final: str,
) -> JSONList | None:
    """Retorna Série Histórica da estação escolhida

    Args:
        codigoestacao (int): Código da estação
        tipo_estacao (TipoDeEstacao): Tipos -> 'Chuva', 'Cotas', 'Vazao'
        data_inicial (str): Data no formato YYYY-MM-DD
        data_final (str): Data no formato YYYY-MM-DD

    Returns:
        JSONList: Série histórica no formato JSON
    """

    return asyncio.run(
        __retorna_serie_historica(
            token_auth, codigoestacao, tipo_estacao, data_inicial, data_final
        )
    )


def serie_historica_chuva(
    token_auth: TokenAuthHandler, codigoestacao: int, data_inicial: str, data_final: str
) -> list[DadosMesAnoChuva]:
    """Retorna Série Histórica de Chuvas da estação escolhida

    Args:
        codigoestacao (int): Código da estação
        data_inicial (str): Data no formato YYYY-MM-DD
        data_final (str): Data no formato YYYY-MM-DD

    Raises:
        TimeSerieNotFoundError: Erro lançado caso a série histórica não seja encontrada

    Returns:
        list[DadoDiarioChuva]: Lista de dados diários de chuva no formato de modelo Pydantic
    """

    serie_diaria_chuva = retorna_serie_historica(
        token_auth=token_auth,
        codigoestacao=codigoestacao,
        tipo_estacao="Chuva",
        data_inicial=data_inicial,
        data_final=data_final,
    )

    if not serie_diaria_chuva:
        raise TimeSerieNotFoundError(
            f"Série histórica de chuva não encontrada para o código da estação {codigoestacao}."
        )

    return [DadosMesAnoChuva.model_validate(item) for item in serie_diaria_chuva]


def serie_historica_cota(
    token_auth: TokenAuthHandler, codigoestacao: int, data_inicial: str, data_final: str
) -> list[DadosMesAnoCota]:
    """Retorna Série Histórica de Cotas da estação escolhida

    Args:
        codigoestacao (int): Código da estação
        data_inicial (str): Data no formato YYYY-MM-DD
        data_final (str): Data no formato YYYY-MM-DD

    Raises:
        TimeSerieNotFoundError: Erro lançado caso a série histórica não seja encontrada

    Returns:
        list[DadoDiarioCota]: Lista de dados diários de cota no formato de modelo Pydantic
    """

    serie_diaria_cota = retorna_serie_historica(
        token_auth=token_auth,
        codigoestacao=codigoestacao,
        tipo_estacao="Cotas",
        data_inicial=data_inicial,
        data_final=data_final,
    )

    if not serie_diaria_cota:
        raise TimeSerieNotFoundError(
            f"Série histórica de cota não encontrada para o código da estação {codigoestacao}."
        )

    return [DadosMesAnoCota.model_validate(item) for item in serie_diaria_cota]


def serie_historica_vazao(
    token_auth: TokenAuthHandler, codigoestacao: int, data_inicial: str, data_final: str
) -> list[DadosMesAnoVazao]:
    """Retorna Série Histórica de Vazões da estação escolhida

    Args:
        codigoestacao (int): Código da estação
        data_inicial (str): Data no formato YYYY-MM-DD
        data_final (str): Data no formato YYYY-MM-DD

    Raises:
        TimeSerieNotFoundError: Erro lançado caso a série histórica não seja encontrada

    Returns:
        list[DadoDiarioVazao]: Lista de dados diários de vazão no formato de modelo Pydantic
    """

    serie_diaria_vazao = retorna_serie_historica(
        token_auth=token_auth,
        codigoestacao=codigoestacao,
        tipo_estacao="Vazao",
        data_inicial=data_inicial,
        data_final=data_final,
    )

    if not serie_diaria_vazao:
        raise TimeSerieNotFoundError(
            f"Série histórica de vazão não encontrada para o código da estação {codigoestacao}."
        )

    return [
        DadosMesAnoVazao.model_validate(item, by_alias=True)
        for item in serie_diaria_vazao
    ]
