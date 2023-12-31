#!/usr/bin/env python3

"""
Main cli or app entry point
"""

from mylib.calculator import add
import click

@click.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
def add_cli(a, b):
    """Add two numbers together

    Example: 
        python3 main.py 1 2
    """
    result = add(a, b)
    click.echo(click.style(str(result), fg="green"))

if __name__=="__main__":
    # pylint: disable=no-value-for-parameter
    add_cli()
    