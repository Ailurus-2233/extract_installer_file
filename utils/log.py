import logging as log

log.basicConfig(
    level=log.DEBUG, 
    format="[%(asctime)s-%(levelname)s-%(filename)s:%(lineno)s]:%(message)s", 
    datefmt="%Y-%m-%d %H:%M:%S"
)
