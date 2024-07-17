import os
# CPU options
ARCH='loongarch'
CPU ='la264'

if os.getenv('RTT_ROOT'):
    RTT_ROOT = os.getenv('RTT_ROOT')
else:
    RTT_ROOT = '../../..'

# toolchains options
CROSS_TOOL  = 'gcc'

if os.getenv('RTT_CC'):
	CROSS_TOOL = os.getenv('RTT_CC')

if  CROSS_TOOL == 'gcc':
	PLATFORM    = 'gcc'
	EXEC_PATH   = "/opt/loongson-gnu-toolchain-x86_64-loongarch64-linux-gnu/bin"
#	EXEC_PATH   = r'D:\opt\gcc\loongarch64-linux\bin'
else:
    print('================ERROR===========================')
    print('Not support %s yet!' % CROSS_TOOL)
    print('=================================================')
    exit(0)

if os.getenv('RTT_EXEC_PATH'):
	EXEC_PATH = os.getenv('RTT_EXEC_PATH')

BUILD       = 'debug'

#PREFIX = 'loongarch64-linux-'
PREFIX = 'loongarch64-linux-gnu-'
CC = PREFIX + 'gcc'
CXX = PREFIX + 'g++'
AS = PREFIX + 'gcc'
AR = PREFIX + 'ar'
LINK = PREFIX + 'gcc'
TARGET_EXT = 'elf'
SIZE = PREFIX + 'size'
OBJDUMP = PREFIX + 'objdump'
OBJCPY = PREFIX + 'objcopy'
READELF = PREFIX + 'readelf'

DEVICE = ' -march=loongarch64 -mabi=lp64s -msoft-float'
CFLAGS = DEVICE + ' -std=gnu11 -G0 -fno-pic -fno-builtin -fno-exceptions -ffunction-sections -fomit-frame-pointer'
AFLAGS = ' -c' + DEVICE + '  -fno-pic -fno-builtin -x assembler-with-cpp'
LFLAGS = DEVICE + ' -static -nostartfiles -Wl,--gc-sections,-Map=rt-thread.map,-cref,-u,Reset_Handler -T rt-thread.lds'
CXXFLAGS = CFLAGS

CPATH = ''
LPATH = ''

if BUILD == 'debug':
    CFLAGS += ' -O0 -gdwarf-2'
    AFLAGS += ' -gdwarf-2'
else:
    CFLAGS += ' -O2'

DUMP_ACTION = OBJDUMP + ' -D -S $TARGET > rt-thread.asm\n'
READELF_ACTION = READELF + ' -a $TARGET > rt-thread\n'
POST_ACTION = OBJCPY + ' -O binary $TARGET rt-thread.bin\n' + SIZE + ' $TARGET \n'
