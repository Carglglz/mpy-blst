add_library(usermod_blst INTERFACE)

set(BLST_MOD_DIR ${CMAKE_CURRENT_LIST_DIR})
set(BLST_SRC_DIR "${BLST_MOD_DIR}/blst/src")
set(BLST_SRC_ASM_DIR "${BLST_MOD_DIR}/blst/build")

idf_build_set_property(COMPILE_OPTIONS "-Wno-unused-function" APPEND)
# idf_build_set_property(COMPILE_OPTIONS "-Wno-unused-value" APPEND)
target_include_directories(usermod_blst INTERFACE
    
    ${BLST_MOD_DIR}
    ${BLST_SRC_DIR}
    ${BLST_SRC_ASM_DIR}
    ${BLST_MOD_DIR}/blst/bindings

)


target_sources(usermod_blst INTERFACE
    ${BLST_MOD_DIR}/mod_blst.c
    ${BLST_SRC_DIR}/server.c
    ${BLST_SRC_ASM_DIR}/assembly.S
)

target_compile_options(usermod INTERFACE -D__BLST_PORTABLE__)

target_link_libraries(usermod INTERFACE usermod_blst)

