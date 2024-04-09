from ..complexities import constant, linear


datetime_complexities = dict()

datetime_date_complexities = {
    'ctime': constant,
    'day': constant,
    'fromisocalendar': constant,
    'fromisoformat': constant,
    'fromordinal': constant,
    'fromtimestamp': constant,
    'isocalendar': constant,
    'isoformat': constant,
    'isoweekday': constant,
    'max': constant,
    'min': constant,
    'month': constant,
    'replace': constant,
    'resolution': constant,
    'strftime': constant,
    'timetuple': constant,
    'today': constant,
    'toordinal': constant,
    'weekday': constant,
    'year': linear,
}

datetime_datetime_complexities = {
    'astimezone': constant,
    'combine': constant,
    'ctime': constant,
    'date': constant,
    'day': constant,
    'dst': constant,
    'fold': constant,
    'fromisocalendar': constant,
    'fromisoformat': constant,
    'fromordinal': constant,
    'fromtimestamp': constant,
    'hour': constant,
    'isocalendar': constant,
    'isoformat': constant,
    'isoweekday': constant,
    'max': constant,
    'microsecond': constant,
    'min': constant,
    'minute': constant,
    'month': constant,
    'now': constant,
    'replace': constant,
    'resolution': constant,
    'second': constant,
    'strftime': constant,
    'strptime': constant,
    'time': constant,
    'timestamp': constant,
    'timetuple': constant,
    'timetz': constant,
    'today': constant,
    'toordinal': constant,
    'tzinfo': constant,
    'tzname': constant,
    'utcfromtimestamp': constant,
    'utcnow': constant,
    'utcoffset': constant,
    'utctimetuple': constant,
    'weekday': constant,
    'year': constant,
}

datetime_timedelta_complexities = {
    'dst': constant,
    'fold': constant,
    'fromisoformat': constant,
    'hour': constant,
    'isoformat': constant,
    'max': constant,
    'microsecond': constant,
    'min': constant,
    'minute': constant,
    'replace': constant,
    'resolution': constant,
    'second': constant,
    'strftime': constant,
    'tzinfo': constant,
    'tzname': constant,
    'utcoffset': constant,
}

datetime_time_complexities = {
    'days': constant,
    'max': constant,
    'microseconds': constant,
    'min': constant,
    'resolution': constant,
    'seconds': constant,
    'total_seconds': constant,
}
