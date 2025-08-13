# Mallory MCP Server

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![smithery badge](https://smithery.ai/badge/@malloryai/mallory-mcp-server)](https://smithery.ai/server/@malloryai/mallory-mcp-server)

Mallory provides a robust source of cyber and threat intelligence. Use this MCP Server to enable your agents with real-time cyber threat intelligence and detailed information about vulnerabilities, threat actors, malware, techniques and other cyber-relevant entities and content. 

<a href="https://glama.ai/mcp/servers/@malloryai/mallory-mcp-server">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@malloryai/mallory-mcp-server/badge" alt="Mallory Server MCP server" />
</a>

## 📋 Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) for dependency management (recommended)

## 🚀 Quick Start

### Installation

Clone the repository:

```bash
git clone https://github.com/malloryai/mallory-mcp-server.git
cd mallory-mcp-server
```

Set up a virtual environment and install dependencies:

```bash
# Using uv (recommended)
uv venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .

# Or using pip
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .
```

### Install Development Dependencies

For development work, install the optional dependencies:

```bash
# Using uv
uv pip install -e ".[lint,tools]"

# Or using pip
pip install -e ".[lint,tools]"
```

### Set Up Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality. Install them with:

```bash
pre-commit install
./scripts/install-commit-hook.sh
```

## ⚙️ Configuration

Create a `.env` file in the project root with the following variables:

```
APP_ENV=local
MALLORY_API_KEY=your_api_key_here
```

## 🏃‍♂️ Running the Server

### Direct Execution

```bash
python -m malloryai.mcp.app
```
 or
```bash
uv run malloryai/mcp/app.py
```

### Via the Claude Desktop Configuration

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "MalloryAI": {
      "command": "/path/to/uv",
      "args": [
        "run",
        "--python",
        "/path/to/mcp-server/.venv/bin/python",
        "/path/to/mcp-server/malloryai/mcp/app.py"
      ],
      "env": {
        "MALLORY_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

## 📦 Project Structure

```
.
├── README.md
├── app.py                  # Main application entry point
├── malloryai/              # Main package
│   ├── __init__.py
│   └── mcp/                # MCP subpackage
│       ├── __init__.py
│       ├── config/         # Configuration modules
│       ├── server/         # Server implementation
│       ├── tools/          # Tool implementations
│       └── utils/          # Utility functions
├── pyproject.toml          # Project metadata and dependencies
├── scripts/                # Utility scripts
│   └── install-commit-hook.sh
```

## 🧪 Development

### Code Style

This project uses:
- [Black](https://github.com/psf/black) for code formatting
- [isort](https://pycqa.github.io/isort/) for import sorting
- [flake8](https://flake8.pycqa.org/) for linting

Format your code with:

```bash
black .
isort .
flake8
```

### Commit Message Format

This project follows the conventional commit format. Each commit message should follow this pattern:

```
<type>[(scope)]: <description>
```

Where `type` is one of:
- `feat` or `feature`: New feature
- `fix`, `bugfix`, or `hotfix`: Bug fixes
- `chore`: Regular maintenance tasks
- `refactor`: Code changes that neither fix bugs nor add features
- `docs`: Documentation only changes
- `style`: Changes that don't affect the meaning of the code
- `test`: Adding or correcting tests
- `perf`: Performance improvements
- `ci`: Changes to CI configuration
- `build`: Changes to build system or dependencies
- `revert`: Reverting previous commits

Example: `feat(server): add new authentication method`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request