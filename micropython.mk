
# this file autodetected by py/py.mk based on its name

BLST_MOD_DIR := $(USERMOD_DIR)
BLST_SRC_DIR := $(BLST_MOD_DIR)/blst/src
BLST_SRC_ASM_DIR := $(BLST_MOD_DIR)/blst/build

SRC_USERMOD += $(BLST_MOD_DIR)/mod_blst.c

CLFAGS_USERMOD += -I$(BLST_SRC_DIR) -I$(BLST_MOD_DIR)/blst/bindings -D__BLST_PORTABLE__

CFLAGS_EXTRA += -Wno-unused-function  

# SRC_USERMOD_LIB_C += $(addprefix $(BLST_SRC_DIR)/, \
#                      server.c \
# 					)

SRC_USERMOD_LIB_C += $(addprefix $(BLST_MOD_DIR)/, \
                     server.c \
					)
SRC_USERMOD_LIB_ASM += $(BLST_SRC_ASM_DIR)/assembly.S


