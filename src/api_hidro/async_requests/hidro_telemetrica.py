import asyncio
from datetime import datetime, timedelta

from api_hidro.sync_request import http_get_sync
from api_hidro.token_authentication import token_auth
from api_hidro.types import IntervaloDeBusca, JSONList, TipoFiltroData, TipoTelemetrica
from api_hidro.utils import flatten_concatenation


async def __retorna_serie_telemetrica_async(
    api_token: str,
    codigoestacao: int,
    tipo_telemetrica: TipoTelemetrica,
    tipo_filtro_data: TipoFiltroData,
    data_busca: str,
    intervalo_busca: IntervaloDeBusca,
) -> JSONList:
    headers = {"Authorization": f"Bearer {api_token}"}
    url = f"https://www.ana.gov.br/hidrowebservice/EstacoesTelemetricas/HidroinfoanaSerieTelemetrica{tipo_telemetrica}/v1"
    params: dict[str, int | str | float | bool | None] = {
        "Código da Estação": codigoestacao,
        "Tipo Filtro Data": tipo_filtro_data,
        "Data de Busca (yyyy-MM-dd)": data_busca,
        "Range Intervalo de busca": intervalo_busca,
    }
    data = await asyncio.to_thread(http_get_sync, url, headers, params)
    return data["items"]  # type: ignore


async def retorna_serie_historica_telemetrica(
    codigoestacao: int,
    tipo_telemetrica: TipoTelemetrica,
    tipo_filtro_data: TipoFiltroData,
    data_inicial: str,
    data_final: str,
    intervalo_busca: IntervaloDeBusca,
) -> JSONList | None:
    """Retorna os dados da estação telemétrica para o período selecionado.
        Será permitido um período máximo de 10 dias consecutivos

    Args:
        codigoestacao (int): Código da estação
        tipo_telemetrica (TipoTelemetrica): Tipos -> 'Detalhada', 'Adotada'
        tipo_filtro_data (TipoFiltroData): Tipos -> 'DATA_LEITURA', 'DATA_ULTIMA_ATUALIZACAO'
        data_inicial (str): Data no formato YYYY-MM-DD
        data_final (str): Data no formato YYYY-MM-DD
        intervalo_busca (IntervaloDeBusca): Intervalos definidos na API (5min até 24h)

    Raises:
        TokenNotFoundError: Erro quando o Token não é localizado

    Returns:
        JSONList | None: Série histórica no formato JSON
    """

    dt_inicial = datetime.strptime(data_inicial, "%Y-%m-%d").date()
    dt_final = datetime.strptime(data_final, "%Y-%m-%d").date()

    if dt_final < dt_inicial:
        raise ValueError("Data final não pode ser menor que data inicial")

    dif_dias = (dt_final - dt_inicial).days
    if dif_dias > 10:
        raise ValueError(
            "Intervalo de tempo entre datas deve ser menor ou igual a 10 dias"
        )

    with token_auth as api_token:
        result = await asyncio.gather(
            *[
                __retorna_serie_telemetrica_async(
                    api_token,
                    codigoestacao,
                    tipo_telemetrica,
                    tipo_filtro_data,
                    (dt_inicial + timedelta(days=num_dias)).strftime("%Y-%m-%d"),
                    intervalo_busca,
                )
                for num_dias in range(dif_dias + 1)
            ]
        )

        data = [i for i in result if i]

    return flatten_concatenation(data)
