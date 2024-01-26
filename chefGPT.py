from typing import Any, Dict
from fastapi import Body, FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import pinecone
import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from dotenv import load_dotenv


load_dotenv()


pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"), 
    environment="gcp-starter"
)

embedder = OpenAIEmbeddings()




# splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder()

# loader = CSVLoader("./recipes.csv")

# docs = loader.load_and_split(text_splitter=splitter)

# vector_store = Pinecone.from_documents(docs, embedder, index_name="recipes")




vector_store = Pinecone.from_existing_index("recipes", embedder)




#####################



app = FastAPI(
    title="ChefGPT. The best provider of Korean Recipes in the world.",
    description="Give ChefGPT a couple of ingredients and it will give you recipes in return.",
    servers=[
        {"url": "https://trailer-challenges-ukraine-actually.trycloudflare.com"} # Cloudflared tunnel
    ]
)



#####################



class Document(BaseModel):
    page_content: str


@app.get("/recipes", 
    summary="Returns a list of recipes.",
    description="Upon receiving an ingredient, this endpoint will return a list of recipes that contain that ingredient.",
    response_description="A Document object that contains the recipe and preparation instructions",
    response_model=list[Document],
    openapi_extra={
        "x-openai-isConsequential": False,
    }
)
def get_recipe(ingredient: str):
    docs = vector_store.similarity_search(ingredient)
    return docs





###########################





@app.get("/authorize", response_class=HTMLResponse, include_in_schema=False)
def handle_authorize(client_id: str, redirect_uri:str, state: str):
    return f"""
        <html>
            <head>
                <title> Log In </title>
            </head>
            <body>
                <h1> Log Into ChefGPT</h1>
                <a href="{redirect_uri}?code=ABCDEF&state={state}"> Authorize ChefGPT </a>
            </body>
        </html>
        """


#######################


user_token_db = {
    "ABCDEF": "nico"
}


@app.post("/token", include_in_schema=False)
def handle_token(code=Form(...)):
    return {
        "access_token": user_token_db[code]
    }