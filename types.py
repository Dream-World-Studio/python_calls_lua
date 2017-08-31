import platform

appbit = 32 if platform.architecture()[0].find("32") != -1 else 64

TO luaconf.h 118