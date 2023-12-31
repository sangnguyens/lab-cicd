"""
Test goes here
"""

from mylib.calculator import add
from click.testing import CliRunner
from main import add_cli

def test_add():
    return add(1,2)==3

def test_help():
    """Test the command-line interface help message."""
    runner = CliRunner()
    result = runner.invoke(add_cli, ["--help"])
    assert result.exit_code == 0
    assert "Show this message and exit." in result.output