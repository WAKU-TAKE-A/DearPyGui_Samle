# サンプルスクリプト6

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)

# コールバック関数
def mouse_click(sender, app_data):
    print(f"sender is: {sender}")
    print(f"app_data is: {app_data}")

# ハンドラーレジストリ「handler_registry1」に、グローバルハンドラー（例はクリック監視）を追加します。
with dpg.handler_registry():
    dpg.add_mouse_click_handler(callback=mouse_click)

# ウィンドウに「text1」を追加します。
with dpg.window(width=250, height=200):
    dpg.add_text("click!", tag="text1")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
