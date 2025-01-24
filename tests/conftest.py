import pytest
from moccasin.moccasin_account import MoccasinAccount
from moccasin.config import get_active_network
from moccasin.boa_tools import VyperContract
from script.deploy_basic_nft import deploy_basic_nft, PUG_URI, ST_BERNARD_URI
from script.deploy_mood_nft import deploy_mood_nft
from src import basic_nft, mood_nft


@pytest.fixture
def default_account() -> MoccasinAccount:
    return get_active_network().get_default_account()


################################################################
#                          BASIC NFT                           #
################################################################
@pytest.fixture
def nft_contract() -> VyperContract:
    return basic_nft.deploy()


@pytest.fixture
def deployed_contract_with_nfts() -> VyperContract:
    return deploy_basic_nft()


@pytest.fixture(scope="session")
def pug_uri() -> str:
    return PUG_URI


@pytest.fixture(scope="session")
def bernard_uri() -> str:
    return ST_BERNARD_URI


################################################################
#                           MOOD NFT                           #
################################################################
@pytest.fixture(scope="session")
def happy_svg_uri() -> str:
    return "data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjAwIDIwMCIgd2lkdGg9IjQwMCIgIGhlaWdodD0iNDAwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjEwMCIgZmlsbD0ieWVsbG93IiByPSI3OCIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIzIi8+CiAgPGcgY2xhc3M9ImV5ZXMiPgogICAgPGNpcmNsZSBjeD0iNzAiIGN5PSI4MiIgcj0iMTIiLz4KICAgIDxjaXJjbGUgY3g9IjEyNyIgY3k9IjgyIiByPSIxMiIvPgogIDwvZz4KICA8cGF0aCBkPSJtMTM2LjgxIDExNi41M2MuNjkgMjYuMTctNjQuMTEgNDItODEuNTItLjczIiBzdHlsZT0iZmlsbDpub25lOyBzdHJva2U6IGJsYWNrOyBzdHJva2Utd2lkdGg6IDM7Ii8+Cjwvc3ZnPg=="


@pytest.fixture(scope="session")
def sad_svg_uri() -> str:
    return "data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjAwIDIwMCIgd2lkdGg9IjQwMCIgaGVpZ2h0PSI0MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiBmaWxsPSJ5ZWxsb3ciIHI9Ijc4IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjMiLz4KICA8ZyBjbGFzcz0iZXllcyI+CiAgICA8Y2lyY2xlIGN4PSI3MCIgY3k9IjgyIiByPSIxMiIvPgogICAgPGNpcmNsZSBjeD0iMTI3IiBjeT0iODIiIHI9IjEyIi8+CiAgPC9nPgogIDxwYXRoIGQ9Ik01NSAxNDBjMTcuNDEtNDIuNzMgODIuMjEtMjYuOSA4MS41Mi0uNzMiIHN0eWxlPSJmaWxsOm5vbmU7IHN0cm9rZTogYmxhY2s7IHN0cm9rZS13aWR0aDogMzsiLz4KPC9zdmc+"


@pytest.fixture
def mood_nft_contract(happy_svg_uri, sad_svg_uri) -> VyperContract:
    return mood_nft.deploy(happy_svg_uri, sad_svg_uri)

@pytest.fixture
def deployed_contract_with_nft() -> VyperContract:
    return deploy_mood_nft()