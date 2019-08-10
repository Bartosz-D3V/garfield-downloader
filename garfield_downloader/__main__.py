""" Main run file containing the CLI
"""

from datetime import date, datetime
import click

from garfield_downloader.parser.get_confirmation_cookie import get_confirmation_data, get_age_gated

DATE_FORMATS = ["%d/%m/%Y", "%d-%m-%Y", "%Y/%m/%d", "%Y-%m-%d"]


@click.command()
@click.option("--start_date",
              default="19/06/1978",
              help="Starting date of comics to download",
              type=click.DateTime(formats=DATE_FORMATS))
@click.option("--end_date",
              default=str(date.today()),
              help="Ending date of comics to download",
              type=click.DateTime(formats=DATE_FORMATS))
# pylint: disable=unused-argument
def main(start_date: datetime, end_date: datetime) -> None:
    """
    Main method instantiating CLI
    :param start_date: datetime
    :param end_date: datetime
    :return: None
    """
    click.secho("Downloading confirmation cookies from https://garfield.com...", fg='red')
    confirmation_data = get_confirmation_data()
    # pylint: disable=unused-variable
    age_gated = get_age_gated(confirmation_data[0], confirmation_data[1])
    click.secho("Done! Cookie downloaded successfully", fg='green')


# pylint: disable=no-value-for-parameter
main()
