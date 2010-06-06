from distutils.core import setup
import py2exe
import psyco
psyco.full()

import matplotlib

setup(
    console=['newton_3.py'],
    name='newton_3.py',
    options={
             'py2exe': {
                        "dll_excludes": [
                        "iconv.dll","intl.dll","libatk-1.0-0.dll",
                        "libgdk_pixbuf-2.0-0.dll","libgdk-win32-2.0-0.dll",
                        "libglib-2.0-0.dll","libgmodule-2.0-0.dll",
                        "libgobject-2.0-0.dll","libgthread-2.0-0.dll",
                        "libgtk-win32-2.0-0.dll","libpango-1.0-0.dll",
                        "libpangowin32-1.0-0.dll"],
                        'packages' : ['matplotlib', 'pytz'],
                       }
            },
    data_files=matplotlib.get_py2exe_datafiles()
)

