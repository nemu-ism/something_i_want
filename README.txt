未来科学部情報メディア学科3年次後期　Web情報システム演習最終課題

概要：ターミナルからYaHooショッピングの商品検索を行えるPythonプログラムです
	キーワード、価格帯、検索ヒット数等による絞り込みや、価格、平均評価等による昇・降順ソートに対応しています

使い方：
	ターミナル上でsmw.pythonに続けて検索条件を追記することでYaHooショッピングから商品検索の結果を取得・表示することができます。

検索条件一覧：								※順不同
	query:'検索したいワード'						※必須
	sort:'ｰ(降順)/+(昇順)適応したいソート'
		　利用できるソート一覧：price(価格)
						　 score(おすすめ度/default)
	condition:'all(default)/new/used'
	price_from:'最低価格(default->0)'
	price_to:'最高価格(default->99999999)'
	offset:'表示する結果の開始位置(default->1)'

使用例(Windows):
	python smw.py query:初音ミク condition:new price_from:5000 price_to:30000

結果例(Windows):
	----------------------------------------
	検索ワード： 初音ミク
	状態:new only
	価格：5,000円から30,000円まで
	5,588件中　1～10件
	----------------------------------------
	1 【送料無料】初音ミク/初音ミク「マジカルミライ 2017」 初音ミク10周年記念版 [完全生産限定][Blu-ray]
	       new 12,730円(税込) 平均評価0.00点(0人中)
	       商品ページ： https://store.shopping.yahoo.co.jp/neowing/vizl-1270.html
	2 初音ミク ハツネミク / マジカルミライ 2017 【通常盤】 (Blu-ray)  〔BLU-RAY DISC〕
	       new 5,280円(税込) 平均評価1.00点(1人中)
	       商品ページ： https://store.shopping.yahoo.co.jp/hmv/8178328.html
	3 初音ミクGTプロジェクト レーシングミク 2017 Ver. 1/1 完成品フィギュア[グッドスマイルレーシング]《０７月予約》
	       new 12,800円(税込) 平均評価5.00点(2人中)
	       商品ページ： https://store.shopping.yahoo.co.jp/amiami/figure-032680.html
	4 キャラクター・ボーカル・シリーズ01 初音ミク 初音ミク 中秋明月Ver.(予約)[グッドスマイルカンパニー]
	       new 11,392円(税込) 平均評価0.00点(0人中)
	       商品ページ： https://store.shopping.yahoo.co.jp/machichara/4580416940375.html
	5 VOCALOID（ボーカロイド・ボカロ） 初音ミク（ハツネミク） -Project DIVA- ハートハンター コスプレ衣装
	       new 11,900円(税込) 平均評価0.00点(0人中)
	       商品ページ： https://store.shopping.yahoo.co.jp/cosplaydonya/10000148.html
	6 初音ミク ハツネミク / マジカルミライ 2017 【限定盤】 (Blu-ray)  〔BLU-RAY DISC〕
	       new 8,194円(税込) 平均評価0.00点(0人中)
	       商品ページ： https://store.shopping.yahoo.co.jp/hmv/8178327.html
	7 初音ミク ハツネミク / マジカルミライ 2017 【初音ミク10周年記念盤 / 完全生産限定】 (DVD)  〔DVD〕
	       new 11,745円(税込) 平均評価0.00点(0人中)
	       商品ページ： https://store.shopping.yahoo.co.jp/hmv/8178329.html
	8 マックスファクトリー 1/ 7 初音ミク ハートハンターVer.(初音ミク -Project DIVA- F 2nd)フィギュア 返品種別B
	       new 12,880円(税込) 平均評価0.00点(0人中)
	       商品ページ： https://store.shopping.yahoo.co.jp/joshin/4545784042359-55-7771.html
	9 新作 初音 ミク（はつね ミク)風コスプレ衣装 変装  cosplay イベント パーティー コスチュームhhc088
	       new 11,781円(税込) 平均評価5.00点(1人中)
	       商品ページ： https://store.shopping.yahoo.co.jp/sakuranokoi/hhc088.html
	10 ミニカー 1/32 初音ミクGTプロジェクト グッドスマイル 初音ミク AMG 2017 シリーズ優勝Ver.[グッドスマイルレーシング]《０６月予約》
	       new 10,590円(税込) 平均評価0.00点(0人中)
	       商品ページ： https://store.shopping.yahoo.co.jp/amiami/toy-scl2-83593.html
