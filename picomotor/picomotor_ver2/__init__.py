"""
this is for adl MIYOPICO_ver1.adl.
"""
import logging
def get_module_logger(modname):
    #logging.config.fileConfig('logging.conf')
    logging.config.fileConfig('/opt/rtcds/userapps/release/cds/common/scripts/picomotor_ver2/picomotor_ver2/logging.conf')
    logger = logging.getLogger('logExample')
    return logger
