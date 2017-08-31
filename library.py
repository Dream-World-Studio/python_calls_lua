import ctypes as __ctypes
import os as _os
from _ctypes import Union,Structure,_Pointer
CDLL = __ctypes.CDLL
if _os.name == "nt":
    luadll=CDLL("LUA53.dll")

