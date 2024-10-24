## WebサイトスクレイピングのためのCLIツール

### 制作目的
HPの検証時などに使用。
ディレクトリマップと比較しページの抜け漏れがないかの調査や、URLの間違い・ページタイトルの間違いがないかを確認するためのツール。

### 実行環境

Python 3.11.9

・requests
・bs4
・csv

#セットアップ

```
# pip install requests bs4
```

### 動作手順
pythonファイル実行

```
python3 scr.py
```
↓
```
TOPページのURLを入力してください
>> https://~~~~~~.com
```

```
CSVファイルの名前を入力してください
>> ~~.csv
```

> 拡張子(.csv)もつけて記入

入力が完了するとスクレイピングが始まります。
スクレイピングが終わると、scr.pyが格納されているディレクトリの中にcsvファイルが作成されます。

unotame.csvは 'https://unotame.com'をスクレイピングした時のサンプルデータです。
タイトル・URLの一覧をヘッダー付きでスクレイピングします。