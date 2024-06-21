"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from app.states.state import State
from app.styles import styles
from app.pages.index import index






app = rx.App(
    style=styles.BASE_STYLE,
    theme=rx.theme(
        accent_color="green",
        radius="medium",
        )
    )
app.add_page(index, on_load=State.on_load)
