import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 入門')

st.write('プレイグスバーの表示')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'DOne!!!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')



text = st.text_input('あなたが趣味を教えてください。')

'あなたの趣味は、' ,text,  'です。'

condition = st.slider('あなたの今の調子は？',0,100,50)
'コンディション：' , condition




option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1,10))
)

'あなたの好きな数字は、' ,option,  'です。'



if st.checkbox('shou Image'):
    img = Image.open('IMG_0606.JPG')
    st.image(img, caption='Kohei Imanishi', use_column_width=True)










"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""






