import logging
import os
from slack_log_handler import SlackLogHandler


def getMyLogger(ENV):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s ["+ENV+"] %(message)s","%m/%d %H:%M:%S")

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    slack = SlackLogHandler(
        'https://hooks.slack.com/services/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',
        username = 'headline soccer'
    )
    slack.setLevel(logging.INFO)
    slack.setFormatter(formatter)
    logger.addHandler(slack)
    return logger
