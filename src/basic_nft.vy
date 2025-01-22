# pragma version 0.4.0
"""
@license MIT
@title Puppy NFT
"""

from snekmate.auth import ownable
initializes: ownable

from snekmate.tokens import erc721
initializes: erc721[ownable := ownable]


exports: (
    erc721.__interface__
)
################################################################
#                       STATE VARIABLES                        #
################################################################
NAME: constant(String[25]) = "Puppy NFT"
SYMBOL: constant(String[5]) = "PNFT"
BASE_URI: public(constant(String[7])) = "ipfs://"
EIP_712_NAME: constant(String[50]) = "CyfrinUpdraft NFT"
EIP_712_VERSION: constant(String[1]) = "1"


################################################################
#                          FUNCTIONS                           #
################################################################
@deploy
def __init__():
    ownable.__init__()
    erc721.__init__(NAME, SYMBOL, BASE_URI, EIP_712_NAME, EIP_712_VERSION)


@external
def mint(uri: String[432]):
    token_id: uint256 = erc721._counter
    erc721._counter = token_id + 1
    erc721._safe_mint(msg.sender, token_id, b"")
    erc721._set_token_uri(token_id, uri)
    
