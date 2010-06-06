rem *** py2exe

rem ***** get rid of all the old files in the build folder
rd /S /Q build

rem ***** create the exe
setup.py py2exe

rem **** pause before exit
pause "done...hit a key to exit"