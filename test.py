# =============================================================================
#  Script de teste para Waveshare ESP32-S3-Touch-LCD-4.3
#  (lvgl_micropython com o TOML my_boards/ws-esp32-s3-touch-lcd-4-3.toml)
#
#  O módulo "display" é gerado automaticamente pelo make.py a partir do TOML.
#  Ele: inicializa o LVGL, cria o RGBBus, o I2C, o CH422G, o driver RGBDisplay
#  (ST7262), o GT911 e arranca o TaskHandler. Não precisas de importar
#  rgb_display, task_handler ou st7701 directamente — "display" já faz tudo.
# =============================================================================

# 1) O GT911 precisa de ter o GPIO4 (INT) a 0 no flanco de subida do seu reset
#    para fixar o endereço I2C 0x5D. O "import display" não faz isto, por isso
#    é necessário este passo ANTES de importar display.
import machine
machine.Pin(4, machine.Pin.OUT, value=0)

# 2) Importar o módulo "display" congelado no firmware. Este módulo:
#    - lv.init()
#    - cria E instantiationa o RGBDisplay (reset, power, backlight, init)
#    - cria e regista o GT911 como indev touch
#    - cria e arranca o TaskHandler (timer que chama lv.task_handler)
import display  # NOQA: E402

import lvgl as lv

print("Display RGB instanciado com sucesso!")

# 3) Criar elementos LVGL — o display já está registado em lv.display_get_default()
scr = lv.screen_active()
btn = lv.button(scr)
btn.set_size(250, 100)
btn.center()

label = lv.label(btn)
label.set_text("Funciona!")
label.center()

# Forçar uma atualização imediata (o TaskHandler já estava a correr, mas esta
# chamada garante que o écrã é atualizado agora)
lv.refr_now(lv.display_get_default())

print("Tudo pronto!")