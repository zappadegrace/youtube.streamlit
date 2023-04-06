##ライブラリのインポート################################################################
import streamlit as st
import numpy as np  #数値処理のライブラリ
import pandas as pd  #データ処理のライブラリ
from PIL import Image #画像を扱うライブラリ
import time
####################################################################################
st.title('streamlit 超入門')
st.sidebar.write('レイアウトの追加')

#テキスト入力#スライダー
text = st.sidebar.text_input('あなたの趣味を教えてください')#(.siderbarを追加するとその部分だけサイドに表示される)
condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)
'あなたの趣味：', text,'です'
'コンディション：', condition

#２カラムレイアウトとボタン
left_column, right_column = st.columns(2)#２カラム（２列）に設定
button = left_column.button('右カラムに文字を表示')#左カラムにボタンを表示(.bottonを追加するとボタンが表示される)
if button:#ボタンが押されたら(Trueなら)処理を実行
    right_column.write('ここは右カラム')#右カラムに文字を表示

#エクスパンダ―
expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ')
expander3.write('問い合わせ3の回答')

#プログレスバー    
st.write('プログレスバーの表示')
'Start!'
latest_iteration = st.empty()#.emptyで空を追加
bar = st.progress(0)#まず空のプログレスバーを用意する

for i in range(100): #０から９９までを繰り返す
    latest_iteration.text(f'Iteration{i+1}')#進行状況をテキストで表示
    bar.progress(i+1)#プログレスバーの長さを伸ばす
    time.sleep(0.1)#timeモジュールを使って0.1秒時間を止める
#このforループが終了しないと以降のプログラムにすすまない
'Done!'



