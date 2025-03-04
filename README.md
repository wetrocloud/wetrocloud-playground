---
title: 'Wetrocloud'
tags: ['wetrocloud']
---

# Wetrocloud Playground 🚀

A powerful chat interface built with Chainlit that supports multiple AI models including LLaMA, GPT, Claude, and more.

## Features

- 🤖 Multiple AI Model Support
- 🎯 Interactive Chat Interface
- ⚙️ Configurable Settings
- 💬 Streaming Responses
- 🎨 Starter Templates

## Available Models

- LLaMA 3.3 70B
- GPT-4.5 Preview
- Claude-3-7 Sonnet
- Deepseek Models
- Qwen 2.5 32B
- Mixtral-8x7B
- And more...

## Quick Start

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your environment variables:
```bash
OPENAI_API_KEY=your_api_key_here
```

3. Run the application:
```bash
chainlit run app.py --watch --port 8000
```

## Usage

1. Launch the application and select your preferred model from the Settings panel
2. Use the starter templates or type your own prompts
3. Interact with the AI through the chat interface
4. Adjust model settings as needed during the conversation

## Project Structure

- `app.py` - Main application file with chat interface and model handling
- `sidebar.py` - Sidebar component implementation
- `.env` - Environment variables configuration

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License