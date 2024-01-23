import streamlit as st
from langchain.prompts import PromptTemplate
from datetime import datetime


st.set_page_config(
    page_title="FullStack_GPT Home",
    page_icon="💡"
)

st.title("FullStack_GPT Home")




####################


tab_one, tab_two, tab_three = st.tabs(["A", "B", "C"])

with tab_one:
    st.write("a")

with tab_two:
    st.write("b")

with tab_three:
    st.write("c")


#####################


st.sidebar.title("title1")
st.sidebar.text_input("input1")


with st.sidebar:
    st.title("title2")
    st.text_input("input2")



####################



today = datetime.today().strftime("%H:%M:%S")
st.title(today)


model = st.selectbox("Choose your model", ("GPT-3", "GPT-4"))
st.write(model)


if model == "GPT-3":
    st.write("cheap")
else:
    st.write("not cheap")


    name = st.text_input("What is your name")
    st.write(name)


    value = st.slider("temperature", min_value=0.1, max_value=1.0)
    st.write(value)


######################


st.title("Hello world")

st.subheader("Welcome to Streamlit")

st.markdown("""
  ### I love it
""")


####################


st.write("hello")

st.write([1, 2, 3])

st.write({"x":1, "y":2, "z": 3})

st.write(PromptTemplate)

p = PromptTemplate.from_template("aaa")
st.write(p)


###############


with st.status("Embedding file...", expanded=True) as status:
    time.sleep(2)
    st.write("Getting the file")
    time.sleep(2)
    st.write("Embedding the file")
    time.sleep(2)
    st.write("Caching the file")
    status.update(label="Error", state="error")