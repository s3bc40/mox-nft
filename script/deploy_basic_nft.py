from moccasin.boa_tools import VyperContract
from src import basic_nft

PUG_URI = "QmW16U98JrY9HBY36rQtUuUtDnm6LdEeNdAAggmrx3thMa"
ST_BERNARD_URI = "QmbGh8w1ENpAx58dDQeKvDKM3AfdsnkV9cXrR1SzfDx5sH"


def deploy_basic_nft() -> VyperContract:
    contract: VyperContract = basic_nft.deploy()
    contract.mint(PUG_URI)
    token_uri_pug = contract.tokenURI(0)
    print(token_uri_pug)
    contract.mint(ST_BERNARD_URI)
    token_uri_bernard = contract.tokenURI(1)
    print(token_uri_bernard)

    return contract


def moccasin_main() -> VyperContract:
    return deploy_basic_nft()
