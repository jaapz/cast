cast
====

A linux command line tool to control your chromecast.

Note: this is a work in progress and the command line interface may change a
lot.

Installation
------------
You can install it by doing

    pip install cast

Usage
-----
`cast play`: resume playing.

`cast pause`: pause current content.

`cast volume`: show current volume.

`cast volume 0.3`: set current volume to 0.3 (needs to be a value between 0 and
1)

`cast status`: show a status message.

`cast toggle`: toggle play/pause.

`cast seek 10`: seek to 10th second of the song.

`cast rewind`: restart current content.

Configuration
-------------
cast loads it's config from ~/.config/cast/config.ini. An example config looks
like this:

    [cast]
    chromecast_ip=192.168.178.19
    sleep_time=0.3


License
-------
This tool is released under the MIT license. See `LICENSE`.

Thanks
------
Many thanks to Paul Schoutsen for creating
[pychromecast](https://github.com/balloob/pychromecast), on which this utility
greatly relies.
