from ..complexities import constant


httclient_complexities = dict()

httclient_HTTPConnection_complexities = {
    'auto_open': constant,
    'close': constant,
    'connect': constant,
    'debuglevel': constant,
    'default_port': constant,
    'endheaders': constant,
    'getresponse': constant,
    'putheader': constant,
    'putrequest': constant,
    'request': constant,
    'response_class': constant,
    'send': constant,
    'set_debuglevel': constant,
    'set_tunnel': constant,
}

httclient_HTTPSConnection_complexities = {
    'auto_open': constant,
    'close': constant,
    'connect': constant,
    'debuglevel': constant,
    'default_port': constant,
    'endheaders': constant,
    'getresponse': constant,
    'putheader': constant,
    'putrequest': constant,
    'request': constant,
    'response_class': constant,
    'send': constant,
    'set_debuglevel': constant,
    'set_tunnel': constant,
}
