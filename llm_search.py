import os
from langchain_community.llms import OpenAI

def query_openai_api(prompt):
    llm = OpenAI(
        temperature=0.7,
        model_name="gpt-3.5-turbo-instruct",  # or text-davinci-003
        openai_api_key="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"         # Optional if already set in ENV
    )
    response = llm.predict(prompt)
    return response

