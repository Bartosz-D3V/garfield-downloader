""" Main run file containing the CLI
"""

import click
from click import DateTime, secho
from datetime import date, datetime

from garfield_downloader.parser.get_confirmation_cookie import get_confirmation_data, get_age_gated

date_formats = ["%d/%m/%Y", "%d-%m-%Y", "%Y/%m/%d", "%Y-%m-%d"]


@click.command()
@click.option("--start_date",
              default="19/06/1978",
              help="Starting date of comics to download",
              type=DateTime(formats=date_formats))
@click.option("--end_date",
              default=str(date.today()),
              help="Ending date of comics to download",
              type=DateTime(formats=date_formats))
# pylint: disable=unused-argument
def main(start_date: datetime, end_date: datetime) -> None:
    secho("Downloading confirmation cookies from https://garfield.com...", fg='red')
    confirmation_data = get_confirmation_data()
    age_gated = get_age_gated(confirmation_data[0], confirmation_data[1])
    secho("Done! Cookie downloaded successfully", color='green')


main()
