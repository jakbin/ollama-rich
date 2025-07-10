import argparse
from rich.console import Console
from ollama_rich import OllamaRichClient
from ollama_rich import models_table, model_info_table
from ollama_rich import __version__

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Ollama Client CLI with Rich UI")
    parser.add_argument('--host', default='http://127.0.0.1:11343', help='Ollama server host URL')
    subparsers = parser.add_subparsers(dest="command")

    # List models
    subparsers.add_parser("models", help="List all available models")

    # Info about a specific model
    model_parser = subparsers.add_parser("model", help="Get information about a specific model")
    model_parser.add_argument("model", help="Model name to get information about")

    # Chat command
    chat_parser = subparsers.add_parser("chat", help="Chat with a model")
    chat_parser.add_argument("model", help="Model name")
    chat_parser.add_argument("message", help="Message to send to the model")
    chat_parser.add_argument("--stream", action="store_true", help="Stream the response live")

    parser.add_argument("--version", action="version", version="Ollama Rich Client CLI version " + __version__, 
                        help="Show the version of the Ollama Rich Client CLI")

    args = parser.parse_args()

    client = OllamaRichClient(host=args.host)

    try:
        if args.command == "models":
            models = client.models()
            models_table(models)
        
        elif args.command == "model":
            model_info = client.model_info(args.model)
            model_info_table(args.model, model_info)

        elif args.command == "chat":
            messages = [{"role": "user", "content": args.message}]
            if args.stream:
                client.chat_and_display(args.model, messages)
            else:
                md = client.chat(args.model, messages)
                console.print(md)
        else:
            parser.print_help()
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Execution interrupted by user (Ctrl+C). Exiting...[/bold yellow]")

if __name__ == "__main__":
    main()