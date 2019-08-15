""" Main run file containing the CLI
"""
from datetime import date, datetime
from queue import Queue

import click

from garfield_downloader.collection_util.split_collection import split_collection
from garfield_downloader.downloader.download_worker import DownloadWorker
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
@click.option("--path",
              default=str('./'),
              help="Path to save the comics",
              type=click.Path(dir_okay=True, writable=True, allow_dash=True))
def main(start_date: datetime, end_date: datetime, path: str) -> None:
    """
    CLI for concurrent downloading comics from garfield.com
    :param start_date: datetime
    :param end_date: datetime
    :param path: str
    :return: None
    """
    click.secho("Downloading confirmation cookies from https://garfield.com...", fg='red')
    confirmation_data = get_confirmation_data()
    age_gated = get_age_gated(confirmation_data[0], confirmation_data[1])
    click.secho("Done! Cookie downloaded successfully", fg='green')

    click.secho("Fetching links to download comics...", fg="yellow")
    website_links = get_comic_links(start_date, end_date)
    click.secho("Done! Links with comics fetched successfully", fg='green')
    raw_img_srcs = [get_imgs_src(link, age_gated=age_gated)[0] for link in website_links]

    queue: Queue = Queue()
    chunked_lists = split_collection(raw_img_srcs, int(len(raw_img_srcs) / 10))
    click.secho("Starting download of the comics...", fg="yellow")
    for chunked_list in chunked_lists:
        worker = DownloadWorker(queue)
        worker.start()
        queue.put((path, chunked_list))
    queue.join()
    click.secho("Done! Comics downloaded successfully", fg='green')


# pylint: disable=no-value-for-parameter
main()
