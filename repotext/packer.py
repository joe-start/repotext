import os
from .file_handler import read_file, write_output
from .security import check_for_sensitive_info
from .tokenizer import count_tokens
from .diff_generator import generate_diff
from .compressor import compress_text
from .utils import get_file_order, analyze_dependencies, get_project_structure

def pack_repository(repo_path, output, exclude, diff, compress, format):
    packed_content = []
    total_tokens = 0
    
    # Get intelligent file order
    file_order = get_file_order(repo_path)
    
    for root, dirs, files in os.walk(repo_path):
        # Exclude version control directories
        dirs[:] = [d for d in dirs if d not in ['.git', '.svn', '.hg']]
        
        for file in files:
            if any(file.endswith(ext) for ext in ['.py', '.js', '.java', '.cpp', '.md', '.txt', '.json', '.yaml', '.yml']):
                file_path = os.path.relpath(os.path.join(root, file), repo_path)
                if not any(file_path.startswith(ex) for ex in exclude):
                    content = read_file(os.path.join(root, file))
                    safe_content = check_for_sensitive_info(content)
                    tokens = count_tokens(safe_content)
                    total_tokens += tokens
                    packed_content.append(f"File: {file_path}\nTokens: {tokens}\n\n{safe_content}\n\n")

    # Add project structure and dependency analysis
    project_structure = get_project_structure(repo_path)
    packed_content.insert(0, f"Project Structure:\n{project_structure}\n\n")
    
    dependencies = analyze_dependencies(repo_path)
    packed_content.insert(1, f"Dependency Analysis:\n{', '.join(dependencies)}\n\n")

    if diff:
        packed_content = generate_diff(packed_content)

    final_content = "".join(packed_content)
    
    if compress:
        final_content = compress_text(final_content)

    write_output(final_content, output, format)
    
    return f"Output written to {output}. Total tokens: {total_tokens}"