import logging
import sys 


log_file = "log.log"

file_handler = logging.FileHandler(filename=log_file, mode="w")
stdout_handler = logging.StreamHandler(stream=sys.stdout)

logging.basicConfig(
    format="[%(asctime)s] /%(filename)s:%(lineno)d / %(levelname)s - %(name)s -- %(message)s",
    handlers = [file_handler,stdout_handler]
)

log = logging.getLogger(name="default")
log.setLevel(logging.DEBUG)