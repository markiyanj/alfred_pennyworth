import logging.handlers


class Error(Exception):
    pass


class TooManyVisitors(Error):
    def __init__(self, message='too many visitors'):
        self.message = message


class TooFewVisitors(Error):
    def __init__(self, message='too few visitors'):
        self.message = message


class Concert:
    # add 2 class attributes - max_visitors (200) and min_visitors (10)
    max_visitors = 200
    min_visitors = 10

    def __init__(self, visitors_num):
        """
        if visitors num is bigger than max_visitors - raise TooManyVisitors error
        if visitors num is less than min_visitors - raise TooFewVisitors error
        """
        if 10 <= visitors_num <= 200:
            self.visitors_num = visitors_num
        else:
            if visitors_num < self.min_visitors:
                raise TooFewVisitors
            else:
                raise TooManyVisitors


def make_concert(visitors_num):
    """
    create Concert instance - handle TooManyVisitors and TooFewVisitors errors here:
    in case if caught - log error to console and return False, in case of successful initialization - return True
    """
    try:
        concert = Concert(visitors_num)
    except TooFewVisitors as err:
        print(err.message)
        return False
    except TooManyVisitors as err:
        print(err.message)
        return False
    else:
        return True


# create Logger object
# set level to debug
# add handler to write logs to file "test.log"
logger = logging.getLogger('File logger')
logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler('test.log', mode='w')
logger.addHandler(handler)


def log_message(message, level):
    """
    this function should use the logger defined above and log messages.
    level is the numeric representation of log level the message should refer to.
    :param message:
    :param level:
    """
    if level == 10:
        logger.debug(message)
    elif level == 20:
        logger.info(message)
    elif level == 30:
        logger.warning(message)
    elif level == 40:
        logger.error(message)
    elif level == 50:
        logger.critical(message)
    else:
        print('level not allowed')


