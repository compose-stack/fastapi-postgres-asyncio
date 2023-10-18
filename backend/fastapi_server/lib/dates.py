import arrow

DATETIME_TZ_FORMAT = "YYYY-MM-DDTHH:mm:ssZZ"


def now(format=DATETIME_TZ_FORMAT):
    date = arrow.utcnow()
    if format:
        date = date.format(DATETIME_TZ_FORMAT)
    return date
