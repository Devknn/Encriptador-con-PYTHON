import reflex as rx
from enum import Enum
MAX_WIDTH = "1200px"

class EmSize(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE_SMALL = "1.5em"
    BIG = "3em"
    VERY_BIG = "4em"
    MEDIUM_BIG = "5em"
    VERY_VERY_BIG = "8em"


class Size(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "2"
    MEDIUM_SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    VERY_BIG = "9"
    
class Color(Enum):
    BARRA = "#1cb17f"
    
    
    
BASE_STYLE = {
    "font_family":"Roboto",
    "color":"#C3C7CB",
    "text_decoration":"none",


    rx.button: {
        "padding": Size.SMALL.value,
        "white_space": "normal",
        "text_align": "start",
        "--cursor-button": "pointer"
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}