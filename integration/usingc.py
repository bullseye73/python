from ctypes import *
dll = windll.LoadLibrary('mydll')
# LibraryLoader(winDLL).LoadLibrary('mydll')
# WinDLL('mydll')

print(dll.Func("Hello", 1))
