""" Main run file containing the CLI
"""
from datetime import date, datetime
import click

from garfield_downloader.parser.get_comic_links import get_comic_links
from garfield_downloader.parser.get_confirmation_cookie import get_confirmation_data, get_age_gated
from garfield_downloader.parser.get_imgs_src import get_imgs_src

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
def main(start_date: datetime, end_date: datetime) -> None:
    """
    Main method instantiating CLI
    :param start_date: datetime
    :param end_date: datetime
    :return: None
    """
    click.secho("Downloading confirmation cookies from https://garfield.com...", fg='red')
    confirmation_data = get_confirmation_data()
    age_gated = get_age_gated(confirmation_data[0], confirmation_data[1])
    click.secho("Done! Cookie downloaded successfully", fg='green')
    website_links = get_comic_links(start_date, end_date)
    raw_img_srcs = map(lambda link: get_imgs_src(link, age_gated=age_gated)[0], website_links)
    print(list(raw_img_srcs))


# pylint: disable=no-value-for-parameter
main()
