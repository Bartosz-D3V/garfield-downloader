""" download_worker module

Defines a worker class that implements
python run concurrency method

"""

from threading import Thread

from garfield_downloader.downloader.download_images import download_images


class DownloadWorker(Thread):
    """
    Class for managing concurrent work
    for comics downloading
    """
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self) -> None:
        """
        Concurrent method to download
        given links
        :return: None
        """
        directory, links = self.queue.get()
        try:
            download_images(directory, links)
        finally:
            self.queue.task_done()
