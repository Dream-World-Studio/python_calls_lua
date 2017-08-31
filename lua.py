# define LUA_OK		0
# define LUA_YIELD	1
# define LUA_ERRRUN	2
# define LUA_ERRSYNTAX	3
# define LUA_ERRMEM	4
# define LUA_ERRGCMM	5
# define LUA_ERRERR	6

# ????typedef struct lua_State lua_State;
# define LUA_TNONE		(-1)

LUA_TNIL = 0
LUA_TBOOLEAN = 1
LUA_TLIGHTUSERDATA = 2
LUA_TNUMBER = 3
LUA_TSTRING = 4
LUA_TTABLE = 5
LUA_TFUNCTION = 6
LUA_TUSERDATA = 7
LUA_TTHREAD = 8

LUA_NUMTAGS = 9
LUA_RIDX_MAINTHREAD = 1
LUA_RIDX_GLOBALS = 2
LUA_RIDX_LAST = LUA_RIDX_GLOBALS

LUA_NUMBER= lua_Number

LUA_INTEGER= lua_Integer

LUA_UNSIGNED= lua_Unsigned

LUA_KCONTEXT =lua_KContext