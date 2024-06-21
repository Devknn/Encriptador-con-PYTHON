import reflex as rx
from app.styles.styles import EmSize, Color, Size
import app.constants as const
def barraNav() -> rx.Component:
    return rx.flex(
            rx.image(
                src=const.LOGO,
                width=EmSize.BIG.value,
                margin_right=EmSize.LARGE_SMALL.value
                ),
            rx.text("Desafío del Encriptador: ¡Protege tus Mensajes!",
                    display=["none","flex"]
                    ),
            rx.vstack(
                rx.text("Desafío del Encriptador:"),
                rx.text("¡Protege tus Mensajes!"),
                spacing=Size.ZERO.value,
                display=["flex","none"]
            ),
            background=Color.BARRA.value,
            width="100%",
            height=EmSize.BIG.value,
            justify="center",
            align="center",
            position="fixed",
            top=EmSize.ZERO.value,
            )