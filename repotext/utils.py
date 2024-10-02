import os
import ast

def get_file_order(repo_path):
    """
    Determine an intelligent order for processing files.
    Prioritize main files, then utilities, then tests.
    """
    file_order = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(('.py', '.js', '.java', '.cpp')):  # Add more extensions as needed
                full_path = os.path.join(root, file)
                if 'main' in file.lower():
                    file_order.insert(0, full_path)
                elif 'test' in file.lower():
                    file_order.append(full_path)
                else:
                    file_order.insert(len(file_order) // 2, full_path)
    return file_order

def analyze_dependencies(repo_path):
    """
    Analyze Python dependencies in the repository.
    """
    dependencies = set()
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r') as f:
                    try:
                        tree = ast.parse(f.read())
                        for node in ast.walk(tree):
                            if isinstance(node, ast.Import):
                                for n in node.names:
                                    dependencies.add(n.name)
                            elif isinstance(node, ast.ImportFrom):
                                dependencies.add(node.module)
                    except SyntaxError:
                        print(f"Couldn't parse {file}")
    return list(dependencies)

def get_project_structure(repo_path):
    """
    Generate a string representation of the project structure.
    """
    structure = []
    for root, dirs, files in os.walk(repo_path):
        level = root.replace(repo_path, '').count(os.sep)
        indent = ' ' * 4 * level
        structure.append(f'{indent}{os.path.basename(root)}/')
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            structure.append(f'{sub_indent}{file}')
    return '\n'.join(structure)