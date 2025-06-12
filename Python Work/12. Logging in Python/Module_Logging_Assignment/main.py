from module_a import module_a_func
from module_b import module_b_func
import logging.config
def config_logging():
    config_dictionary={
        'version':1,
        'formatters':{
            'default':{
                'format':'%(asctime)s-%(name)s-%(levelname)s-%(message)s'
            }
        },
        'handlers':{
            'file':
            {
                'class':'logging.FileHandler',
                'filename':'ModularLogging',
                'formatter':'default',
                'level':'DEBUG'
            },
            'console':
            {
                'class':'logging.StreamHandler',
                'formatter':'default',
                'level':'DEBUG'
            }
        },
        'root':
        {
            'handlers':['file','console'],
            'level':'DEBUG'
        }
    }
    logging.config.dictConfig(config_dictionary)

if __name__=="__main__":
    config_logging()
    main_logger=logging.getLogger(__name__)
    main_logger.info("Main Module Started")
    module_a_func()
    module_b_func()
    main_logger.info("Main Module Ended")

