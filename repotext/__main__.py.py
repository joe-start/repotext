#!/usr/bin/env python3

import click
import os
from .packer import pack_repository
from .compressor import compress_text, decompress_text

@click.command()
@click.argument('repo_path', type=click.Path(exists=True))
@click.option('--output', '-o', default='repotext_output.txt', help='Output file name')
@click.option('--exclude', '-e', multiple=True, help='Patterns to exclude')
@click.option('--diff', is_flag=True, help='Generate diff from last pack')
@click.option('--compress', is_flag=True, help='Compress the output')
@click.option('--format', type=click.Choice(['txt', 'md', 'json']), default='txt', help='Output format')
def main(repo_path, output, exclude, diff, compress, format):
    """Pack a repository into a single AI-friendly file."""
    try:
        result = pack_repository(repo_path, output, exclude, diff, compress, format)
        click.echo(f"Repository packed successfully: {result}")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

if __name__ == '__main__':
    main()