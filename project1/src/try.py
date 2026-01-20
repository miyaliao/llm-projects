import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def llm_response(prompt):
    response = client.responses.create(
        model='gpt-4.1-mini',
        input = prompt,
        temperature=0
    )
    return response.output_text

prompt = '''
Classify the following review
as having either a positive or
negative sentiment:

The banana pudding was really tasty!
'''

response = llm_response(prompt)
print(response)

