# IBM Watson Personality Insights 向けに Twitter ログ（.csv）を整形する
Utility tool for IBM Watson Personality Insights

2017年8月14日 Yoshiki Hayama @storywriter

## 使いかた

前提: Python がインストールされていること。（Python 2.7.10 で動作確認）

1. Twitter から、全ツイート履歴をダウンロードする。
2. 全ツイート履歴を解凍したフォルダに tweets_csv_to_json.py を入れる。
3. コマンドラインで、解凍したフォルダに移動し、 python tweets_csv_to_json.py と入力する。
4. プログラムが tweets.csv を読み込んで整形し、 tweet_all.json というファイルを生成する。
5. 生成された tweet_all.json が IBM Watson Personality Insights 向けの JSON ファイルです。cURL で Personality Insights に送ると、分析結果が得られます。

## 参考

IBM Watson Personality Insights:
https://www.ibm.com/watson/services/personality-insights/

## 備考

- Twitter からダウンロードできる全ツイート履歴は、数年より前のデータでは、投稿時間が記録されていない。
