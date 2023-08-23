import click

# from dotenv import set_key


@click.group()
@click.version_option()
def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m webling_calendar` and `$ webling_calendar `.
    """
    pass


@main.command()
@click.option("--set")
@click.option("api.key", prompt=True)
def config(api_key):  # pragma: no cover
    click.echo(f"set API Key: {api_key}")
    # set_key('./.env', 'WEBLING_API_KEY', api_key)
