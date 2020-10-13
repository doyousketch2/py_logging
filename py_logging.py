#! /usr/bin/env python3

import os
import logging

##  https://realpython.com/python-logging
##================================================================================================##
##  DEBUG,  INFO,  WARNING,  ERROR,  CRITICAL

log_level  = logging .DEBUG

date_time  = '%d %b\'%y  %H:%M:%S'  ##  strftime.org

##-----------------------------------------------------------------------------

posix_colors_available  = os .name == 'posix'

Black  = '\033[30m'
Red    = '\033[31m'
Green  = '\033[32m'
Yellow = '\033[33m'
Blue   = '\033[34m'
Pink   = '\033[35m'
Cyan   = '\033[36m'
White  = '\033[37m'

LightBlack  = '\033[1;30m'
LightRed    = '\033[1;31m'
LightGreen  = '\033[1;32m'
LightYellow = '\033[1;33m'
LightBlue   = '\033[1;34m'
LightPink   = '\033[1;35m'
LightCyan   = '\033[1;36m'
LightWhite  = '\033[1;37m'

Normal = '\033[0;39m'  ##  revert

commandline_bar  = LightPink +'-' *60 + Normal

current_module_name, ext  = os .path .splitext( __file__ )
log_name  = current_module_name +'.rst'  ##  reStructured Text

##================================================================================================##

logger  = logging .getLogger()
logger .setLevel( log_level )  ##  have to specify first, before denoting individual streams

commandline  = logging .StreamHandler()
file_output  = logging .FileHandler( log_name )

logger .addHandler( commandline )
logger .addHandler( file_output )

commandline .setLevel( log_level )
file_output .setLevel( log_level )

##-----------------------------------------------------------------------------

if posix_colors_available:
    cmd_header_format  = '{} user: {} %(name)s {} processID: {} %(process)d  %(message)s{}'\
    .format( LightBlue,  Normal,  LightBlue,  Normal,  commandline_bar )
else:  ##  screw Windows, no color for you
    cmd_header_format  = 'user:  %(name)s   processID:  %(process)d  %(message)s' +'-' *60

cmd_header_formatted  = logging .Formatter( fmt = cmd_header_format,  datefmt = date_time )

file_out_header_format  = '-' *80 +'\n**user: %(name)s  processID: %(process)d**  %(message)s'
file_out_header_formatted  = logging .Formatter( fmt = file_out_header_format,  datefmt = date_time )

commandline .setFormatter( cmd_header_formatted )
file_output .setFormatter( file_out_header_formatted )
logger .info( '\n' )  ##  print header

##-----------------------------------------------------------------------------

if posix_colors_available:
    commandline_format  = '{} %(levelname)s - {} %(message)s'.format( LightCyan, Normal )
else:  ##  screw Windows, no color for you
    commandline_format  = '%(levelname)s -  %(message)s'

commandline_formatted  = logging .Formatter( fmt = commandline_format,  datefmt = date_time )

file_out_format  = '%(asctime)s  %(levelname)s - %(message)s'
file_out_formatted  = logging .Formatter( fmt = file_out_format,  datefmt = date_time )

commandline .setFormatter( commandline_formatted )
file_output .setFormatter( file_out_formatted )

##-----------------------------------------------------------------------------

logger .debug( 'This is a debug message' )
logger .info( 'This is an info message' )

logger .warning( 'This is a warning message' )
logger .error( 'This is an error message' )
logger .critical( 'This is a critical message' )

##================================================================================================##

