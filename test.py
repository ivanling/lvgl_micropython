import lvgl as lv

# Inicializar o LVGL
lv.init()

# Obter o ecrã ativo atual da forma compatível com LVGL v9
scr = lv.screen_active()

# Criar um Label (Texto) no ecrã principal
label = lv.label(scr)
label.set_text("Waveshare ESP32-S3 4.3\"\nMicroPython + LVGL OK!")
label.center()

print("Interface de teste desenhada no ecrã!")