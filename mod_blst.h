
#include <py/mpconfig.h>
#include <py/misc.h>
#include <py/gc.h>
#include <py/runtime.h>
#include <string.h>
#include "mpy_binding_blst.h"


#undef alloca
#define alloca(s) mp_alloca(s)

void *mp_alloca(size_t size);
