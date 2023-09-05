import click
from webling_calendar.config import Config
from webling_calendar.ics_reader import IcsReader
from webling_calendar.api import Api
from webling_calendar.calendarevent import Calendarevent

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
@click.option("--set-api-key", help="Sets and saves API key.")
@click.option("--set-api-url", help="Sets and saves API enpoint url.")
@click.option("--get-api-key", help="Show API key.", is_flag=True)
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


@main.command(no_args_is_help=True)
@click.argument("file")
def create_from_ics(file):  # pragma: no cover
    try:
        CONFIG.check_configuration()
        ics = IcsReader(file)
        api = Api(CONFIG.webling_api_key, CONFIG.webling_endpoint_url)
        calendar_ids = api.get_calendar_ids()
        for id in calendar_ids:
            calendar = api.get_calendar_from_id(id)
            click.echo(f"{id}: {calendar.title}")
        choosen_calendar = click.prompt(
            "Enter the id of the calendar you would want to add the events to",
            type=int,
        )
        while choosen_calendar not in calendar_ids:
            choosen_calendar = click.prompt(
                "Calendar ID not valid, try again", type=int
            )
        click.confirm(
            f"Calendardata from {file} will be added to {choosen_calendar}",
            abort=True,
        )
        for event in ics.event_list:
            calendarevent = Calendarevent(event, [choosen_calendar])
            api.create_new_calendarevent(calendarevent)
    except Exception as e:
        click.secho(e, fg="red", err=True)
