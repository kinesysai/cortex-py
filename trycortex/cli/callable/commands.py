import pathlib
import re
import click
import validators

from trycortex.cli.callable import callable_config


@click.group(help="Callable-related commands")
def callable():
    pass

def _slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s)
    s = s.strip("-")
    return s

@callable.command("init", help="Creates an callable.yaml file.")
def init_callable():
    click.echo("init callable")
    path = pathlib.Path(path or ".")
    path.mkdir(parents=True, exist_ok=True)

    try:
        current_config = callable_config.load_config(path)
    except FileNotFoundError:
        current_config = callable_config.CallableConfig(handle=_slugify(path.resolve().name))
    
    
