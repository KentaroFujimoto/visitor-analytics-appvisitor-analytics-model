#シートを指定
ws = ss.worksheet('出力結果')

#データを定義
data = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
]

#書き込み
for i in range(len(data)):
  ws.append_row(data[i])