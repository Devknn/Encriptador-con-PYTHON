import reflex as rx
from app.styles.styles import EmSize, Color

def barraNav() -> rx.Component:
    return rx.flex(
            rx.image(
                src="favicon.ico",
                width=EmSize.BIG.value,
                margin_right=EmSize.LARGE_SMALL.value
                ),
            rx.text("Desafío del Encriptador: ¡Protege tus Mensajes!",
                    display=["none","flex"]
                    ),
            rx.vstack(
                rx.text("Desafío del Encriptador:"),
                rx.text("¡Protege tus Mensajes!"),
                spacing="0",
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