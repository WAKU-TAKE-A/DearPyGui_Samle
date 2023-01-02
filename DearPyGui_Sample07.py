# サンプルスクリプト7

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)

# コールバック関数
def click_text(sender, app_data):
    print(f"sender is: {sender}")
    print(f"app_data is: {app_data}")

# アイテムハンドラーレジストリ「text1_handler_registry」に、アイテムハンドラー（例はクリック監視）を追加します。
with dpg.item_handler_registry(tag="text1_handler_registry"):
    dpg.add_item_clicked_handler(callback=click_text)

# ウィンドウに「text1」を追加します。
with dpg.window(width=250, height=200):
    dpg.add_text("click me", tag="text1")

# アイテムとアイテムハンドラーレジストリを紐づけます。
dpg.bind_item_handler_registry("text1", "text1_handler_registry")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
