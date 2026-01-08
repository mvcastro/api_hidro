from api_hidro.api_requests.models import DadoTelemetricaDetalhada
import asyncio
from datetime import datetime, timedelta

from api_hidro.api_requests.models import DadoTelemetricaAdotada
from api_hidro.api_requests.sync_request import http_get_sync
from api_hidro.errors import TimeSerieNotFoundError
from api_hidro.token_authentication import TokenAuthHandler
from api_hidro.types import IntervaloDeBusca, JSONList, TipoFiltroData, TipoTelemetrica
from api_hidro.utils import flatten_concatenation


async def __retorna_serie_telemetrica_async(
    token_auth: TokenAuthHandler,
    codigoestacao: int,
    tipo_telemetrica: TipoTelemetrica,
    tipo_filtro_data: TipoFiltroData,
    data_busca: str,
    intervalo_busca: IntervaloDeBusca,
) -> JSONList:
    with token_auth as api_token:
        headers = {"Authorization": f"Bearer {api_token}"}
        url = f"https://www.ana.gov.br/hidrowebservice/EstacoesTelemetricas/HidroinfoanaSerieTelemetrica{tipo_telemetrica}/v1"
        params: dict[str, int | str | float | bool | None] = {
            "Código da Estação": codigoestacao,
            "Tipo Filtro Data": tipo_filtro_data,
            "Data de Busca (yyyy-MM-dd)": data_busca,
            "Range Intervalo de busca": intervalo_busca,
        }
        data = await asyncio.to_thread(http_get_sync, url, headers, params)
        return data["items"]


async def __retorna_serie_historica_telemetrica(
    token_auth: TokenAuthHandler,
    codigoestacao: int,
    tipo_telemetrica: TipoTelemetrica,
    tipo_filtro_data: TipoFiltroData,
    data_inicial: str,
    data_final: str,
    intervalo_busca: IntervaloDeBusca,
) -> JSONList | None:
    """Função privada do módulo
        Retorna os dados da estação telemétrica para o período selecionado.
        Será permitido um período máximo de 10 dias consecutivos

    Args:
        token_auth (TokenAuthHandler): Objeto da classe TokenAuthHandler para autenticação
            de acesso à API
        codigoestacao (int): Código da estação
        tipo_telemetrica (TipoTelemetrica): Tipos -> 'Detalhada', 'Adotada'
        tipo_filtro_data (TipoFiltroData): Tipos -> 'DATA_LEITURA', 'DATA_ULTIMA_ATUALIZACAO'
        data_inicial (str): Data no formato YYYY-MM-DD
        data_final (str): Data no formato YYYY-MM-DD
        intervalo_busca (IntervaloDeBusca): Intervalos definidos na API (5min até 24h)

    Raises:
        TokenNotFoundError: Erro quando o Token não é localizado

    Returns:
        JSONList | None: Série histórica no formato JSON (dicionário Python)
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

    result = await asyncio.gather(
        *[
            __retorna_serie_telemetrica_async(
                token_auth,
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


def retorna_serie_historica_telemetrica(
    token_auth: TokenAuthHandler,
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
        token_auth (TokenAuthHandler): Objeto da classe TokenAuthHandler para autenticação
            de acesso à API
        codigoestacao (int): Código da estação
        tipo_telemetrica (TipoTelemetrica): Tipos -> 'Detalhada', 'Adotada'
        tipo_filtro_data (TipoFiltroData): Tipos -> 'DATA_LEITURA', 'DATA_ULTIMA_ATUALIZACAO'
        data_inicial (str): Data no formato YYYY-MM-DD
        data_final (str): Data no formato YYYY-MM-DD
        intervalo_busca (IntervaloDeBusca): Intervalos definidos na API (5min até 24h)

    Returns:
        JSONList | None: Série histórica no formato JSON (dicionário Python)
    """
    return asyncio.run(
        __retorna_serie_historica_telemetrica(
            token_auth,
            codigoestacao,
            tipo_telemetrica,
            tipo_filtro_data,
            data_inicial,
            data_final,
            intervalo_busca,
        )
    )


def serie_historica_telemetrica_adotada(
    token_auth: TokenAuthHandler,
    codigoestacao: int,
    data_inicial: str,
    data_final: str,
    intervalo_busca: IntervaloDeBusca = "HORA_24",
) -> list[DadoTelemetricaAdotada]:
    """Retorna os dados resumidos da estação telemétrica para o período selecionado.
        Será permitido um período máximo de 10 dias consecutivos

    Args:
        token_auth (TokenAuthHandler): Objeto da classe TokenAuthHandler
        codigoestacao (int): Código da estação
        data_inicial (str): Data no formato YYYY-MM-DD
        data_final (str): Data no formato YYYY-MM-DD
        intervalo_busca (IntervaloDeBusca, optional): Intervalos definidos na API (5min até 24h).
            Defaults to "HORA_24".

    Raises:
        TimeSerieNotFoundError: Erro lançado caso a série histórica não seja encontrada

    Returns:
        list[DadoTelemetricaAdotada]: Lista de dados da estação telemétrica adotada
        no formato de modelo Pydantic - classe DadoTelemetricaAdotada
    """
    dados_telemetrica = retorna_serie_historica_telemetrica(
        token_auth,
        codigoestacao,
        "Adotada",
        "DATA_LEITURA",
        data_inicial,
        data_final,
        intervalo_busca,
    )

    if not dados_telemetrica:
        raise TimeSerieNotFoundError(
            f"Série histórica telemétrica adotada não encontrada para o código da estação {codigoestacao}."
        )

    return [
        DadoTelemetricaAdotada.model_validate(item, by_alias=True)
        for item in dados_telemetrica
    ]


def serie_historica_telemetrica_detalhada(
    token_auth: TokenAuthHandler,
    codigoestacao: int,
    data_inicial: str,
    data_final: str,
    intervalo_busca: IntervaloDeBusca = "HORA_24",
) -> list[DadoTelemetricaDetalhada]:
    """Retorna os dados detalhados da estação telemétrica para o período selecionado.
        Será permitido um período máximo de 10 dias consecutivos

    Args:
        token_auth (TokenAuthHandler): Objeto da classe TokenAuthHandler
        codigoestacao (int): Código da estação
        data_inicial (str): Data no formato YYYY-MM-DD
        data_final (str): Data no formato YYYY-MM-DD
        intervalo_busca (IntervaloDeBusca, optional): Intervalos definidos na API (5min até 24h).
            Defaults to "HORA_24".

    Raises:
        TimeSerieNotFoundError: Erro lançado caso a série histórica não seja encontrada

    Returns:
        list[DadoTelemetricaAdotada]: Lista de dados da estação telemétrica adotada
        no formato de modelo Pydantic - classe DadoTelemetricaAdotada
    """
    dados_telemetrica = retorna_serie_historica_telemetrica(
        token_auth,
        codigoestacao,
        "Detalhada",
        "DATA_LEITURA",
        data_inicial,
        data_final,
        intervalo_busca,
    )

    if not dados_telemetrica:
        raise TimeSerieNotFoundError(
            f"Série histórica telemétrica adotada não encontrada para o código da estação {codigoestacao}."
        )

    return [
        DadoTelemetricaDetalhada.model_validate(item, by_alias=True)
        for item in dados_telemetrica
    ]
