# jupyter notebookで画像を横に並べて描画する
入力画像に対して、グレースケール化、二値化、エッジ検出、結果、ヒストグラムなどを横一列に並べて表示したい時に使用する

## 使用方法
Debug.pyが本体  
Debug.pyをディレクトリに突っ込む
```
# 初期化など
import Debug
debug = Debug.debug()
debug.initialize()

# 描画
debug.draw(img, 'img_name')
debug.plot(graph, 'graph_name')
```

## もう少し詳しい説明
```
debug = Debug.debug(True_or_False, size, num)
### True_or_False: Falseを選ぶと描画されなくなる（デフォルトTrue）
### size: 全図を描画する面積(x, y)、デフォルト(20, 15)
### num: 一列に並べる図の数、この数以上だとエラーがでる、デフォルト10
```
```
debug.SetWholeSize(size)
debug.SetSubNum(num)
### 後から、sizeとnumを変更するための関数
```
```
debug.Initialize()
### 描画ウィンドウなどを作成する。for文のはじめとかに宣言すると吉（サンプルコード参考）
```
```
debug.draw(image, name, cmap='gray')
### image: 画像データ
### name: 画像の名前
### cmap: cmapにある値を設定。デフォルトはgray
```
```
debug.plot(graph, name)
### image: グラフデータ
### name: グラフの名前
```


## 使用例
example.ipynbを実行する

![res](https://user-images.githubusercontent.com/39123031/76051284-a591d400-5fad-11ea-948a-271a0501ce55.PNG)
