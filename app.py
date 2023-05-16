import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

st.title("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.checkbox('yes')
st.button('Touch')
st.selectbox('Pick your gender',['Men','Women'])
st.slider('your older',0,100)

rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)
