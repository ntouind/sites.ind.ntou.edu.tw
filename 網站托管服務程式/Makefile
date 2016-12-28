PRODUCT_NAME=pop3-user-authentication
DEBUG=1

# uname --operating-system returns unsafe "GNU/Linux" in Ubuntu 16.04
OS_CATEGORY=$(shell uname --kernel-name)
# --hardware-platform and --processor are not portable according to `uname` itself
PLATFORM_CATEGORY=$(shell uname --machine)
LINKING_TYPE_DYNAMIC=dynamic
LINKING_TYPE_STATIC=static
LINKING_TYPE=${LINKING_TYPE_DYNAMIC}
FILENAME_COMPONENT_SEPARATOR=.
F_C_S=${FILENAME_COMPONENT_SEPARATOR}
FILENAME_EXTENSION_SOURCECODE_C=.c
FILENAME_EXTENSION_EXECUTABLE=.executable
CFLAGS_INCLUDE_DEBUG_SYMBOLS="-g"
ifeq (${DEBUG}, 1)
	CFLAGS_DEBUG=${CFLAGS_INCLUDE_DEBUG_SYMBOLS}
else
	CFLAGS_DEBUG=
endif
CFLAGS_LINKING_STATIC="-static"
ifeq ("${LINKING_TYPE}", "${LINKING_TYPE_STATIC}")
	CFLAGS_LINKING=${CFLAGS_LINKING_STATIC}
endif
CFLAGS=${CFLAGS_DEBUG} ${CFLAGS_LINKING}

# .PHONY: help
# help:
# 	echo "Just run `make`, run `make LINKING_TYPE=static` for static linking.\n"

.PHONY: all
all:
	gcc ${CFLAGS} -o ${PRODUCT_NAME}${F_C_S}${OS_CATEGORY}${F_C_S}${PLATFORM_CATEGORY}${F_C_S}${LINKING_TYPE}${FILENAME_EXTENSION_EXECUTABLE} ${PRODUCT_NAME}${FILENAME_EXTENSION_SOURCECODE_C}

.PHONY: clean
clean:
	rm --force *.executable
