def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_output(content, output_file, format):
    with open(output_file, 'w') as file:
        if format == 'json':
            import json
            json.dump({'content': content}, file)
        elif format == 'md':
            file.write(f"# Repository Content\n\n{content}")
        else:
            file.write(content)