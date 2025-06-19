import argparse
from rich.console import Console
from rich.table import Table
from ollama_rich.ollama_rich import OllamaRichClient
from ollama_rich.utils import to_gb
from rich.panel import Panel

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

    args = parser.parse_args()
    client = OllamaRichClient(host=args.host)

    if args.command == "models":
        models = client.models()
        if 'models' in models:
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Model", style="red")
            table.add_column("Size (GB)", style="blue")
            table.add_column("Parameters", style="green")
            for model in models['models']:
                table.add_row(
                    model.get('model', ''),
                    f"{to_gb(model.get('size', 0))}",
                    str(model.get('details', {}).get('parameter_size', ''))
                )
            console.print(table)
        else:
            console.print("[bold red]No models found.[/ bold red]")
    
    elif args.command == "model":
        model_info = client.model_info(args.model)
        if model_info:
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Field", style="red")
            table.add_column("Value", style="blue")
            for key, value in model_info.dict().items():
                if key == "details" and isinstance(value, dict):
                    details_table = Table(show_header=True, header_style="bold cyan")
                    details_table.add_column("Detail", style="yellow")
                    details_table.add_column("Value", style="green")
                    for d_key, d_value in value.items():
                        details_table.add_row(str(d_key), str(d_value))
                    table.add_row(key, Panel(details_table, title="Details", expand=False))
                else:
                    table.add_row(key, str(value))
            console.print(table)
        else:
            console.print(f"[bold red]Model '{args.model}' not found.[/bold red]")

    elif args.command == "chat":
        messages = [{"role": "user", "content": args.message}]
        if args.stream:
            client.chat_and_display(args.model, messages)
        else:
            md = client.chat(args.model, messages)
            console.print(md)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
