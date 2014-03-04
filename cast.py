"""Command line utility to control your Google Chromecast.

Usage:
    cast next
    cast pause
    cast play
    cast status
    cast volume [<value>]

Options:
    -h --help       Show this text.
    -v --version    Show current version.
"""

from docopt import docopt
import pychromecast
import time
import logging

from ConfigParser import ConfigParser
from os.path import expanduser

config = ConfigParser()
config.read(expanduser('~/.config/cast/config.ini'))

CHROMECAST_HOST = config.get('cast', 'chromecast_ip')
SLEEP_TIME = float(config.get('cast', 'sleep_time'))


# HACK: disable the pychromecast and requests loggers because the pychromecast
# module sets the global logging level to INFO and we do not want to see all
# the ugly logging output.
pychromecast_logger = logging.getLogger('pychromecast')
pychromecast_logger.setLevel(logging.ERROR)

requests_logger = logging.getLogger('requests.packages.urllib3.connectionpool')
requests_logger.setLevel(logging.ERROR)
def _volume_command(ramp, volume):
    """ Set the value if a volume level is provided, else print the current
    volume level. """
    if volume is not None:
        ramp.set_volume(float(volume))
    else:
        print ramp.volume


def main():
    """ Read the options given on the command line and do the required actions.

    This method is used in the entry_point `cast`.
    """
    opts = docopt(__doc__, version="cast 0.1")

    cast = pychromecast.PyChromecast(CHROMECAST_HOST)
    ramp = cast.get_protocol(pychromecast.PROTOCOL_RAMP)

    # Wait for ramp connection to be initted.
    time.sleep(SLEEP_TIME)

    if opts['next'] is True:
        ramp.next()
    elif opts['pause'] is True:
        ramp.pause()
    elif opts['play'] is True:
        ramp.play()
    elif opts['status'] is True:
        # TODO: make this into a user readable text
        print cast.app
    elif opts['volume'] is True:
        _volume_command(ramp, opts['<value>'])

    # Wait for command to be sent.
    time.sleep(SLEEP_TIME)
