import os
import logging
from .file_handler import read_file, write_output
from .security import check_for_sensitive_info
from .tokenizer import count_tokens
from .diff_generator import generate_diff
from .compressor import compress_text
from .utils import get_file_order, analyze_dependencies, get_project_structure

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def pack_repository(repo_path, output, exclude, diff, compress, format):
    packed_content = []
    total_tokens = 0
    
    # Add these to the existing exclude list
    default_excludes = [
        '__pycache__', 'venv', '.venv', '.git', '.idea', '.vscode',
        'build', 'dist', '*.egg-info', '*.pyc', '.DS_Store'
    ]
    exclude = list(exclude) + default_excludes

    for root, dirs, files in os.walk(repo_path):
        # Remove excluded directories
        dirs[:] = [d for d in dirs if d not in exclude]
        
        for file in files:
            if any(file.endswith(ext) for ext in ['.py', '.md', '.txt', '.yml', '.yaml', '.json']):
                file_path = os.path.relpath(os.path.join(root, file), repo_path)
                if not any(fnmatch.fnmatch(file_path, pattern) for pattern in exclude):
                    content = read_file(os.path.join(root, file))
                    safe_content = check_for_sensitive_info(content)
                    tokens = count_tokens(safe_content)
                    total_tokens += tokens
                    packed_content.append(f"File: {file_path}\nTokens: {tokens}\n\n{safe_content}\n\n")
    
    logger.debug(f"Starting to pack repository: {repo_path}")
    
    # Get intelligent file order
    file_order = get_file_order(repo_path)
    
    for file_path in file_order:
        if any(file_path.endswith(ext) for ext in ['.py', '.js', '.java', '.cpp', '.md', '.txt', '.json', '.yaml', '.yml']):
            if not any(file_path.startswith(ex) for ex in exclude):
                try:
                    content = read_file(file_path)
                    if content is not None:
                        safe_content = check_for_sensitive_info(content)
                        tokens = count_tokens(safe_content)
                        total_tokens += tokens
                        relative_path = os.path.relpath(file_path, repo_path)
                        packed_content.append(f"File: {relative_path}\nTokens: {tokens}\n\n{safe_content}\n\n")
                    else:
                        logger.warning(f"Skipping file {file_path} due to None content")
                except Exception as e:
                    logger.error(f"Error processing file {file_path}: {str(e)}")

    # Add project structure and dependency analysis
    project_structure = get_project_structure(repo_path)
    packed_content.insert(0, f"Project Structure:\n{project_structure}\n\n")
    
    dependencies = analyze_dependencies(repo_path)
    if dependencies:
        packed_content.insert(1, f"Dependency Analysis:\n{', '.join(dependencies)}\n\n")
    else:
        packed_content.insert(1, "Dependency Analysis: No dependencies found.\n\n")

    if diff:
        packed_content = generate_diff(packed_content)

    final_content = "".join(packed_content)
    
    if compress:
        final_content = compress_text(final_content)

    write_output(final_content, output, format)
    
    logger.debug(f"Finished packing repository. Output written to {output}")
    return f"Output written to {output}. Total tokens: {total_tokens}"