# MCP Test Repo Helper

A Model Context Protocol (MCP) server built with FastMCP that provides basic tools, resources, and prompts for testing and development purposes.

## Features

This MCP server includes three main capabilities:

### 🔧 Tools
- **`add(a: int, b: int) -> int`** - Adds two numbers together
  - Supports both integers and floating-point numbers
  - Example: `add(300099933, 0.99393939393)` returns `300099933.99393939393`

### 📚 Resources
- **`greeting://{name}`** - Provides personalized greetings
  - Example: `greeting://devon` returns "Hello, devon!"

### 💬 Prompts
- **`greet_user(name: str, style: str = "friendly") -> str`** - Generates greeting prompts in different styles
  - **Styles available:**
    - `friendly` - "Please write a warm, friendly greeting"
    - `formal` - "Please write a formal, professional greeting" 
    - `casual` - "Please write a casual, relaxed greeting"
  - Example: `greet_user("devon", "friendly")` returns "Please write a warm, friendly greeting for someone named devon."

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd mcp-test-repo-helper
   ```

2. **Install dependencies using uv:**
   ```bash
   uv sync
   ```

3. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

## Running the Server

### Option 1: Direct Python execution
```bash
python3 main.py
```

### Option 2: Using MCP CLI
```bash
mcp run main.py
```

### Option 3: Development mode with Inspector
```bash
mcp dev main.py
```
This opens the MCP Inspector UI for interactive testing and debugging.

## Testing the Server

Once running, you can test the server using:

1. **MCP Inspector UI** (recommended for development)
   - Run `mcp dev main.py` to open the interactive interface
   - Test all tools, resources, and prompts through the web UI

2. **Direct MCP client connections**
   - Connect any MCP-compatible client to the server
   - Use stdio transport for local connections

## Project Structure

```
mcp-test-repo-helper/
├── main.py              # Main MCP server implementation
├── pyproject.toml       # Project dependencies and configuration
├── README.md           # This file
└── venv/               # Virtual environment (created by uv)
```

## Dependencies

- **mcp[cli]>=1.13.0** - Model Context Protocol framework
- **Python >=3.12** - Required Python version

## Development Notes

### Common Issues and Solutions

1. **"command not found: python"**
   - Use `python3` instead of `python` on macOS
   - Ensure virtual environment is activated

2. **"No such file or directory" errors**
   - Make sure you're in the correct directory (`mcp-test-repo-helper/`)
   - Check that `main.py` exists in the current directory

3. **MCP server not responding**
   - Verify the server is running with `mcp dev main.py` for interactive testing
   - Check that all dependencies are installed with `uv sync`

### Server Architecture

The server uses FastMCP for easy MCP server development:
- **FastMCP("Demo")** - Creates the main server instance
- **@mcp.tool()** - Decorator for adding callable tools
- **@mcp.resource()** - Decorator for adding accessible resources  
- **@mcp.prompt()** - Decorator for adding prompt generators
- **mcp.run("stdio")** - Runs the server with stdio transport

## Usage Examples

### Testing the Addition Tool
```python
# In MCP Inspector or client
add(a=5, b=3)  # Returns: 8
add(a=300099933, b=0.99393939393)  # Returns: 300099933.99393939393
```

### Testing the Greeting Resource
```python
# Access resource
greeting://devon  # Returns: "Hello, devon!"
```

### Testing the Greeting Prompt
```python
# Generate different greeting styles
greet_user(name="devon", style="friendly")  # Returns: "Please write a warm, friendly greeting for someone named devon."
greet_user(name="devon", style="formal")    # Returns: "Please write a formal, professional greeting for someone named devon."
greet_user(name="devon", style="casual")    # Returns: "Please write a casual, relaxed greeting for someone named devon."
```

## Contributing

This is a test/example MCP server. Feel free to:
- Add new tools, resources, or prompts
- Modify existing functionality
- Use as a template for your own MCP servers

## License

This project is open source and available under the MIT License.
