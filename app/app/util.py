import reflex as rx 
import app.constants as const


def lang()->rx.Component:
    return rx.script("document.documentElement.lang='es'")

#comun
preview = const.LOGO
_meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@keniernn"}
    ]

#Index
index_title = "KenierN | Encriptador"
index_description = "Desafío del Encriptador: ¡Protege tus Mensajes!"
index_meta = [
                {"name": "og:title", "content": "KenierN | Encriptador"},
                {"name": "og:description", "content":  "Desafío del Encriptador: ¡Protege tus Mensajes!"},   
            ]
index_meta.extend(_meta)