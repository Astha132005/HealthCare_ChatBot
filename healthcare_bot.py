import os
import chainlit as cl
from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain

os.environ['HUGGINGFACEHUB_API_TOKEN'] = "enter code"

model_id = "distilgpt2"
generator = pipeline("text-generation", model=model_id, device_map="auto")

llm = HuggingFacePipeline(
    pipeline=generator,
    model_kwargs={"temperature": 0.7, "max_new_tokens": 100}
)

template = """You are a helpful and friendly healthcare assistant.
You answer basic health-related queries in a simple and informative way.

{query}
"""

prompt = PromptTemplate(template=template, input_variables=["query"])
chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

@cl.on_chat_start
def start():
    cl.user_session.set("llm_chain", chain)

@cl.on_message
async def respond(message: cl.Message):
    llm_chain = cl.user_session.get("llm_chain")
    res = await llm_chain.acall(message.content, callbacks=[cl.AsyncLangchainCallbackHandler()])
    await cl.Message(content=res["text"]).send()
