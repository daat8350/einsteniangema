from distutils.core import setup
import py2exe
import glob

opts = {
    'py2exe': { 'packages': ['visual']
              }
       }

# Additional data files are required by matplotlib.  Note that the glob.glob routine
# doesn't seem to pick up the .matplotlib resource file, so I copy that separately.
# Do the same if you need to
setup(
    data_files = [( r'visual', glob.glob (r'C:\Python25\Lib\site-packages\visual\*.tga' )),
                  (r'visual',[r'C:\Python25\Lib\site-packages\visual\turbulence3.tga'])],
    name = 'selfoc',
    description = 'Selfoc fiber simulation',
    console = ['ex7.py']
    )
