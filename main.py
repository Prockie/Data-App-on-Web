import streamlit as st
import pandas


data = {
  'Series_1':[1,2,3,4,6,9],
  'Series_2':[10,20,53,250,275,300]
}

df = pandas.DataFrame(data)

st.title('Our first steamlit app')
st.subheader('Introducing this as a awy of showing data')
st.write(''' THis is nice
Really nice
''')

st.write(df)
st.line_chart(df)
