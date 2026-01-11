# mypkg
![test](https://github.com/06nkzw15/robosys2025/actions/workflows/test.yml/badge.svg)
ロボットシステム課題2
# stdin_publisherコマンド
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布お
よび使用が許可されます．
- これはROS2のパッケージです。
- このプログラムは標準入力をそのままトピックに流すものです。
## ノード一覧
- /stdin_publisher
## トピック一覧
- /parameter_events
- /rosout
- /stdin
# 実行例
- 端末１
```
     $ ros2 topic mypkg stdin_publisher
     [INFO] [1766911068.830241415] [stdin_pubulisher]: Type something and press enter...
     hello world
```
- 端末2
```
     $ ros2 topic echo /stdin
     data: hello world
```
## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.7〜3.10
## テスト環境
- Ubuntu 24.04.3 LTS

© 2025 Taiki Nakazawa

