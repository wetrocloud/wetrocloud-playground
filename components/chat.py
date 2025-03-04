# from openai import AsyncOpenAI
# import chainlit as cl

# client = AsyncOpenAI(base_url="http://127.0.0.1:8001/v1/openai",api_key="c80d5cb1f295297ef77eb82f42aafe09b71625e1")

# template = """{input}
# ```"""

# settings = {
#     "model": "llama-3.3-70b",
#     "temperature": 0,
#     "max_tokens": 500,
#     "top_p": 1,
#     "frequency_penalty": 0,
#     "presence_penalty": 0,
#     "stop": ["```"],
# }

# @cl.set_starters
# async def starters():
#     return [
#        cl.Starter(
#            label=">50 minutes watched",
#            message="Compute the number of customers who watched more than 50 minutes of video this month."
#        )
#     ]
# @cl.on_message
# async def chat(message: cl.Message):
#     stream = await client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": template.format(input=message.content),
#             }
#         ], stream=True, **settings
#     )

#     msg = await cl.Message(content="", language="sql").send()

#     async for part in stream:
#         if token := part.choices[0].delta.content or "":
#             await msg.stream_token(token)

#     await msg.update()