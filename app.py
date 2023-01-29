import streamlit as st
st.write("# 유튜브 조회수")
view = [50, 100, 150, 200]
st.write('## Bar Chart')
st.bar_chart(view)
st.markdown('PANDAS')
import pandas as pd
pdS_view = pd.Series(view)
pdS_view
