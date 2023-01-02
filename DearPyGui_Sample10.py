# サンプルスクリプト10

import os
import dearpygui.dearpygui as dpg
import easygui as eg
import numpy as np
import cv2

# 実行するpyファイルのあるディレクトリ名の取得
DIR = os.path.dirname(__file__)

# DearPyGuiのアイテ「x」がすでにある場合は削除する関数
delItemIfExist = lambda x: dpg.delete_item(x) if dpg.does_item_exist(x) else ""

# 画像をRGBA形式で開く関数
imread_rgba = lambda x : cv2.cvtColor(cv2.imread(x), cv2.COLOR_BGR2RGBA)

# 画像ファイルをテクスチャーレジストリに登録し、描画する関数
def draw_image_opencv(img, tag_texture_registry, parent=None):
    h, w, ch = img.shape
    if ch != 4:
        return
    delItemIfExist("txtr_for_this_func")
    delItemIfExist("img_for_this_func")
    dpg.add_static_texture(w, h, img/255, parent=tag_texture_registry, tag="txtr_for_this_func")
    if parent is None:
        return dpg.add_image("txtr_for_this_func", tag ="img_for_this_func", width=w, height=h)
    else:
        return dpg.add_image("txtr_for_this_func", parent=parent, tag ="img_for_this_func", width=w, height=h)

# ボタンを押した時のコールバック
def button_callback(sender, app_data, user_data):
    fname = eg.fileopenbox()
    img = imread_rgba(fname)
    draw_image_opencv(img, "texture_registry_01", parent="window2")
 
# 以下、DearPyGuiの基本構成 
dpg.create_context()
dpg.create_viewport(title='Title', width=600, height=600)

# テクスチャーレジストリの作成
with dpg.texture_registry(tag="texture_registry_01"):
    pass

# window01の作成
with dpg.window(label="window01"):
    dpg.add_button(label="file open", callback=button_callback)

# windows02の作成（Default.pngを読み込みます）
with dpg.window(label="window02", pos=(100,0), width=400, height=400, tag="window2", horizontal_scrollbar=True):
    fname = DIR + "/Default.png"
    img = imread_rgba(fname)
    draw_image_opencv(img, "texture_registry_01")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
