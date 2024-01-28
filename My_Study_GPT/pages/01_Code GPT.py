import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.schema.runnable import RunnablePassthrough


st.set_page_config(
    page_title="Code GPT",
    page_icon="🧑🏼‍💻",
)


st.title("Code GPT")


st.markdown("""
    This is Code analyzer.
    Input the Code that you want to analyze.
""")


#########################


llm = ChatOpenAI(
    temperature=0.1,
    model="gpt-3.5-turbo-1106",
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)


prompt = ChatPromptTemplate.from_template(
         """
            You are a first-class IT expert.
            Please analyze the {code} with refer to the specific part of codes
            Analyze Easy to understand for IT beginner and intermediate.
        """
)

            
chain = ({"code": RunnablePassthrough()} | prompt | llm)




#####################



inputCode = st.text_input("Code")

if inputCode:
    outputCode = chain.invoke(inputCode)
    st.write(outputCode.content)