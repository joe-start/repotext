# RepoText

RepoText is an open-source tool that packs your entire repository into a single, AI-friendly file. It's designed to help developers feed their codebase into LLMs/AI tools like Claude, ChatGPT, and Gemini for comprehensive project analysis and advice.

## Features

- Optimized for AI tools like Claude, ChatGPT, etc.
- Includes project and folder structure for AI context
- Provides token counts for each file and the entire repo
- One-command repo packing
- Customizable file inclusion/exclusion
- Security checks to detect and prevent inclusion of sensitive information
- Language and project type agnostic
- Optimized for smallest file size possible
- Intelligent file ordering
- Dependency analysis
- Diff-style output for changes since the last pack

## Quick Start (No Installation)

To run RepoText without installation:

1. Clone the repository:
git clone https://github.com/yourusername/repotext.git
cd repotext

2. Run directly using Python:
python3 run.py /path/to/your/repo --output packed_repo.txt

### Using a Virtual Environment (Recommended)

It's recommended to use a virtual environment to avoid conflicts with other Python packages:

1. Create a virtual environment:

python3 -m venv venv

2. Activate the virtual environment:

source venv/bin/activate

3. Install the package:

pip install -e .

4. You can now use RepoText within this virtual environment.

5. When you're done, you can deactivate the virtual environment:

deactivate

## Installation (Optional)

If you prefer to install RepoText:

1. Clone the repository:
git clone https://github.com/yourusername/repotext.git
cd repotext

2. Install the package:

pip install -e .

3. Run RepoText:
repotext /path/to/your/repo --output packed_repo.txt

## Usage

To pack a repository: 

repotext /path/to/your/repo --output packed_repo.txt

Options:
- `--output, -o`: Specify the output file name (default: repotext_output.txt)
- `--exclude, -e`: Patterns to exclude (can be used multiple times)
- `--diff`: Generate diff from last pack
- `--compress`: Compress the output
- `--format`: Output format (txt, md, or json)

Example with options:

repotext /path/to/your/repo -o packed_repo.txt --exclude ".pyc" --exclude "venv/" --diff --compress --format md

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.