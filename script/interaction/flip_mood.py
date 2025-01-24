"""Only for Anvil deploy for learning"""

from moccasin.boa_tools import VyperContract
from moccasin.config import get_config


def flip_mood() -> VyperContract:
    active_network = get_config().get_active_network()
    mood_nft_contract = active_network.manifest_named("mood_nft")
    mood_nft_contract.flip_mood(0)
    return mood_nft_contract


def moccasin_main() -> VyperContract:
    return flip_mood()
