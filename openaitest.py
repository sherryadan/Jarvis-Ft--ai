import openai
from config import apikey
# client = openai()

openai.api_key = apikey

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "hello write me an email for resgination"
    }
  ],
  temperature=1,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)