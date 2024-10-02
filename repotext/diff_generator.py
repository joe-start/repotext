import difflib
import os

def generate_diff(new_content, repo_path):
    """
    Generate a diff between the new content and the last packed content.
    """
    last_pack_file = os.path.join(repo_path, '.last_repotext_pack.txt')
    
    if not os.path.exists(last_pack_file):
        # If no previous pack exists, return the full new content
        with open(last_pack_file, 'w') as f:
            f.write('\n'.join(new_content))
        return new_content

    with open(last_pack_file, 'r') as f:
        old_content = f.read().splitlines()

    differ = difflib.Differ()
    diff = list(differ.compare(old_content, new_content))

    # Update the last pack file
    with open(last_pack_file, 'w') as f:
        f.write('\n'.join(new_content))

    return diff