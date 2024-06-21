import reflex as rx
from app.styles.styles import EmSize


def FloatButton() -> rx.Component:
    return  rx.flex(
                rx.hover_card.root(
                    rx.hover_card.trigger(
                        rx.button(
                            rx.image(
                            src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg",
                            ),
                        variant="ghost",
                        width=EmSize.VERY_BIG.value,
                        )
                    ),
                    rx.hover_card.content(
                        rx.link(
                            rx.text(
                                "Para regresar a mi página web,", 
                            rx.text.em("haz clic aquí",
                                        color="blue"
                                        )),
                        href="https://keniernn-devknns-projects.vercel.app/")
                    ),
                        margin_bottom=EmSize.BIG.value,
                ),
                width="95%",
                justify="end",
                align="end",
                position="fixed",
               # z_index="555"
            )