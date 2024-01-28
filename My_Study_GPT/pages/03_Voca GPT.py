import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.schema.runnable import RunnablePassthrough
from langchain.callbacks.base import BaseCallbackHandler


st.set_page_config(
    page_title="Voca GPT",
    page_icon="📙",
)


st.title("Voca GPT")


st.markdown("""
    This is English Dictionary.
    Input the English vocabulary that you want to search.
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
            You are an first-class English-Korean Dictionary.
            Please Explain the {voca} with example sentence.
            And explain in Korean too.
            print the Result like the below.

                - meaning: ㅊㅍ  

                - Example Sentence:


                - 뜻:

                - 예문:
        """
)


chain = ({"voca": RunnablePassthrough()} | prompt | llm)




#####################



inputVoca = st.text_input("voca")

if inputVoca:
    outputVoca = chain.invoke(inputVoca)
    st.write(outputVoca.content)