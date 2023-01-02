# サンプルスクリプト12

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Title', width=640, height=480)

with dpg.window(label="TableSample01"):
    # テーブル追加
    with dpg.table(header_row=True, borders_innerH=True, borders_innerV=True):
        # 列の設定
        dpg.add_table_column(label="Column1")
        dpg.add_table_column(label="Column2")
        dpg.add_table_column(label="Column3")
        for i in range(0, 5):
            # 行の追加            
            with dpg.table_row():
                dpg.add_text(f"Row{i} Column1")  #左から順番に
                dpg.add_text(f"Row{i} Column2")
                dpg.add_text(f"Row{i} Column3")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
