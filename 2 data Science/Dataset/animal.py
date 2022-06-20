
# coding:utf-8
# CIFAR-10 是一個接近一般物體的彩色圖像資料集
# 一共包含 10 個類別的 RGB 彩色圖片
# 圖片尺寸為 32x32，共有 50000 張訓練圖片和 10000 張測試圖片
# 匯入 cifar10 模組
import cifar10
# 匯入 TensorFlow 套件，並且以 tf 別名稱呼
import tensorflow as tf

# tf.app.flags.FLAGS 是 TensorFlow 內定的一個全局變數儲存器，
# 同時可以用於指令行參數的處理，相當於 argv 的使用方式
FLAGS = tf.app.flags.FLAGS
# 在 cifar10 模組中預先定義了 f.app.flags.FLAGS.data_dir 為 CIFAR-10 的資料路徑
# 我們把這個路徑改為 cifar10_data
FLAGS.data_dir = 'cifar10_data/'

# 若果不存在資料檔，就會執行下載
cifar10.maybe_download_and_extract()