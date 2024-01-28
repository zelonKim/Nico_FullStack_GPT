import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.schema.runnable import RunnablePassthrough


st.set_page_config(
    page_title="Translator GPT",
    page_icon="🌎",
)


st.title("Translator GPT")


st.markdown("""
    This is English-Korean Translator.
    Input the English text that you want to translate to Korean text.
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
            You are a first-class translator.
            Please Translate the {text} into Korean and Show me only translated Korean.
            Translate Naturally in context.
            Do not translate awkwardly in context.
        """
)

            


chain = ({"text": RunnablePassthrough()} | prompt | llm)




#####################



inputText = st.text_input("English Text")

if inputText:
    outputText = chain.invoke(inputText)
    st.write(outputText.content)