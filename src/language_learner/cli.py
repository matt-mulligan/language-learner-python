from typing import Optional

from pyapp.app import CliApplication

app = CliApplication(description="Python Language Learner")

main = app.dispatch

@app.command()
def hello(name: Optional[str] = None):
    """Say hello."""
    from .ex01_hello_world import hello
    hello(name)
