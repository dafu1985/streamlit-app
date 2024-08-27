import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# 〇title追加
st.title('Streamlit 超入門')
# 〇テキスト追加
# st.write('DataFrame')
# 〇画像の追加
st.write('Display Image')
st.sidebar.write('Interactive Widgets')
st.write('レイアウト')

st.write('プログレスバーの表示')
'Start!!'

# 〇プログレスバー
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)
    
'Done!!!!!'

# 〇チェックボックス ※チェックいれたら表示 if文の処理はタブを入れる
if st.checkbox('Show Image'):
    img = Image.open('image.jpg')
    st.image(img, caption = "image", use_column_width = True)

# 〇音声
st.audio("1.mp3", format="audio/mpeg", loop=True)

# 〇動画
if st.checkbox('Show move'):
    st.video("move.mp4", loop=True)

# 〇セレクトボックス
option = st.selectbox(
    'あなたが好きな数字は？',
    list(range(1, 11))
)
'you like number', option, '!'

# 〇ツーカラムレイアウト
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button: # buttonが押下されたら
    right_column.write('右カラムです。')

# 〇テキスト入力 ※値の動的変化 + サイドバー
texts = st.sidebar.text_input('あなたの趣味は？')
'あなたの趣味は', texts, 'ですね！'

# 〇スライダー + サイドバー
condition = st.sidebar.slider('今のあなたの調子は？', 0, 100, 50)
'condition is', condition 

# 〇エキスパンダー
expander = st.expander('問い合わせ1')
expander.write('問い合わせ1の回答')
expander = st.expander('問い合わせ2')
expander.write('問い合わせ2の回答')
expander = st.expander('問い合わせ3')
expander.write('問い合わせ3の回答')

# 表の使い方 df = pd.DataFrame({     
#     '1列目': [3, 2, 3, 4],
#     '2列3': [10, 20, 30, 40]

# })
# 〇表を表示させる
# st.write(df)
# st.dataframe(df)

# 〇引数で縦横サイズ、ハイライトを指定できる。※writeではできない。
# 〇maxの引数(axis=0)は列、1だったら行。
# st.dataframe(df.style.highlight_max(axis=0), width = 100, height = 100)

# 〇staticな表(静的な表)
# st.table(df.style.highlight_max(axis=0))

# 〇マークダウン ※左寄せしないとうまく反映されない。
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """

# 〇チャート
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

# 〇折れ線
# st.line_chart(df)
# st.area_chart(df)

# 〇棒グラフ
# st.bar_chart(df)

# 〇マップ
df = pd.DataFrame(
    np.random.rand(100, 2)/ [50, 50] + [35.69, 139.70],
    columns=[ 'lat', 'lon']
)
st.map(df)

