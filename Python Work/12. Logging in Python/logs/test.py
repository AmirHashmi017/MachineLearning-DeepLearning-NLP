from logging_settings import logging
logging.info("Just an Information")
logging.debug("Program is working")
logging.warning("This is warning")
logging.error("Error Log")
logging.critical("Critical Error")

logger1=logging.getLogger("Module1")
logger1.setLevel(logging.DEBUG)
logger2=logging.getLogger("Module2")
logger2.setLevel(logging.ERROR)

logger1.debug("Logger 1 Debugging")
logger2.error(" Logger2 error")