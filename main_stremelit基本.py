##ライブラリのインポート################################################################
import streamlit as st
import numpy as np  #数値処理のライブラリ
import pandas as pd  #データ処理のライブラリ
from PIL import Image #画像を扱うライブラリ
####################################################################################
st.title('streamlit 超入門')#アプリケーションのタイトルを設定#ターミナルかコマンドラインで現在の作業フォルダに移動してstreamlit run main.pyとすればブラウザで確認できる
st.write("DataFrame")#テキストを追加

###pandasライブラリーを使用して表作成##################################################
df = pd.DataFrame({'１列目':[1,2,3,4],'2列目':[10,20,30,40]}) 
###表の描写の種類
st.write(df) #writeでも描画できるが、引数を指定できない
st.dataframe(df, width=300, height=300)#dataframeを使うと引数を指定して、サイズを指定した描画ができる
st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)#pandasのstyleを指定して列方向で最大値にハイライトをつけて描写させる例
st.table(df.style.highlight_max(axis=0))#tableを使うと静的（ソートできない）な表を描写

##マジックコマンドを使って描写～##マークダウン=見出しを描写（ダブルウォーテーション３つ）################
"""
# 章
## 節
### 項

```python   #マジックコマンドを使って描写～##pythonコードをそのまま描写させる（バッククォーテーション３つ）
import streamlit as st
import numpy as np
import pandas as pd
```
"""
#折れ線グラフを作成########################################################################
df = pd.DataFrame(np.random.rand(20,3),columns=['a','b','c'])#abcというカラム（列）を指定/numpyのnp.random.rand()を使って乱数（正規表現）を使って縦20-横3の行列を作る
st.line_chart(df)#折れ線グラフを描写
st.area_chart(df)#塗りつぶしありの折れ線グラフを描写
st.bar_chart(df)#棒グラフを描写

#マップを作成########################################################################
df = pd.DataFrame(np.random.rand(100,2)/[50,50]+[35.69,139.70],columns=['lat','lon'])#lat/lonというカラム（列）を指定/numpyのnp.random.rand()を使って乱数（正規表現）を発生させそれをそれぞれ50で割る
st.map(df)#マップを描写

#画像を表示########################################################################
st.write('Display Image')
img = Image.open('sample.png')#Imageライブラリを使って画像を読み込む。作業ファイルと同じ階層だったら画像名だけ指定すればよい
st.image(img,caption='サンプル画像',use_column_width=True)#画像を描写（キャプションつき）、use_colum_withをtrueにするとWebページのカラム（列）の横幅のレイアウトに合わせて拡大縮小される

#インタラクティブなウィジェットを作成########################################################################
#チェックボックス
if st.checkbox('Show Image'): #チェックボックス（True/Falseを返す）を表示。もしTrueなら以下の処理を実行させる
    img = Image.open('sample.png')#Imageライブラリを使って画像を読み込む。作業ファイルと同じ階層だったら画像名だけ指定すればよい
    st.image(img,caption='サンプル画像',use_column_width=True)
    
#セレクトボタン    
option = st.selectbox('あなたが好きな数字を教えてください',list(range(1,11)))#range()で1～10の整数を発生させ、それをリスト化する
'あなたの好きな数字は、', option,'です'#st.write()を使わなくてもこれだけで文字を描写できる

#テキスト入力
text = st.text_input('あなたの趣味を教えてください')#st,text_inputでテキストボックスを表示
'あなたの趣味：', text,'です'

#スライダー
condition = st.slider('あなたの今の調子は？',0,100,50)#st.sliderでスライダーを表示(最小値,最大値,最初の値)
'コンディション：', condition

