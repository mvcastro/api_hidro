import asyncio
from typing import cast

from api_hidro.constants import BACIAS
from api_hidro.sync_request import http_get_sync
from api_hidro.types import CodigoBacia, Estado, JSONAPIResponse, JSONList
from api_hidro.utils import flatten_concatenation

from ..errors import ArgsNotGiven
from ..token_authentication import token_auth


async def __retorna_inventario(
    codigoestacao: int | None = None,
    unidade_federativa: Estado | None = None,
    codigo_bacia: CodigoBacia | None = None,
) -> JSONAPIResponse:
    """Retorna Inventário da estação selecionada.
        Pelo menos unm dos argumentos da função deve ser fornecida

    Args:
        codigoestacao (int | None, optional): Código da estação. Defaults to None.
        unidade_federativa (str | None, optional): Sigla da Unidade Federativa. Defaults to None.
        codigo_bacia (int | None, optional): Código da Bacia. Defaults to None.

    Raises:
        ArgsNotGiven: Erro gerado quando não for fornecido nenhum dos argumentos

    Returns:
        JSONList: Retorna em uma lista, o inventário da estação em formato JSON
    """

    if not any([codigoestacao, unidade_federativa, codigo_bacia]):
        raise ArgsNotGiven("Pelo menos um dos campos de pesquisa deve ser fornecido!")

    with token_auth as api_token:
        headers = {"Authorization": f"Bearer {api_token}"}
        url = "https://www.ana.gov.br/hidrowebservice/EstacoesTelemetricas/HidroInventarioEstacoes/v1"

        params: dict[str, int | str | float | bool | None] = {
            "Código da Estação": codigoestacao,
            "Unidade Federativa": unidade_federativa,
            "Código da Bacia": codigo_bacia,
        }
        data = await asyncio.to_thread(http_get_sync, url, headers, params)

    return cast(JSONAPIResponse, data)


async def __retorna_inventario_completo() -> JSONList:
    """Retorna inventário completo das estações do HIDRO

    Returns:
        JSONList: Retorna uma lista com o inventário de todas as estação em formato JSON
    """

    result = await asyncio.gather(
        *[__retorna_inventario(codigo_bacia=bacia["codigobacia"]) for bacia in BACIAS]
    )

    if not result:
        raise ValueError("Nenhum dado retornado para o inventário completo.")

    data: list[JSONList] = []

    for obj in result:
        if obj is not None:
            json_obj = obj.get("items")
            if json_obj:
                data.append(json_obj)

    return flatten_concatenation(data)


def retorna_inventario(
    codigoestacao: int | None = None,
    unidade_federativa: Estado | None = None,
    codigo_bacia: CodigoBacia | None = None,
) -> JSONList:
    """Retorna Inventário da estação selecionada.
        Pelo menos unm dos argumentos da função deve ser fornecida

    Args:
        codigoestacao (int | None, optional): Código da estação. Defaults to None.
        unidade_federativa (str | None, optional): Sigla da Unidade Federativa. Defaults to None.
        codigo_bacia (int | None, optional): Código da Bacia. Defaults to None.

    Raises:
        ArgsNotGiven: Erro gerado quando não for fornecido nenhum dos argumentos

    Returns:
        JSONList: Retorna em uma lista, o inventário da estação em formato JSON
    """

    if not any([codigoestacao, unidade_federativa, codigo_bacia]):
        raise ArgsNotGiven("Pelo menos um dos campos de pesquisa deve ser fornecido!")

    response = asyncio.run(
        __retorna_inventario(
            codigoestacao=codigoestacao,
            unidade_federativa=unidade_federativa,
            codigo_bacia=codigo_bacia,
        )
    )

    return response["items"]


def retorna_inventario_completo() -> JSONList:
    """Retorna inventário completo das estações do HIDRO

    Returns:
        JSONList: Retorna uma lista com o inventário de todas as estação em formato JSON
    """
    result = asyncio.run(__retorna_inventario_completo())
    return result
