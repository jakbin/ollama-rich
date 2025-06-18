# ollama-rich

A feature-rich Ollama client with enhanced terminal UI using the Rich library.

## Features
- List available Ollama models in a beautiful table
- Chat with models directly from the terminal
- Stream responses live with markdown rendering
- Easy-to-use CLI interface
- More comming soon

## Requirements
- Python 3.7+
- [Ollama](https://github.com/jmorganca/ollama) server running
- [rich](https://github.com/Textualize/rich) Python library

## Clone the Repository

To get the source code, clone this repository:

```bash
git clone https://github.com/yourusername/ollama-rich.git
cd ollama-rich
```

## Installation
```bash
pip install .
```

## Usage
### List Models
```bash
ollama-rich models
```

### Chat with a Model
```bash
ollama-rich chat <model> "Your message here"
```

### Stream Chat Response
```bash
ollama-rich chat <model> "Your message here" --stream
```


