import asyncio
import time
import reflex as rx
class State(rx.State):
    textoIngresado: str = ""
    textoProcesado: str = ""
    ocultarInfo: bool = True
    textoBoton: str = "Copiar"
    textoCopiado: bool = False
    
    def on_load(self):
        # Restablece los valores iniciales cuando la página se carga
        self.textoIngresado = ""
        self.textoProcesado = ""
        self.ocultarInfo = True
    
    def encriptador(self):
            self.textoProcesado = self.textoIngresado.replace("e","enter").replace("i","imes").replace("a","ai").replace("o","ober").replace("u","ufat")
            self.textoIngresado = ""
            self.ocultarInfo = False
    
    def desencriptador(self):
            self.textoProcesado = self.textoIngresado.replace("enter","e").replace("imes","i").replace("ai","a").replace("ober","o").replace("ufat","u")
            self.textoIngresado = ""
            self.ocultarInfo = False
            
    async def copyText(self):
        rx.set_clipboard(self.textoProcesado)
        State.textoCopiado = True
          
        
