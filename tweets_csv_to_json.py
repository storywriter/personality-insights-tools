#! /usr/local/bin/python2.7
# coding: utf-8

# IBM Watson Personality Insights 向けに Twitter ログ（.csv）を整形する
# 2017年8月14日


import csv
import json
import time


# リツイートを分析対象から除外するか？
exclude_retweet = False



# Watson に投入する JSON データ
watson_list = []


# csv の読み込み
with open( 'tweets.csv' ) as csvfile:

  reader = csv.reader( csvfile )

  header = next( reader ) # ヘッダ行を読み飛ばす

  for row in reader:

    if exclude_retweet and row[ 6 ]: 

      pass # exclude_retweet = True なら、リツイート行は何もしない

    else:

      # UNIXタイムに変換
      row[ 3 ] = row[ 3 ].replace( ' +0000', '' ) # 次行で %z が動かないことがあるため
      row[ 3 ] = time.strptime( row[ 3 ], '%Y-%m-%d %H:%M:%S' )
      row[ 3 ] = int( time.mktime( row[ 3 ] ) )

      # JSON オブジェクトを整形
      item = {
        "content": row[ 5 ],
        "contenttype": "text/plain",
        "created": row[ 3 ],
        "id": row[ 0 ],
        "language": "ja"
      }

      # リストに追加
      watson_list.append( item )


# Watson 用のデータ形式に整形
watson_list = {
  "contentItems": watson_list
}


# 結果を JSON ファイルへ書き出す
output_file = open( 'tweet_all.json', 'w' )
json.dump( watson_list, output_file, indent = 4 )
output_file.close()
