from ..complexities import constant

io_complexities = dict()

io_bytesio_complexities = {
    'close': constant,
    'closed': constant,
    'detach': constant,
    'fileno': constant,
    'flush': constant,
    'getbuffer': constant,
    'getvalue': constant,
    'isatty': constant,
    'read': constant,
    'read1': constant,
    'readable': constant,
    'readinto': constant,
    'readinto1': constant,
    'readline': constant,
    'readlines': constant,
    'seek': constant,
    'seekable': constant,
    'tell': constant,
    'truncate': constant,
    'writable': constant,
    'write': constant,
    'writelines': constant,
}
