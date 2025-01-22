import pytest
from moccasin.moccasin_account import MoccasinAccount
from moccasin.config import get_active_network
from moccasin.boa_tools import VyperContract
from script.deploy_basic_nft import deploy_basic_nft, PUG_URI, ST_BERNARD_URI
from src import basic_nft


@pytest.fixture
def default_account() -> MoccasinAccount:
    return get_active_network().get_default_account()


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
