from openai import AsyncOpenAI
import chainlit as cl
from chainlit.data.base import BaseDataLayer
from chainlit.input_widget import Select, Switch, Slider
import requests
from decouple import config

client = AsyncOpenAI(base_url=config('OPENAI_BASE_URL'))


MODEL_LISTS = [
    "llama-3.3-70b","gpt-4.5-preview","claude-3-7-sonnet-20250219","deepseek-r1-distill-qwen-32b","qwen-2.5-32b","mixtral-8x7b-32768"
    "deepseek-r1-distill-llama-70b","claude-3-5-sonnet-20240620","gpt-4","gpt-3.5-turbo","o3-mini","o1-mini","o1","o1-preview","gemma2-9b-it"
]

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
    cl.user_session.set("messages", [])
    settings = await cl.ChatSettings(
        [
            Select(
                id="Model",
                label="Select Model",
                values=MODEL_LISTS,
                initial_index=0,
            )
        ]
    ).send()
    await update_settings(settings)
    msg = """ # Welcome to Wetrocloud! ☁️🚀
Hi there! 👋 I'm your Wetrocloud assistant. How can I help you today? 😊
You can click the Settings button to try out different models and customize your experience! ⚙️✨"""
    await cl.Message(content=msg).send()

@cl.on_settings_update
async def update_settings(settings):
    cl.user_session.set("model", settings["Model"])

async def call_wetrocloud(query: cl.Message, model="llama-3.3-70b"):

    messages = cl.user_session.get("messages")
    model = cl.user_session.get("model")
    messages.append(
        {"role": "user", "content": query.content})
    
    msg = cl.Message(content="", author="Wetrocloud")
    stream = await client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

    await msg.send()
    async for part in stream:
        if part.choices != []:
            if token := part.choices[0].delta.content or "":
                await msg.stream_token(token)
    
    messages.append({"role": "assistant", "content": msg.content})
    cl.user_session.set("messages", messages)

@cl.on_message
async def chat(message: cl.Message):
    await call_wetrocloud(message)

