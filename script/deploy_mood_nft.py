import base64
from moccasin.boa_tools import VyperContract
from src import mood_nft


def deploy_mood_nft() -> VyperContract:
    happy_svg_uri = ""
    sad_svg_uri = ""
    with open("img/happy.svg", "r") as f:
        happy_svg = f.read()
        happy_svg_uri = svg_to_base64_uri(happy_svg)
        print(happy_svg_uri)
    with open("img/sad.svg", "r") as f:
        sad_svg = f.read()
        sad_svg_uri = svg_to_base64_uri(sad_svg)
        print(sad_svg_uri)

    mood_nft.deploy(happy_svg_uri, sad_svg_uri)


def moccasin_main() -> VyperContract:
    return deploy_mood_nft()


def svg_to_base64_uri(svg: str) -> str:
    svg_bytes = svg.encode("utf-8")
    base64_svg = base64.b64encode(svg_bytes).decode("utf-8")
    return f"data:image/svg+xml;base64,{base64_svg}"
