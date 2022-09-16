import logging

from .network import Network

logging.basicConfig(level=logging.DEBUG)

network = Network()

network.run(0, 5)
