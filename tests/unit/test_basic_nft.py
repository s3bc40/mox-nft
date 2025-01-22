import boa
from src import basic_nft

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"
NAME = "Puppy NFT"
SYMBOL = "PNFT"


def test_init_nft(default_account):
    # Arrange/Act
    nft_contract = basic_nft.deploy()

    # Assert
    assert nft_contract.name() == NAME
    assert nft_contract.symbol() == SYMBOL
    assert nft_contract.owner() == default_account.address


def test_mint_nft_fail_empty_address(nft_contract, pug_uri):
    # Arrange/Act/Assert
    with boa.reverts("erc721: mint to the zero address"):
        with boa.env.prank(ZERO_ADDRESS):
            nft_contract.mint(pug_uri)


def test_nfts_minted(
    default_account, deployed_contract_with_nfts, pug_uri, bernard_uri
):
    # Arrange/Act/Assert
    assert (
        deployed_contract_with_nfts.tokenURI(0)
        == f"{deployed_contract_with_nfts.BASE_URI()}{pug_uri}"
    )
    assert (
        deployed_contract_with_nfts.tokenURI(1)
        == f"{deployed_contract_with_nfts.BASE_URI()}{bernard_uri}"
    )
