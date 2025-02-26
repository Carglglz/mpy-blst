
#include <py/mpconfig.h>
#include <py/misc.h>
#include <py/gc.h>
#include <py/runtime.h>
#include <string.h>
#include "mpy_binding_blst.h"


#undef alloca
#define alloca(s) mp_alloca(s)

void *mp_alloca(size_t size);

#define PRIVATE_KEY_SIZE 32
#define PUBLIC_KEY_SIZE 48
#define SIGNATURE_SIZE 96

#define BASIC_SCHEME_MPL "BLS_SIG_BLS12381G2_XMD:SHA-256_SSWU_RO_NUL_"
#define AUG_SCHEME_MPL "BLS_SIG_BLS12381G2_XMD:SHA-256_SSWU_RO_AUG_"
#define POP_SCHEME_MPL "BLS_SIG_BLS12381G2_XMD:SHA-256_SSWU_RO_POP_"
#define POPSIG_SCHEME_MPL "BLS_POP_BLS12381G2_XMD:SHA-256_SSWU_RO_POP_"
