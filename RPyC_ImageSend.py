# Author: Joseph McFadden
# Description:  Create an RPyC microservice server with a method when called returns a random path to an image
#               based on a key

import rpyc
from random import *
import os


class MyService(rpyc.Service):
    """
    Defines a server that provides an images search functionality
    """

    def on_connect(self, conn):
        pass

    @staticmethod
    def exposed_get_image(key, directory):
        """
        Searches a directory for a random image
        :parameter key: the descriptor word used to select a specific directory of images
        :parameter directory: The main directory which stores folders with images
        """
        imagesPath = f"{directory}\\{key}"
        images = os.listdir(path=imagesPath)
        randomNum = randint(0, 10000000)
        if len(images) <= randomNum:
            return f"{imagesPath}\\{images[randomNum % len(images)]}"
        else:
            return f"{imagesPath}\\{images[randomNum]}"


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()

