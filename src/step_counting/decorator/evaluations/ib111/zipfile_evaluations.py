from ..complexities import constant


zipfile_complexities = {
    'is_zipfile': constant,
}

zipfile_zipfile_complexities = {
    'close': constant,
    'comment': constant,
    'extract': constant,
    'extractall': constant,
    'fp': constant,
    'getinfo': constant,
    'infolist': constant,
    'namelist': constant,
    'open': constant,
    'printdir': constant,
    'read': constant,
    'setpassword': constant,
    'testzip': constant,
    'write': constant,
    'writestr': constant,
}
