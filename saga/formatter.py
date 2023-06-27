import logging

DATE_FMT = "%Y-%m-%d %H:%M:%S"

def formatter(runtime, traceid):
    formatter_obj = logging.Formatter(
        datefmt=DATE_FMT,
        fmt=(
        f'%(asctime)s loglevel="%(levelname)s" task="{runtime.name}"'
        f' message="%(message)s" traceid="{traceid}"'
        )
    )
    return formatter_obj