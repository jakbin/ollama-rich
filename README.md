# ollama-rich ✨

A feature-rich Ollama client with a polished terminal UI powered by Rich.

[![PyPI version](https://badge.fury.io/py/ollama-rich.svg)](https://pypi.org/project/ollama-rich)
[![Downloads](https://pepy.tech/badge/ollama-rich/month)](https://pepy.tech/project/ollama-rich)
[![Downloads](https://static.pepy.tech/personalized-badge/ollama-rich?period=total&units=international_system&left_color=green&right_color=blue&left_text=Total%20Downloads)](https://pepy.tech/project/ollama-rich)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/jakbin/ollama-rich)
![GitHub last commit](https://img.shields.io/github/last-commit/jakbin/ollama-rich)

## Features 🚀
- 📦 List available Ollama models in a beautiful, colored table
- 💬 Chat with models directly from your terminal
- 📝 Markdown rendering with live updates
- ⚡ Streaming support for responsive conversations
- 🔧 Simple, ergonomic CLI
- 🧰 Handy commands to pull, load, and manage models

## Requirements 📋
- Python 3.7+
- Running [Ollama](https://github.com/jmorganca/ollama) server
- Python packages: [rich](https://github.com/Textualize/rich), [ollama](https://github.com/ollama/ollama), [pyyaml](https://pyyaml.org/)

## Installation 📦
```bash
pip install ollama-rich
```

From source:
```bash
git clone https://github.com/jakbin/ollama-rich.git
cd ollama-rich
pip install .
```

## Quick start ⚡
```bash
# 1) Optional: configure defaults
ollama-rich setup -s http://localhost:11434 -m llama2

# 2) See available models
ollama-rich models

# 3) Pull a model (streaming by default)
ollama-rich pull llama2

# 4) Load a model into memory
ollama-rich load llama2

# 5) Chat
ollama-rich chat -m llama2 "Hello there!"

# Tip: short alias also available
or chat -m llama2 "Hi!" --stream
```

## Command reference 🧭

- Global options:
	- `--host` Set Ollama host (default comes from config; fallback: `http://localhost:11434`)
	- `--version` Show CLI version

- Setup/config:
	- `ollama-rich setup [-s --host <url>] [-m --model <name>]`

- Model management:
	- `ollama-rich models` – list available models
	- `ollama-rich model <name>` – show details for a model
	- `ollama-rich pull <name> [--nostream]` – pull a model (stream by default)
	- `ollama-rich delete <name>` – delete a model (with confirmation)
	- `ollama-rich load <name>` – load model into memory
	- `ollama-rich ps` – list models currently loaded in memory

- Chat:
	- `ollama-rich chat -m <name> "Your message" [--stream]`
		- If `-m/--model` is omitted, the default model from your config is used.

You can also use the short alias `or` in place of `ollama-rich` for all commands.

## Examples 🧪
```bash
# List models
ollama-rich models

# Show info for a model
ollama-rich model llama2

# Pull without streaming
ollama-rich pull llama2 --nostream

# Chat with streaming
ollama-rich chat -m llama2 "Explain transformers in 3 bullet points" --stream
```

## Notes 🗒️
- The default host and model are stored in a YAML config under your user config directory; run `ollama-rich setup` to change them interactively or via flags.
- Output uses Rich for colored tables, progress bars, and markdown rendering.

## License 📄
MIT
