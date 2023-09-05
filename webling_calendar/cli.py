import click
from webling_calendar.config import Config

CONFIG = Config()


@click.group()
@click.version_option()
def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m webling_calendar` and `$ webling_calendar `.
    """
    pass


@main.command(no_args_is_help=True)
@click.option("--set-api-key", help="Sets and saves API key")
@click.option("--set-api-url", help="Sets and saves API enpoint url.")
@click.option("--get-api-key", help="Show API key", is_flag=True)
@click.option("--get-api-url", help="Show API url.", is_flag=True)
def config(
    set_api_key, set_api_url, get_api_key, get_api_url
):  # pragma: no cover
    if get_api_key:
        click.echo(f"API Key: {CONFIG.webling_api_key}")
    if get_api_url:
        click.echo(f"API endpoint url: {CONFIG.webling_endpoint_url}")
    if set_api_key:
        CONFIG.set_api_key(set_api_key)
    if set_api_url:
        CONFIG.set_enpoint_url(set_api_url)

    try:
        CONFIG.check_configuration()
    except Exception as e:
        click.secho(e, fg="red", err=True)
