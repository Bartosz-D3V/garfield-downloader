""" Main run file containing the CLI
"""
from datetime import date, datetime
import click

from garfield_downloader.downloader.create_dir import create_dir
from garfield_downloader.downloader.download_image import download_image
from garfield_downloader.downloader.get_comic_dir import get_comic_dir
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

    click.secho("Fetching links to download comics...", fg="yellow")
    website_links = get_comic_links(start_date, end_date)
    click.secho("Done! Links with comics fetched successfully", fg='green')
    raw_img_srcs = map(lambda link: get_imgs_src(link, age_gated=age_gated)[0], website_links)
    click.secho("Starting download of the comics...")
    for src in raw_img_srcs:
        save_dir = get_comic_dir(src)
        create_dir("/".join(save_dir.split('/')[:2]))
        download_image(save_dir, src)
        click.secho(f"Downloaded comic: {save_dir}")


# pylint: disable=no-value-for-parameter
main()
