import reflex as rx 
import app.constants as const
from app.styles import styles
from app.styles.styles import EmSize, Size
from app.components.nav_bar import barraNav
from app.components.float_button import FloatButton
from app.states.state import State



def index() -> rx.Component:
    return rx.box(
         #rx.color_mode.button(position="bottom-left"),
         barraNav(),
         rx.center(
             rx.flex(
                 rx.grid(
                     rx.box(
                        rx.text_area(
                            placeholder="Ingrese el texto aqui...",
                            height=EmSize.VERY_VERY_BIG.value,
                            max_length=200,
                            value=State.textoIngresado,
                            on_change=State.set_textoIngresado
                            ),
                        align_self="center",
                        ),                     
                     rx.flex(
                         rx.icon(   
                             "shield-alert",
                             align_self="center",
                             color="orange",
                             size=18
                            ),
                         rx.text(
                            "Solo letras minúsculas y sin acentos",
                             size=Size.VERY_SMALL.value
                            ),
                        margin_top=EmSize.DEFAULT.value,
                        padding_left=EmSize.LARGE_SMALL.value,
                        align_self="end",
                        spacing=Size.SMALL.value,
                        margin_bottom=EmSize.DEFAULT.value
                        ),
                     rx.flex(
                         rx.button("Encriptar",
                                   width="40%",
                                   variant="soft",
                                   on_click=State.encriptador
                                   ),
                         rx.button("Desencriptar",
                                   width="40%",
                                   disabled=False,
                                   variant="soft",
                                   on_click=State.desencriptador
                                   ),
                         justify="center",
                         spacing=Size.SMALL.value,
                         width="100%"
                     ),
                     margin=EmSize.DEFAULT.value,
                     width="90%",
                     height="100%"
                 ),
                 
                 # La otra mitad
                 rx.box(
                    rx.cond(
                        State.ocultarInfo,
                        rx.image(
                            src=const.imagen_1, 
                            display=["none","none","flex"]
                            ),
                        None #No muestra nada cuando la condicion es verdadera
                        ),
                    rx.cond(
                        State.ocultarInfo,
                        rx.center(
                        
                        rx.chakra.circular_progress(
                            rx.chakra.circular_progress_label(
                                "∞", color="rgb(107,99,246)"
                                 ),
                        is_indeterminate=True,
                        display=["flex","flex","none"],
                        size=Size.BIG.value,
                        margin_bottom=EmSize.DEFAULT.value
                        )),
                    None           
                    ),
                    rx.cond(
                        State.ocultarInfo,
                        rx.vstack(
                            rx.text("Ningún mensaje fue encontrado"),
                            rx.text("Ingresa el texto que desees encriptar o desencriptar"),
                            text_align="center",
                            align="center"
                            ),
                        None
                        ),
                    rx.cond(
                       State.textoProcesado != "",
                            rx.text(State.textoProcesado), 
                
                    None
                    ),
                    rx.center(
                        rx.button(
                            State.textoBoton,
                                variant="soft",
                                width="40%",
                                on_click=rx.set_clipboard(State.textoProcesado),

                                ),
                        margin_top=EmSize.DEFAULT.value,

                        ),
                    justify_self="center",
                    align_self="center",
                    width="60%"
                    ),
                spacing=Size.BIG.value,
                max_width=styles.MAX_WIDTH,
                width="100%",
                height="85vh", 
                margin=EmSize.DEFAULT.value,

                flex_direction=["column","column","row"]
               ), 
            width="100%",
            margin_top=EmSize.DEFAULT.value,
            margin_bottom=EmSize.DEFAULT.value

            ),
            FloatButton(),

            rx.logo(),
         width="100%",
        )