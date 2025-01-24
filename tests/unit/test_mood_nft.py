import boa
from moccasin.boa_tools import VyperContract
from src import mood_nft

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"
RANDOM_USER = boa.env.generate_address("randome_user")

NAME: str = "Mood NFT"
SYMBOL: str = "MNFT"
LAPPY_SVG_URI = "data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjAwIDIwMCIgd2lkdGg9IjQwMCIgIGhlaWdodD0iNDAwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjEwMCIgZmlsbD0ieWVsbG93IiByPSI3OCIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIzIi8-CiAgPGcgY2xhc3M9ImV5ZXMiPgogICAgPGNpcmNsZSBjeD0iNzAiIGN5PSI4MiIgcj0iMTIiLz4KICAgIDxjaXJjbGUgY3g9IjEyNyIgY3k9IjgyIiByPSIxMiIvPgogIDwvZz4KICA8cGF0aCBkPSJtMTM2LjgxIDExNi41M2MuNjkgMjYuMTctNjQuMTEgNDItODEuNTItLjczIiBzdHlsZT0iZmlsbDpub25lOyBzdHJva2U6IGJsYWNrOyBzdHJva2Utd2lkdGg6IDM7Ii8-Cjwvc3ZnPg=="
HAPPY_SVG_URI = "data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjAwIDIwMCIgd2lkdGg9IjQwMCIgIGhlaWdodD0iNDAwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjEwMCIgZmlsbD0ieWVsbG93IiByPSI3OCIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIzIi8+CiAgPGcgY2xhc3M9ImV5ZXMiPgogICAgPGNpcmNsZSBjeD0iNzAiIGN5PSI4MiIgcj0iMTIiLz4KICAgIDxjaXJjbGUgY3g9IjEyNyIgY3k9IjgyIiByPSIxMiIvPgogIDwvZz4KICA8cGF0aCBkPSJtMTM2LjgxIDExNi41M2MuNjkgMjYuMTctNjQuMTEgNDItODEuNTItLjczIiBzdHlsZT0iZmlsbDpub25lOyBzdHJva2U6IGJsYWNrOyBzdHJva2Utd2lkdGg6IDM7Ii8+Cjwvc3ZnPg=="
SAD_SVG_URI = "data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjAwIDIwMCIgd2lkdGg9IjQwMCIgaGVpZ2h0PSI0MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiBmaWxsPSJ5ZWxsb3ciIHI9Ijc4IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjMiLz4KICA8ZyBjbGFzcz0iZXllcyI+CiAgICA8Y2lyY2xlIGN4PSI3MCIgY3k9IjgyIiByPSIxMiIvPgogICAgPGNpcmNsZSBjeD0iMTI3IiBjeT0iODIiIHI9IjEyIi8+CiAgPC9nPgogIDxwYXRoIGQ9Ik01NSAxNDBjMTcuNDEtNDIuNzMgODIuMjEtMjYuOSA4MS41Mi0uNzMiIHN0eWxlPSJmaWxsOm5vbmU7IHN0cm9rZTogYmxhY2s7IHN0cm9rZS13aWR0aDogMzsiLz4KPC9zdmc+"
HAPPY_SVG_TOKEN_URI = "data:application/json;base64,eyJuYW1lIjoiTW9vZCBORlQiLCAiZGVzY3JpcHRpb24iOiJBbiBORlQgdGhhdCByZWZsZWN0cyB0aGUgbW9vZCBvZiB0aGUgb3duZXIsIDEwMCUgb24gQ2hhaW4hIiwgImF0dHJpYnV0ZXMiOiBbeyJ0cmFpdF90eXBlIjogIm1vb2RpbmVzcyIsICJ2YWx1ZSI6IDEwMH1dLCAiaW1hZ2UiOiJkYXRhOmltYWdlL3N2Zyt4bWw7YmFzZTY0LFBITjJaeUIyYVdWM1FtOTRQU0l3SURBZ01qQXdJREl3TUNJZ2QybGtkR2c5SWpRd01DSWdJR2hsYVdkb2REMGlOREF3SWlCNGJXeHVjejBpYUhSMGNEb3ZMM2QzZHk1M015NXZjbWN2TWpBd01DOXpkbWNpUGdvZ0lEeGphWEpqYkdVZ1kzZzlJakV3TUNJZ1kzazlJakV3TUNJZ1ptbHNiRDBpZVdWc2JHOTNJaUJ5UFNJM09DSWdjM1J5YjJ0bFBTSmliR0ZqYXlJZ2MzUnliMnRsTFhkcFpIUm9QU0l6SWk4K0NpQWdQR2NnWTJ4aGMzTTlJbVY1WlhNaVBnb2dJQ0FnUEdOcGNtTnNaU0JqZUQwaU56QWlJR041UFNJNE1pSWdjajBpTVRJaUx6NEtJQ0FnSUR4amFYSmpiR1VnWTNnOUlqRXlOeUlnWTNrOUlqZ3lJaUJ5UFNJeE1pSXZQZ29nSUR3dlp6NEtJQ0E4Y0dGMGFDQmtQU0p0TVRNMkxqZ3hJREV4Tmk0MU0yTXVOamtnTWpZdU1UY3ROalF1TVRFZ05ESXRPREV1TlRJdExqY3pJaUJ6ZEhsc1pUMGlabWxzYkRwdWIyNWxPeUJ6ZEhKdmEyVTZJR0pzWVdOck95QnpkSEp2YTJVdGQybGtkR2c2SURNN0lpOCtDand2YzNablBnPT0ifQ=="
SAD_SVG_TOKEN_URI = "data:application/json;base64,eyJuYW1lIjoiTW9vZCBORlQiLCAiZGVzY3JpcHRpb24iOiJBbiBORlQgdGhhdCByZWZsZWN0cyB0aGUgbW9vZCBvZiB0aGUgb3duZXIsIDEwMCUgb24gQ2hhaW4hIiwgImF0dHJpYnV0ZXMiOiBbeyJ0cmFpdF90eXBlIjogIm1vb2RpbmVzcyIsICJ2YWx1ZSI6IDEwMH1dLCAiaW1hZ2UiOiJkYXRhOmltYWdlL3N2Zyt4bWw7YmFzZTY0LFBITjJaeUIyYVdWM1FtOTRQU0l3SURBZ01qQXdJREl3TUNJZ2QybGtkR2c5SWpRd01DSWdhR1ZwWjJoMFBTSTBNREFpSUhodGJHNXpQU0pvZEhSd09pOHZkM2QzTG5jekxtOXlaeTh5TURBd0wzTjJaeUkrQ2lBZ1BHTnBjbU5zWlNCamVEMGlNVEF3SWlCamVUMGlNVEF3SWlCbWFXeHNQU0o1Wld4c2IzY2lJSEk5SWpjNElpQnpkSEp2YTJVOUltSnNZV05ySWlCemRISnZhMlV0ZDJsa2RHZzlJak1pTHo0S0lDQThaeUJqYkdGemN6MGlaWGxsY3lJK0NpQWdJQ0E4WTJseVkyeGxJR040UFNJM01DSWdZM2s5SWpneUlpQnlQU0l4TWlJdlBnb2dJQ0FnUEdOcGNtTnNaU0JqZUQwaU1USTNJaUJqZVQwaU9ESWlJSEk5SWpFeUlpOCtDaUFnUEM5blBnb2dJRHh3WVhSb0lHUTlJazAxTlNBeE5EQmpNVGN1TkRFdE5ESXVOek1nT0RJdU1qRXRNall1T1NBNE1TNDFNaTB1TnpNaUlITjBlV3hsUFNKbWFXeHNPbTV2Ym1VN0lITjBjbTlyWlRvZ1lteGhZMnM3SUhOMGNtOXJaUzEzYVdSMGFEb2dNenNpTHo0S1BDOXpkbWMrIn0="


################################################################
#                           MOOD NFT                           #
################################################################
def test_mood_nft_init(default_account, happy_svg_uri, sad_svg_uri):
    # Arrange/Act
    mood_contract: VyperContract = mood_nft.deploy(happy_svg_uri, sad_svg_uri)

    # Assert
    assert mood_contract.HAPPY_SVG_URI() == happy_svg_uri
    assert mood_contract.SAD_SVG_URI() == sad_svg_uri
    assert mood_contract.owner() == default_account.address
    assert mood_contract.name() == NAME
    assert mood_contract.symbol() == SYMBOL


def test_mood_nft_mint_fail_empty_address(mood_nft_contract):
    # Arrange/Act/Assert
    with boa.reverts("erc721: mint to the zero address"):
        with boa.env.prank(ZERO_ADDRESS):
            mood_nft_contract.mint_nft()


def test_mood_nft_mint(mood_nft_contract):
    # Arrange/Act
    mood_nft_contract.mint_nft()

    # Assert
    assert mood_nft_contract.tokenURI(0) == HAPPY_SVG_TOKEN_URI
    assert mood_nft_contract.token_id_to_mood(0) == 1
    assert mood_nft_contract.get_counter() == 1


def test_mood_nft_svg_to_uri(mood_nft_contract, happy_svg_uri, sad_svg_uri):
    # Arrange
    happy_svg = ""
    sad_svg = ""
    with open("img/happy.svg", "r") as f:
        happy_svg = f.read()
    with open("img/sad.svg", "r") as f:
        sad_svg = f.read()

    # Act/Assert
    assert mood_nft_contract.svg_to_uri(happy_svg) == HAPPY_SVG_URI
    assert mood_nft_contract.svg_to_uri(sad_svg) == SAD_SVG_URI


def test_mood_nft_flip_mood_fail_not_owner_or_approved(deployed_contract_with_nft):
    # Arrange/Act/Assert
    with boa.env.prank(RANDOM_USER):
        with boa.reverts("mood nft: Not owner or approved user"):
            deployed_contract_with_nft.flip_mood(0)


def test_mood_nft_flip_mood_should_be_happy(deployed_contract_with_nft):
    # Arrange/Act
    deployed_contract_with_nft.flip_mood(0)

    # Assert
    assert deployed_contract_with_nft.tokenURI(0) == SAD_SVG_TOKEN_URI
    assert deployed_contract_with_nft.token_id_to_mood(0) == 2
    assert deployed_contract_with_nft.get_counter() == 1


def test_mood_nft_flip_mood_should_be_sad(deployed_contract_with_nft):
    # Arrange/Act
    deployed_contract_with_nft.flip_mood(0)
    deployed_contract_with_nft.flip_mood(0)

    # Assert
    assert deployed_contract_with_nft.tokenURI(0) == HAPPY_SVG_TOKEN_URI
    assert deployed_contract_with_nft.token_id_to_mood(0) == 1
    assert deployed_contract_with_nft.get_counter() == 1


################################################################
#                            ERC721                            #
################################################################
def test_mood_erc721_owner_of_wrong_token_id(deployed_contract_with_nft):
    # Arrange/Act/Assert
    with boa.reverts("erc721: invalid token ID"):
        deployed_contract_with_nft.ownerOf(1)


def test_mood_erc721_owner_of(deployed_contract_with_nft):
    # Arrange/Act
    deployed_contract_with_nft.ownerOf(0)

    # Assert
    assert deployed_contract_with_nft.ownerOf(0) == deployed_contract_with_nft.owner()


def test_mood_erc721_approve_fail_on_owner(deployed_contract_with_nft):
    # Arrange/Act/Assert
    with boa.reverts("erc721: approval to current owner"):
        deployed_contract_with_nft.approve(deployed_contract_with_nft.owner(), 0)


def test_mood_erc721_approve(deployed_contract_with_nft):
    # Arrange/Act
    deployed_contract_with_nft.approve(RANDOM_USER, 0)

    # Assert
    assert deployed_contract_with_nft.getApproved(0) == RANDOM_USER


def test_mood_erc721_get_approved_wrong_token_id(deployed_contract_with_nft):
    # Arrange/Act/Assert
    with boa.reverts("erc721: invalid token ID"):
        deployed_contract_with_nft.getApproved(1)


def test_mood_erc721_token_by_index_out_of_bounds(deployed_contract_with_nft):
    # Arrange/Act/Assert
    with boa.reverts("erc721: global index out of bounds"):
        deployed_contract_with_nft.tokenByIndex(2)


def test_mood_erc721_token_by_index(deployed_contract_with_nft):
    # Arrange/Act
    token_id: int = deployed_contract_with_nft.tokenByIndex(0)

    # Assert
    assert token_id == 0


################################################################
#                           OWNABLE                            #
################################################################
def test_mood_ownable_transfer_ownership_fail_not_owner(mood_nft_contract):
    # Arrange/Act/Assert
    with boa.reverts("ownable: caller is not the owner"):
        with boa.env.prank(RANDOM_USER):
            mood_nft_contract.transfer_ownership(RANDOM_USER)


def test_mood_ownable_transfer_ownership_fail_zero_address(mood_nft_contract):
    # Arrange/Act/Assert
    with boa.reverts("erc721: new owner is the zero address"):
        mood_nft_contract.transfer_ownership(ZERO_ADDRESS)


def test_mood_ownable_transfer_ownership(mood_nft_contract):
    # Arrange
    previous_owner = mood_nft_contract.owner()

    # Act
    mood_nft_contract.transfer_ownership(RANDOM_USER)

    # Assert
    logs = mood_nft_contract.get_logs()
    log_previous_owner = logs[1].topics[0]
    log_new_owner = logs[1].topics[1]

    assert log_previous_owner == previous_owner
    assert log_new_owner == RANDOM_USER
    assert mood_nft_contract.owner() == RANDOM_USER


def test_mood_ownable_renounce_ownership(mood_nft_contract):
    # Arrange/Act
    mood_nft_contract.renounce_ownership()

    # Assert
    assert mood_nft_contract.owner() == ZERO_ADDRESS
