from openai import AsyncOpenAI
import chainlit as cl
from chainlit.data.base import BaseDataLayer
from chainlit.input_widget import Select, Switch, Slider
import requests

client = AsyncOpenAI(base_url="http://127.0.0.1:8001/v1/openai",api_key="c80d5cb1f295297ef77eb82f42aafe09b71625e1")

@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Morning routine ideation",
            message="Can you help me create a personalized morning routine that would help increase my productivity throughout the day? Start by asking me about my current habits and what activities energize me in the morning.",
            icon="/public/favicon.svg",
            ),

        cl.Starter(
            label="Explain superconductors",
            message="Explain superconductors like I'm five years old.",
            icon="/public/favicon.svg",
            ),
        cl.Starter(
            label="Python script for daily email reports",
            message="Write a script to automate sending daily email reports in Python, and walk me through how I would set it up.",
            icon="/public/favicon.svg",
            ),
        cl.Starter(
            label="Text inviting friend to wedding",
            message="Write a text asking a friend to be my plus-one at a wedding next month. I want to keep it super short and casual, and offer an out.",
            icon="/public/favicon.svg",
            )
        ]


@cl.on_chat_start
async def start():
    elements = [  
        cl.CustomElement(name="custom",props={"link":"https://wetrocloud.com/","name":"Describing why Wetrocloud is the best why Wetrocloud is the best"}),
    ]

    await cl.ElementSidebar.set_elements(elements)
    # await cl.ElementSidebar.set_title("Test title")
    settings = await cl.ChatSettings(
        [
            Select(
                id="Model",
                label="OpenAI - Model",
                values=["gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-4", "gpt-4-32k"],
                initial_index=1,
            ),
            Switch(id="Streaming", label="OpenAI - Stream Tokens", initial=True),
            Slider(
                id="Temperature",
                label="OpenAI - Temperature",
                initial=0,
                min=0,
                max=2,
                step=0.1,
            ),
            Slider(
                id="SAI_Steps",
                label="Stability AI - Steps",
                initial=30,
                min=10,
                max=150,
                step=1,
                description="Amount of inference steps performed on image generation.",
            ),
            Slider(
                id="SAI_Cfg_Scale",
                label="Stability AI - Cfg_Scale",
                initial=7,
                min=1,
                max=35,
                step=0.1,
                description="Influences how strongly your generation is guided to match your prompt.",
            ),
            Slider(
                id="SAI_Width",
                label="Stability AI - Image Width",
                initial=512,
                min=256,
                max=2048,
                step=64,
                tooltip="Measured in pixels",
            ),
            Slider(
                id="SAI_Height",
                label="Stability AI - Image Height",
                initial=512,
                min=256,
                max=2048,
                step=64,
                tooltip="Measured in pixels",
            ),
        ]
    ).send()

# @cl.on_chat_start
# async def start_chat():
#     cl.user_session.set("messages", [])
# @cl.action_callback("action_button")
# async def on_action(action: cl.Action):
#     print(action.payload)

# async def call_wetrocloud(query: str):
#     messages = cl.user_session.get("messages")
#     messages.append({"role": "user", "content": query})
    
#     msg = cl.Message(content="", author="Wetrocloud")
#     stream = [{"role": "assistant", "content": "Hello, how can I help you today?"}]
#     # stream = await client.chat.completions.create(
#     #     model="llama-3.3-70b",
#     #     messages=messages,
#     #     max_tokens=1000,
#     #     stream=True,
#     # )

#     # await msg.send()
#     # async for part in stream:
#     #     if token := part.choices[0].delta.content or "":
#     #         await msg.stream_token(token)
#     await msg.send()
#     async for part in stream:
#         await msg.stream_token(part["content"])
    
#     messages.append({"role": "assistant", "content": msg.content})
#     cl.user_session.set("messages", messages)

# @cl.on_message
# async def chat(message: cl.Message):
#     await call_wetrocloud(message.content)

# @cl.set_chat_profiles
# async def chat_profile(current_user: cl.User):
#     return [
#         cl.ChatProfile(
#             name="My Chat Profile",
#             icon="https://picsum.photos/250",
#             markdown_description="The underlying LLM model is **GPT-3.5**, a *175B parameter model* trained on 410GB of text data.",
#             starters=[
#                 cl.Starter(
#                     label="Morning routine ideation",
#                     message="Can you help me create a personalized morning routine that would help increase my productivity throughout the day? Start by asking me about my current habits and what activities energize me in the morning.",
#                     icon="/public/favicon.svg",
#                 ),
#                 cl.Starter(
#                     label="Explain superconductors",
#                     message="Explain superconductors like I'm five years old.",
#                     icon="/public/favicon.svg",
#                 ),
#             ],
#         )
#     ]
