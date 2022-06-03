"""
Stub function and module used as a setuptools entry point.
"""

from sys import argv, exit, stdin, stdout, stderr
from nextstrain import cli

# Entry point for setuptools-installed script.
def main():
    # Ensure all our stdio streams are UTF-8; a poor man's UTF-8 mode (-X utf8
    # or PYTHONUTF8=1) roughly equivalent to PYTHONIOENCODING=UTF-8.
    for stdio in (stdin, stdout, stderr):
        if stdio.encoding != "UTF-8":
            try:
                stdio.reconfigure(encoding = "UTF-8")
            except AttributeError:
                # reconfigure() is Python 3.7+
                pass

    return cli.run( argv[1:] )

# Run when called as `python -m nextstrain.cli`, here for good measure.
if __name__ == "__main__":
    exit( main() )
