# system configuration generated and used by the sysconfig module
build_time_vars = {'ABIFLAGS': '',
 'AC_APPLE_UNIVERSAL_BUILD': 0,
 'AIX_BUILDDATE': 0,
 'AIX_GENUINE_CPLUSPLUS': 0,
 'ALT_SOABI': 0,
 'ANDROID_API_LEVEL': 21,
 'AR': '/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-ar',
 'ARFLAGS': 'rcs',
 'BASECFLAGS': '-mfloat-abi=softfp -mfpu=vfpv3-d16 -Wno-unused-result '
               '-Wsign-compare -Wunreachable-code',
 'BASECPPFLAGS': '-IObjects -IInclude -IPython',
 'BASEMODLIBS': '',
 'BINDIR': '/usr/local/bin',
 'BINLIBDEST': '/usr/local/lib/python3.9',
 'BLDLIBRARY': '-L. -lpython3.9',
 'BLDSHARED': '/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang '
              '-target armv7a-linux-androideabi21 -fomit-frame-pointer '
              '-march=armv7-a -mfloat-abi=softfp -mfpu=vfp -mthumb -fPIC '
              '-pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions '
              '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/libs_collections/taskapp/armeabi-v7a '
              '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3/obj/local/armeabi-v7a '
              '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/.libs '
              '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1 '
              '-L/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/arm-linux-androideabi/21 '
              '-march=armv7-a -Wl,--fix-cortex-a8   '
              '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/libs_collections/taskapp/armeabi-v7a '
              '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3/obj/local/armeabi-v7a '
              '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/.libs '
              '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1 '
              '-L/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/arm-linux-androideabi/21',
 'BUILDEXE': '',
 'BUILDPYTHON': 'python',
 'BUILD_GNU_TYPE': 'x86_64-pc-linux-gnu',
 'BYTESTR_DEPS': '\\',
 'CC': '/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/bin/armv7a-linux-androideabi21-clang',
 'CCSHARED': '',
 'CFLAGS': '-mfloat-abi=softfp -mfpu=vfpv3-d16 -Wno-unused-result '
           '-Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall '
           '-fPIC -DANDROID -fPIC -DANDROID',
 'CFLAGSFORSHARED': '',
 'CFLAGS_ALIASING': '-fno-strict-aliasing',
 'CFLAGS_NODIST': '',
 'CONFIGFILES': 'configure configure.ac acconfig.h pyconfig.h.in '
                'Makefile.pre.in',
 'CONFIGURE_CFLAGS': '-fPIC -DANDROID',
 'CONFIGURE_CFLAGS_NODIST': '-std=c99 -Wextra -Wno-unused-result '
                            '-Wno-unused-parameter '
                            '-Wno-missing-field-initializers '
                            '-Wstrict-prototypes '
                            '-Werror=implicit-function-declaration '
                            '-fvisibility=hidden',
 'CONFIGURE_CPPFLAGS': '-DANDROID '
                       '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
                       '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/python-installs/taskapp/armeabi-v7a/include/python3.9 '
                       '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3 '
                       '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/include '
                       '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include '
                       '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/internal '
                       '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/openssl '
                       '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include',
 'CONFIGURE_LDFLAGS': '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/libs_collections/taskapp/armeabi-v7a '
                      '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3/obj/local/armeabi-v7a '
                      '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/.libs '
                      '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1 '
                      '-L/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/arm-linux-androideabi/21 '
                      '-march=armv7-a -Wl,--fix-cortex-a8',
 'CONFIGURE_LDFLAGS_NODIST': '',
 'CONFIG_ARGS': "'--host=arm-linux-androideabi' '--build=x86_64-pc-linux-gnu' "
                "'--enable-shared' '--enable-ipv6' 'ac_cv_file__dev_ptmx=yes' "
                "'ac_cv_file__dev_ptc=no' '--without-ensurepip' "
                "'ac_cv_little_endian_double=yes' '--prefix=/usr/local' "
                "'--exec-prefix=/usr/local' "
                "'--enable-loadable-sqlite-extensions' "
                "'--with-openssl=/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1' "
                "'build_alias=x86_64-pc-linux-gnu' "
                "'host_alias=arm-linux-androideabi' "
                "'CC=/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/bin/armv7a-linux-androideabi21-clang' "
                "'CFLAGS=-fPIC -DANDROID' 'LDFLAGS=  "
                '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/libs_collections/taskapp/armeabi-v7a '
                '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3/obj/local/armeabi-v7a '
                '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/.libs '
                '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1 '
                "-L/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/arm-linux-androideabi/21' "
                "'LIBS= -lsqlite3 -lffi -lcrypto1.1 -lssl1.1 -lz' "
                "'CPPFLAGS=-DANDROID "
                '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/python-installs/taskapp/armeabi-v7a/include/python3.9 '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3 '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/include '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/internal '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/openssl '
                "-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include' "
                "'PKG_CONFIG_PATH=/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi'",
 'CONFINCLUDEDIR': '/usr/local/include',
 'CONFINCLUDEPY': '/usr/local/include/python3.9',
 'COREPYTHONPATH': '',
 'COVERAGE_INFO': '/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/android-build/coverage.info',
 'COVERAGE_REPORT': '/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/android-build/lcov-report',
 'COVERAGE_REPORT_OPTIONS': '--no-branch-coverage --title "CPython lcov '
                            'report"',
 'CPPFLAGS': '-IObjects -IInclude -IPython -I. '
             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/Include '
             '-DANDROID '
             '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/python-installs/taskapp/armeabi-v7a/include/python3.9 '
             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3 '
             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/include '
             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include '
             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/internal '
             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/openssl '
             '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
             '-DANDROID '
             '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/python-installs/taskapp/armeabi-v7a/include/python3.9 '
             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3 '
             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/include '
             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include '
             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/internal '
             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/openssl '
             '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include',
 'CXX': '/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++ '
        '-target armv7a-linux-androideabi21 -fomit-frame-pointer '
        '-march=armv7-a -mfloat-abi=softfp -mfpu=vfp -mthumb -fPIC',
 'DESTDIRS': '/usr/local /usr/local/lib /usr/local/lib/python3.9 '
             '/usr/local/lib/python3.9/lib-dynload',
 'DESTLIB': '/usr/local/lib/python3.9',
 'DESTPATH': '',
 'DESTSHARED': '/usr/local/lib/python3.9/lib-dynload',
 'DFLAGS': '',
 'DIRMODE': 755,
 'DIST': 'README.rst ChangeLog configure configure.ac acconfig.h pyconfig.h.in '
         'Makefile.pre.in Include Lib Misc Ext-dummy',
 'DISTDIRS': 'Include Lib Misc Ext-dummy',
 'DISTFILES': 'README.rst ChangeLog configure configure.ac acconfig.h '
              'pyconfig.h.in Makefile.pre.in',
 'DLINCLDIR': '.',
 'DLLLIBRARY': '',
 'DOUBLE_IS_ARM_MIXED_ENDIAN_IEEE754': 0,
 'DOUBLE_IS_BIG_ENDIAN_IEEE754': 0,
 'DOUBLE_IS_LITTLE_ENDIAN_IEEE754': 1,
 'DTRACE': '',
 'DTRACE_DEPS': '\\',
 'DTRACE_HEADERS': '',
 'DTRACE_OBJS': '',
 'DYNLOADFILE': 'dynload_shlib.o',
 'ENABLE_IPV6': 1,
 'ENSUREPIP': 'no',
 'EXE': '',
 'EXEMODE': 755,
 'EXPORTSFROM': '',
 'EXPORTSYMS': '',
 'EXTRATESTOPTS': '',
 'EXTRA_CFLAGS': '',
 'EXT_SUFFIX': '.cpython-39.so',
 'FILEMODE': 644,
 'FLOAT_WORDS_BIGENDIAN': 0,
 'FLOCK_NEEDS_LIBBSD': 0,
 'GETPGRP_HAVE_ARG': 0,
 'GITBRANCH': '',
 'GITTAG': '',
 'GITVERSION': '',
 'GNULD': 'yes',
 'HAVE_ACCEPT4': 1,
 'HAVE_ACOSH': 1,
 'HAVE_ADDRINFO': 1,
 'HAVE_ALARM': 1,
 'HAVE_ALIGNED_REQUIRED': 1,
 'HAVE_ALLOCA_H': 1,
 'HAVE_ALTZONE': 0,
 'HAVE_ASINH': 1,
 'HAVE_ASM_TYPES_H': 1,
 'HAVE_ATANH': 1,
 'HAVE_BIND_TEXTDOMAIN_CODESET': 0,
 'HAVE_BLUETOOTH_BLUETOOTH_H': 0,
 'HAVE_BLUETOOTH_H': 0,
 'HAVE_BROKEN_MBSTOWCS': 0,
 'HAVE_BROKEN_NICE': 0,
 'HAVE_BROKEN_PIPE_BUF': 0,
 'HAVE_BROKEN_POLL': 0,
 'HAVE_BROKEN_POSIX_SEMAPHORES': 0,
 'HAVE_BROKEN_PTHREAD_SIGMASK': 0,
 'HAVE_BROKEN_SEM_GETVALUE': 1,
 'HAVE_BROKEN_UNSETENV': 0,
 'HAVE_BUILTIN_ATOMIC': 1,
 'HAVE_CHFLAGS': 0,
 'HAVE_CHOWN': 1,
 'HAVE_CHROOT': 1,
 'HAVE_CLOCK': 1,
 'HAVE_CLOCK_GETRES': 1,
 'HAVE_CLOCK_GETTIME': 1,
 'HAVE_CLOCK_SETTIME': 1,
 'HAVE_COMPUTED_GOTOS': 0,
 'HAVE_CONFSTR': 0,
 'HAVE_CONIO_H': 0,
 'HAVE_COPYSIGN': 1,
 'HAVE_COPY_FILE_RANGE': 0,
 'HAVE_CRYPT_H': 0,
 'HAVE_CRYPT_R': 0,
 'HAVE_CTERMID': 0,
 'HAVE_CTERMID_R': 0,
 'HAVE_CURSES_FILTER': 0,
 'HAVE_CURSES_H': 0,
 'HAVE_CURSES_HAS_KEY': 0,
 'HAVE_CURSES_IMMEDOK': 0,
 'HAVE_CURSES_IS_PAD': 0,
 'HAVE_CURSES_IS_TERM_RESIZED': 0,
 'HAVE_CURSES_RESIZETERM': 0,
 'HAVE_CURSES_RESIZE_TERM': 0,
 'HAVE_CURSES_SYNCOK': 0,
 'HAVE_CURSES_TYPEAHEAD': 0,
 'HAVE_CURSES_USE_ENV': 0,
 'HAVE_CURSES_WCHGAT': 0,
 'HAVE_DECL_ISFINITE': 1,
 'HAVE_DECL_ISINF': 1,
 'HAVE_DECL_ISNAN': 1,
 'HAVE_DECL_RTLD_DEEPBIND': 0,
 'HAVE_DECL_RTLD_GLOBAL': 1,
 'HAVE_DECL_RTLD_LAZY': 1,
 'HAVE_DECL_RTLD_LOCAL': 1,
 'HAVE_DECL_RTLD_MEMBER': 0,
 'HAVE_DECL_RTLD_NODELETE': 1,
 'HAVE_DECL_RTLD_NOLOAD': 1,
 'HAVE_DECL_RTLD_NOW': 1,
 'HAVE_DECL_TZNAME': 0,
 'HAVE_DEVICE_MACROS': 1,
 'HAVE_DEV_PTC': 0,
 'HAVE_DEV_PTMX': 1,
 'HAVE_DIRECT_H': 0,
 'HAVE_DIRENT_D_TYPE': 1,
 'HAVE_DIRENT_H': 1,
 'HAVE_DIRFD': 1,
 'HAVE_DLFCN_H': 1,
 'HAVE_DLOPEN': 1,
 'HAVE_DUP2': 1,
 'HAVE_DUP3': 1,
 'HAVE_DYLD_SHARED_CACHE_CONTAINS_PATH': 0,
 'HAVE_DYNAMIC_LOADING': 1,
 'HAVE_ENDIAN_H': 1,
 'HAVE_EPOLL': 1,
 'HAVE_EPOLL_CREATE1': 1,
 'HAVE_ERF': 1,
 'HAVE_ERFC': 1,
 'HAVE_ERRNO_H': 1,
 'HAVE_EXECV': 1,
 'HAVE_EXPLICIT_BZERO': 0,
 'HAVE_EXPLICIT_MEMSET': 0,
 'HAVE_EXPM1': 1,
 'HAVE_FACCESSAT': 1,
 'HAVE_FCHDIR': 1,
 'HAVE_FCHMOD': 1,
 'HAVE_FCHMODAT': 1,
 'HAVE_FCHOWN': 1,
 'HAVE_FCHOWNAT': 1,
 'HAVE_FCNTL_H': 1,
 'HAVE_FDATASYNC': 1,
 'HAVE_FDOPENDIR': 1,
 'HAVE_FDWALK': 0,
 'HAVE_FEXECVE': 0,
 'HAVE_FINITE': 1,
 'HAVE_FLOCK': 1,
 'HAVE_FORK': 1,
 'HAVE_FORKPTY': 0,
 'HAVE_FPATHCONF': 1,
 'HAVE_FSEEK64': 0,
 'HAVE_FSEEKO': 1,
 'HAVE_FSTATAT': 1,
 'HAVE_FSTATVFS': 1,
 'HAVE_FSYNC': 1,
 'HAVE_FTELL64': 0,
 'HAVE_FTELLO': 1,
 'HAVE_FTIME': 0,
 'HAVE_FTRUNCATE': 1,
 'HAVE_FUTIMENS': 1,
 'HAVE_FUTIMES': 0,
 'HAVE_FUTIMESAT': 0,
 'HAVE_GAI_STRERROR': 1,
 'HAVE_GAMMA': 1,
 'HAVE_GCC_ASM_FOR_MC68881': 0,
 'HAVE_GCC_ASM_FOR_X64': 0,
 'HAVE_GCC_ASM_FOR_X87': 0,
 'HAVE_GCC_UINT128_T': 0,
 'HAVE_GETADDRINFO': 1,
 'HAVE_GETC_UNLOCKED': 1,
 'HAVE_GETENTROPY': 0,
 'HAVE_GETGRGID_R': 0,
 'HAVE_GETGRNAM_R': 0,
 'HAVE_GETGROUPLIST': 1,
 'HAVE_GETGROUPS': 1,
 'HAVE_GETHOSTBYNAME': 0,
 'HAVE_GETHOSTBYNAME_R': 1,
 'HAVE_GETHOSTBYNAME_R_3_ARG': 0,
 'HAVE_GETHOSTBYNAME_R_5_ARG': 0,
 'HAVE_GETHOSTBYNAME_R_6_ARG': 1,
 'HAVE_GETITIMER': 1,
 'HAVE_GETLOADAVG': 0,
 'HAVE_GETLOGIN': 1,
 'HAVE_GETNAMEINFO': 1,
 'HAVE_GETPAGESIZE': 1,
 'HAVE_GETPEERNAME': 1,
 'HAVE_GETPGID': 1,
 'HAVE_GETPGRP': 1,
 'HAVE_GETPID': 1,
 'HAVE_GETPRIORITY': 1,
 'HAVE_GETPWENT': 0,
 'HAVE_GETPWNAM_R': 1,
 'HAVE_GETPWUID_R': 1,
 'HAVE_GETRANDOM': 0,
 'HAVE_GETRANDOM_SYSCALL': 1,
 'HAVE_GETRESGID': 1,
 'HAVE_GETRESUID': 1,
 'HAVE_GETSID': 1,
 'HAVE_GETSPENT': 0,
 'HAVE_GETSPNAM': 0,
 'HAVE_GETWD': 0,
 'HAVE_GLIBC_MEMMOVE_BUG': 0,
 'HAVE_GRP_H': 1,
 'HAVE_HSTRERROR': 1,
 'HAVE_HTOLE64': 1,
 'HAVE_HYPOT': 1,
 'HAVE_IEEEFP_H': 0,
 'HAVE_IF_NAMEINDEX': 0,
 'HAVE_INET_ATON': 1,
 'HAVE_INET_PTON': 1,
 'HAVE_INITGROUPS': 1,
 'HAVE_INTTYPES_H': 1,
 'HAVE_IO_H': 0,
 'HAVE_IPA_PURE_CONST_BUG': 0,
 'HAVE_KILL': 1,
 'HAVE_KILLPG': 1,
 'HAVE_KQUEUE': 0,
 'HAVE_LANGINFO_H': 1,
 'HAVE_LARGEFILE_SUPPORT': 1,
 'HAVE_LCHFLAGS': 0,
 'HAVE_LCHMOD': 0,
 'HAVE_LCHOWN': 1,
 'HAVE_LGAMMA': 1,
 'HAVE_LIBDL': 1,
 'HAVE_LIBDLD': 0,
 'HAVE_LIBIEEE': 0,
 'HAVE_LIBINTL_H': 0,
 'HAVE_LIBREADLINE': 0,
 'HAVE_LIBRESOLV': 0,
 'HAVE_LIBSENDFILE': 0,
 'HAVE_LIBUTIL_H': 0,
 'HAVE_LIBUUID': 0,
 'HAVE_LINK': 1,
 'HAVE_LINKAT': 1,
 'HAVE_LINUX_CAN_BCM_H': 1,
 'HAVE_LINUX_CAN_H': 1,
 'HAVE_LINUX_CAN_J1939_H': 1,
 'HAVE_LINUX_CAN_RAW_FD_FRAMES': 1,
 'HAVE_LINUX_CAN_RAW_H': 1,
 'HAVE_LINUX_CAN_RAW_JOIN_FILTERS': 1,
 'HAVE_LINUX_MEMFD_H': 1,
 'HAVE_LINUX_NETLINK_H': 1,
 'HAVE_LINUX_QRTR_H': 1,
 'HAVE_LINUX_RANDOM_H': 1,
 'HAVE_LINUX_TIPC_H': 1,
 'HAVE_LINUX_VM_SOCKETS_H': 1,
 'HAVE_LINUX_WAIT_H': 1,
 'HAVE_LOCKF': 0,
 'HAVE_LOG1P': 1,
 'HAVE_LOG2': 1,
 'HAVE_LONG_DOUBLE': 1,
 'HAVE_LSTAT': 1,
 'HAVE_LUTIMES': 0,
 'HAVE_MADVISE': 1,
 'HAVE_MAKEDEV': 1,
 'HAVE_MBRTOWC': 1,
 'HAVE_MEMFD_CREATE': 0,
 'HAVE_MEMORY_H': 1,
 'HAVE_MEMRCHR': 1,
 'HAVE_MKDIRAT': 1,
 'HAVE_MKFIFO': 1,
 'HAVE_MKFIFOAT': 0,
 'HAVE_MKNOD': 1,
 'HAVE_MKNODAT': 1,
 'HAVE_MKTIME': 1,
 'HAVE_MMAP': 1,
 'HAVE_MREMAP': 1,
 'HAVE_NCURSES_H': 0,
 'HAVE_NDIR_H': 0,
 'HAVE_NETPACKET_PACKET_H': 1,
 'HAVE_NET_IF_H': 1,
 'HAVE_NICE': 1,
 'HAVE_NON_UNICODE_WCHAR_T_REPRESENTATION': 0,
 'HAVE_OPENAT': 1,
 'HAVE_OPENPTY': 0,
 'HAVE_PATHCONF': 1,
 'HAVE_PAUSE': 1,
 'HAVE_PIPE2': 1,
 'HAVE_PLOCK': 0,
 'HAVE_POLL': 1,
 'HAVE_POLL_H': 1,
 'HAVE_POSIX_FADVISE': 1,
 'HAVE_POSIX_FALLOCATE': 1,
 'HAVE_POSIX_SPAWN': 0,
 'HAVE_POSIX_SPAWNP': 0,
 'HAVE_PREAD': 1,
 'HAVE_PREADV': 0,
 'HAVE_PREADV2': 0,
 'HAVE_PRLIMIT': 0,
 'HAVE_PROCESS_H': 0,
 'HAVE_PROTOTYPES': 1,
 'HAVE_PTHREAD_CONDATTR_SETCLOCK': 1,
 'HAVE_PTHREAD_DESTRUCTOR': 0,
 'HAVE_PTHREAD_GETCPUCLOCKID': 1,
 'HAVE_PTHREAD_H': 1,
 'HAVE_PTHREAD_INIT': 0,
 'HAVE_PTHREAD_KILL': 1,
 'HAVE_PTHREAD_SIGMASK': 1,
 'HAVE_PTY_H': 1,
 'HAVE_PWRITE': 1,
 'HAVE_PWRITEV': 0,
 'HAVE_PWRITEV2': 0,
 'HAVE_READLINK': 1,
 'HAVE_READLINKAT': 1,
 'HAVE_READV': 1,
 'HAVE_REALPATH': 1,
 'HAVE_RENAMEAT': 1,
 'HAVE_RL_APPEND_HISTORY': 0,
 'HAVE_RL_CATCH_SIGNAL': 0,
 'HAVE_RL_COMPLETION_APPEND_CHARACTER': 0,
 'HAVE_RL_COMPLETION_DISPLAY_MATCHES_HOOK': 0,
 'HAVE_RL_COMPLETION_MATCHES': 0,
 'HAVE_RL_COMPLETION_SUPPRESS_APPEND': 0,
 'HAVE_RL_PRE_INPUT_HOOK': 0,
 'HAVE_RL_RESIZE_TERMINAL': 0,
 'HAVE_ROUND': 1,
 'HAVE_RTPSPAWN': 0,
 'HAVE_SCHED_GET_PRIORITY_MAX': 1,
 'HAVE_SCHED_H': 1,
 'HAVE_SCHED_RR_GET_INTERVAL': 1,
 'HAVE_SCHED_SETAFFINITY': 1,
 'HAVE_SCHED_SETPARAM': 1,
 'HAVE_SCHED_SETSCHEDULER': 1,
 'HAVE_SEM_CLOCKWAIT': 0,
 'HAVE_SEM_GETVALUE': 1,
 'HAVE_SEM_OPEN': 1,
 'HAVE_SEM_TIMEDWAIT': 1,
 'HAVE_SEM_UNLINK': 1,
 'HAVE_SENDFILE': 1,
 'HAVE_SETEGID': 1,
 'HAVE_SETEUID': 1,
 'HAVE_SETGID': 1,
 'HAVE_SETGROUPS': 1,
 'HAVE_SETHOSTNAME': 0,
 'HAVE_SETITIMER': 1,
 'HAVE_SETLOCALE': 1,
 'HAVE_SETPGID': 1,
 'HAVE_SETPGRP': 1,
 'HAVE_SETPRIORITY': 1,
 'HAVE_SETREGID': 1,
 'HAVE_SETRESGID': 1,
 'HAVE_SETRESUID': 1,
 'HAVE_SETREUID': 1,
 'HAVE_SETSID': 1,
 'HAVE_SETUID': 1,
 'HAVE_SETVBUF': 1,
 'HAVE_SHADOW_H': 0,
 'HAVE_SHM_OPEN': 0,
 'HAVE_SHM_UNLINK': 0,
 'HAVE_SIGACTION': 1,
 'HAVE_SIGALTSTACK': 1,
 'HAVE_SIGFILLSET': 1,
 'HAVE_SIGINFO_T_SI_BAND': 1,
 'HAVE_SIGINTERRUPT': 1,
 'HAVE_SIGNAL_H': 1,
 'HAVE_SIGPENDING': 1,
 'HAVE_SIGRELSE': 0,
 'HAVE_SIGTIMEDWAIT': 0,
 'HAVE_SIGWAIT': 1,
 'HAVE_SIGWAITINFO': 0,
 'HAVE_SNPRINTF': 1,
 'HAVE_SOCKADDR_ALG': 1,
 'HAVE_SOCKADDR_SA_LEN': 0,
 'HAVE_SOCKADDR_STORAGE': 1,
 'HAVE_SOCKETPAIR': 1,
 'HAVE_SPAWN_H': 1,
 'HAVE_SSIZE_T': 1,
 'HAVE_STATVFS': 1,
 'HAVE_STAT_TV_NSEC': 1,
 'HAVE_STAT_TV_NSEC2': 0,
 'HAVE_STDARG_PROTOTYPES': 1,
 'HAVE_STDINT_H': 1,
 'HAVE_STDLIB_H': 1,
 'HAVE_STD_ATOMIC': 1,
 'HAVE_STRDUP': 1,
 'HAVE_STRFTIME': 1,
 'HAVE_STRINGS_H': 1,
 'HAVE_STRING_H': 1,
 'HAVE_STRLCPY': 1,
 'HAVE_STROPTS_H': 0,
 'HAVE_STRSIGNAL': 1,
 'HAVE_STRUCT_PASSWD_PW_GECOS': 1,
 'HAVE_STRUCT_PASSWD_PW_PASSWD': 1,
 'HAVE_STRUCT_STAT_ST_BIRTHTIME': 0,
 'HAVE_STRUCT_STAT_ST_BLKSIZE': 1,
 'HAVE_STRUCT_STAT_ST_BLOCKS': 1,
 'HAVE_STRUCT_STAT_ST_FLAGS': 0,
 'HAVE_STRUCT_STAT_ST_GEN': 0,
 'HAVE_STRUCT_STAT_ST_RDEV': 1,
 'HAVE_STRUCT_TM_TM_ZONE': 1,
 'HAVE_SYMLINK': 1,
 'HAVE_SYMLINKAT': 1,
 'HAVE_SYNC': 1,
 'HAVE_SYSCONF': 1,
 'HAVE_SYSEXITS_H': 1,
 'HAVE_SYS_AUDIOIO_H': 0,
 'HAVE_SYS_BSDTTY_H': 0,
 'HAVE_SYS_DEVPOLL_H': 0,
 'HAVE_SYS_DIR_H': 0,
 'HAVE_SYS_ENDIAN_H': 1,
 'HAVE_SYS_EPOLL_H': 1,
 'HAVE_SYS_EVENT_H': 0,
 'HAVE_SYS_FILE_H': 1,
 'HAVE_SYS_IOCTL_H': 1,
 'HAVE_SYS_KERN_CONTROL_H': 0,
 'HAVE_SYS_LOADAVG_H': 0,
 'HAVE_SYS_LOCK_H': 0,
 'HAVE_SYS_MEMFD_H': 0,
 'HAVE_SYS_MKDEV_H': 0,
 'HAVE_SYS_MMAN_H': 1,
 'HAVE_SYS_MODEM_H': 0,
 'HAVE_SYS_NDIR_H': 0,
 'HAVE_SYS_PARAM_H': 1,
 'HAVE_SYS_POLL_H': 1,
 'HAVE_SYS_RANDOM_H': 1,
 'HAVE_SYS_RESOURCE_H': 1,
 'HAVE_SYS_SELECT_H': 1,
 'HAVE_SYS_SENDFILE_H': 1,
 'HAVE_SYS_SOCKET_H': 1,
 'HAVE_SYS_STATVFS_H': 1,
 'HAVE_SYS_STAT_H': 1,
 'HAVE_SYS_SYSCALL_H': 1,
 'HAVE_SYS_SYSMACROS_H': 1,
 'HAVE_SYS_SYS_DOMAIN_H': 0,
 'HAVE_SYS_TERMIO_H': 0,
 'HAVE_SYS_TIMES_H': 1,
 'HAVE_SYS_TIME_H': 1,
 'HAVE_SYS_TYPES_H': 1,
 'HAVE_SYS_UIO_H': 1,
 'HAVE_SYS_UN_H': 1,
 'HAVE_SYS_UTSNAME_H': 1,
 'HAVE_SYS_WAIT_H': 1,
 'HAVE_SYS_XATTR_H': 1,
 'HAVE_TCGETPGRP': 1,
 'HAVE_TCSETPGRP': 1,
 'HAVE_TEMPNAM': 1,
 'HAVE_TERMIOS_H': 1,
 'HAVE_TERM_H': 0,
 'HAVE_TGAMMA': 1,
 'HAVE_TIMEGM': 1,
 'HAVE_TIMES': 1,
 'HAVE_TMPFILE': 1,
 'HAVE_TMPNAM': 1,
 'HAVE_TMPNAM_R': 0,
 'HAVE_TM_ZONE': 1,
 'HAVE_TRUNCATE': 1,
 'HAVE_TZNAME': 0,
 'HAVE_UCS4_TCL': 0,
 'HAVE_UNAME': 1,
 'HAVE_UNISTD_H': 1,
 'HAVE_UNLINKAT': 1,
 'HAVE_USABLE_WCHAR_T': 0,
 'HAVE_UTIL_H': 0,
 'HAVE_UTIMENSAT': 1,
 'HAVE_UTIMES': 1,
 'HAVE_UTIME_H': 1,
 'HAVE_UUID_CREATE': 0,
 'HAVE_UUID_ENC_BE': 0,
 'HAVE_UUID_GENERATE_TIME_SAFE': 0,
 'HAVE_UUID_H': 0,
 'HAVE_UUID_UUID_H': 0,
 'HAVE_WAIT3': 0,
 'HAVE_WAIT4': 1,
 'HAVE_WAITID': 1,
 'HAVE_WAITPID': 1,
 'HAVE_WCHAR_H': 1,
 'HAVE_WCSCOLL': 1,
 'HAVE_WCSFTIME': 1,
 'HAVE_WCSXFRM': 1,
 'HAVE_WMEMCMP': 1,
 'HAVE_WORKING_TZSET': 0,
 'HAVE_WRITEV': 1,
 'HAVE_X509_VERIFY_PARAM_SET1_HOST': 1,
 'HAVE_ZLIB_COPY': 1,
 'HAVE__GETPTY': 0,
 'HOST_GNU_TYPE': 'arm-unknown-linux-androideabi',
 'INCLDIRSTOMAKE': '/usr/local/include /usr/local/include '
                   '/usr/local/include/python3.9 /usr/local/include/python3.9',
 'INCLUDEDIR': '/usr/local/include',
 'INCLUDEPY': '/usr/local/include/python3.9',
 'INSTALL': '/usr/bin/install -c',
 'INSTALL_DATA': '/usr/bin/install -c -m 644',
 'INSTALL_PROGRAM': '/usr/bin/install -c',
 'INSTALL_SCRIPT': '/usr/bin/install -c',
 'INSTALL_SHARED': '/usr/bin/install -c -m 755',
 'INSTSONAME': 'libpython3.9.so.1.0',
 'IO_H': 'Modules/_io/_iomodule.h',
 'IO_OBJS': '\\',
 'LDCXXSHARED': '/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang '
                '-target armv7a-linux-androideabi21 -fomit-frame-pointer '
                '-march=armv7-a -mfloat-abi=softfp -mfpu=vfp -mthumb -fPIC '
                '-pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions',
 'LDFLAGS': '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/libs_collections/taskapp/armeabi-v7a '
            '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3/obj/local/armeabi-v7a '
            '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/.libs '
            '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1 '
            '-L/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/arm-linux-androideabi/21 '
            '-march=armv7-a -Wl,--fix-cortex-a8   '
            '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/libs_collections/taskapp/armeabi-v7a '
            '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3/obj/local/armeabi-v7a '
            '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/.libs '
            '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1 '
            '-L/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/arm-linux-androideabi/21',
 'LDFLAGS_NODIST': '',
 'LDLIBRARY': 'libpython3.9.so',
 'LDLIBRARYDIR': '',
 'LDSHARED': '/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang '
             '-target armv7a-linux-androideabi21 -fomit-frame-pointer '
             '-march=armv7-a -mfloat-abi=softfp -mfpu=vfp -mthumb -fPIC '
             '-pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions '
             '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/libs_collections/taskapp/armeabi-v7a '
             '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3/obj/local/armeabi-v7a '
             '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/.libs '
             '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1 '
             '-L/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/arm-linux-androideabi/21 '
             '-march=armv7-a -Wl,--fix-cortex-a8   '
             '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/libs_collections/taskapp/armeabi-v7a '
             '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3/obj/local/armeabi-v7a '
             '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/.libs '
             '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1 '
             '-L/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/arm-linux-androideabi/21',
 'LDVERSION': '3.9',
 'LIBC': '',
 'LIBDEST': '/usr/local/lib/python3.9',
 'LIBDIR': '/usr/local/lib',
 'LIBFFI_INCLUDEDIR': '/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/include',
 'LIBM': '-lm',
 'LIBOBJDIR': 'Python/',
 'LIBOBJS': '',
 'LIBPC': '/usr/local/lib/pkgconfig',
 'LIBPL': '/usr/local/lib/python3.9/config-3.9',
 'LIBPYTHON': '-lpython3.9',
 'LIBRARY': 'libpython3.9.a',
 'LIBRARY_OBJS': '\\',
 'LIBRARY_OBJS_OMIT_FROZEN': '\\',
 'LIBS': '-ldl  -lsqlite3 -lffi -lcrypto1.1 -lssl1.1 -lz -lm',
 'LIBSUBDIRS': 'tkinter tkinter/test tkinter/test/test_tkinter \\',
 'LINKCC': '/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/bin/armv7a-linux-androideabi21-clang',
 'LINKFORSHARED': '-pie -Xlinker -export-dynamic',
 'LIPO_32BIT_FLAGS': '',
 'LIPO_INTEL64_FLAGS': '',
 'LLVM_PROF_ERR': 'no',
 'LLVM_PROF_FILE': 'LLVM_PROFILE_FILE="code-%p.profclangr"',
 'LLVM_PROF_MERGER': '/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-profdata '
                     'merge -output=code.profclangd *.profclangr',
 'LN': 'ln',
 'LOCALMODLIBS': '',
 'MACHDEP': 'linux',
 'MACHDEP_OBJS': '',
 'MACHDESTLIB': '/usr/local/lib/python3.9',
 'MACOSX_DEPLOYMENT_TARGET': '',
 'MAINCC': '/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/bin/armv7a-linux-androideabi21-clang',
 'MAJOR_IN_MKDEV': 0,
 'MAJOR_IN_SYSMACROS': 1,
 'MAKESETUP': '/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/Modules/makesetup',
 'MANDIR': '/usr/local/share/man',
 'MKDIR_P': '/usr/bin/mkdir -p',
 'MODBUILT_NAMES': 'posix  errno  pwd  _sre  _codecs  _weakref  _functools  '
                   '_operator  _collections  _abc  itertools  atexit  _signal  '
                   '_stat  time  _thread  _locale  _io  faulthandler  '
                   '_tracemalloc  _peg_parser  _symtable  xxsubtype',
 'MODDISABLED_NAMES': '',
 'MODLIBS': '',
 'MODOBJS': 'Modules/posixmodule.o  Modules/errnomodule.o  '
            'Modules/pwdmodule.o  Modules/_sre.o  Modules/_codecsmodule.o  '
            'Modules/_weakref.o  Modules/_functoolsmodule.o  '
            'Modules/_operator.o  Modules/_collectionsmodule.o  '
            'Modules/_abc.o  Modules/itertoolsmodule.o  '
            'Modules/atexitmodule.o  Modules/signalmodule.o  Modules/_stat.o  '
            'Modules/timemodule.o  Modules/_threadmodule.o  '
            'Modules/_localemodule.o  Modules/_iomodule.o Modules/iobase.o '
            'Modules/fileio.o Modules/bytesio.o Modules/bufferedio.o '
            'Modules/textio.o Modules/stringio.o  Modules/faulthandler.o  '
            'Modules/_tracemalloc.o  Modules/_peg_parser.o  '
            'Modules/symtablemodule.o  Modules/xxsubtype.o',
 'MODULE_OBJS': '\\',
 'MULTIARCH': '',
 'MULTIARCH_CPPFLAGS': '',
 'MVWDELCH_IS_EXPRESSION': 0,
 'NO_AS_NEEDED': '-Wl,--no-as-needed',
 'OBJECT_OBJS': '\\',
 'OPENSSL_INCLUDES': '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include',
 'OPENSSL_LDFLAGS': '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/lib',
 'OPENSSL_LIBS': '-lssl -lcrypto',
 'OPT': '-DNDEBUG -g -fwrapv -O3 -Wall',
 'OTHER_LIBTOOL_OPT': '',
 'PACKAGE_BUGREPORT': 0,
 'PACKAGE_NAME': 0,
 'PACKAGE_STRING': 0,
 'PACKAGE_TARNAME': 0,
 'PACKAGE_URL': 0,
 'PACKAGE_VERSION': 0,
 'PARSER_HEADERS': '\\',
 'PARSER_OBJS': '\\ \\ Parser/myreadline.o Parser/parsetok.o '
                'Parser/tokenizer.o',
 'PEGEN_HEADERS': '\\',
 'PEGEN_OBJS': '\\',
 'PGO_PROF_GEN_FLAG': '-fprofile-instr-generate',
 'PGO_PROF_USE_FLAG': '-fprofile-instr-use=code.profclangd',
 'PLATLIBDIR': 'lib',
 'POBJS': '\\',
 'POSIX_SEMAPHORES_NOT_ENABLED': 0,
 'PROFILE_TASK': '-m test --pgo',
 'PTHREAD_KEY_T_IS_COMPATIBLE_WITH_INT': 1,
 'PTHREAD_SYSTEM_SCHED_SUPPORTED': 0,
 'PURIFY': '',
 'PY3LIBRARY': 'libpython3.so',
 'PYLONG_BITS_IN_DIGIT': 0,
 'PYTHON': 'python',
 'PYTHONFRAMEWORK': '',
 'PYTHONFRAMEWORKDIR': 'no-framework',
 'PYTHONFRAMEWORKINSTALLDIR': '',
 'PYTHONFRAMEWORKPREFIX': '',
 'PYTHONPATH': '',
 'PYTHON_FOR_BUILD': '_PYTHON_PROJECT_BASE=/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/android-build '
                     '_PYTHON_HOST_PLATFORM=$(_PYTHON_HOST_PLATFORM) '
                     'PYTHONPATH=$(shell test -f pybuilddir.txt && echo '
                     '/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/android-build/`cat '
                     'pybuilddir.txt`:)/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/Lib '
                     '_PYTHON_SYSCONFIGDATA_NAME=_sysconfigdata__linux_ '
                     'python3',
 'PYTHON_HEADERS': '\\',
 'PYTHON_OBJS': '\\',
 'PY_BUILTIN_HASHLIB_HASHES': '"md5,sha1,sha256,sha512,sha3,blake2"',
 'PY_BUILTIN_MODULE_CFLAGS': '-mfloat-abi=softfp -mfpu=vfpv3-d16 '
                             '-Wno-unused-result -Wsign-compare '
                             '-Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall '
                             '-fPIC -DANDROID -fPIC -DANDROID -std=c99 -Wextra '
                             '-Wno-unused-result -Wno-unused-parameter '
                             '-Wno-missing-field-initializers '
                             '-Wstrict-prototypes '
                             '-Werror=implicit-function-declaration '
                             '-fvisibility=hidden  '
                             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/Include/internal '
                             '-IObjects -IInclude -IPython -I. '
                             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/Include '
                             '-DANDROID '
                             '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
                             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/python-installs/taskapp/armeabi-v7a/include/python3.9 '
                             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3 '
                             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/include '
                             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include '
                             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/internal '
                             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/openssl '
                             '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
                             '-DANDROID '
                             '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
                             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/python-installs/taskapp/armeabi-v7a/include/python3.9 '
                             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3 '
                             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/include '
                             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include '
                             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/internal '
                             '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/openssl '
                             '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
                             '-DPy_BUILD_CORE_BUILTIN',
 'PY_CFLAGS': '-mfloat-abi=softfp -mfpu=vfpv3-d16 -Wno-unused-result '
              '-Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall '
              '-fPIC -DANDROID -fPIC -DANDROID',
 'PY_CFLAGS_NODIST': '-std=c99 -Wextra -Wno-unused-result '
                     '-Wno-unused-parameter -Wno-missing-field-initializers '
                     '-Wstrict-prototypes '
                     '-Werror=implicit-function-declaration '
                     '-fvisibility=hidden  '
                     '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/Include/internal',
 'PY_COERCE_C_LOCALE': 1,
 'PY_CORE_CFLAGS': '-mfloat-abi=softfp -mfpu=vfpv3-d16 -Wno-unused-result '
                   '-Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 '
                   '-Wall -fPIC -DANDROID -fPIC -DANDROID -std=c99 -Wextra '
                   '-Wno-unused-result -Wno-unused-parameter '
                   '-Wno-missing-field-initializers -Wstrict-prototypes '
                   '-Werror=implicit-function-declaration -fvisibility=hidden  '
                   '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/Include/internal '
                   '-IObjects -IInclude -IPython -I. '
                   '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/Include '
                   '-DANDROID '
                   '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
                   '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/python-installs/taskapp/armeabi-v7a/include/python3.9 '
                   '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3 '
                   '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/include '
                   '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include '
                   '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/internal '
                   '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/openssl '
                   '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
                   '-DANDROID '
                   '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
                   '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/python-installs/taskapp/armeabi-v7a/include/python3.9 '
                   '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3 '
                   '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/include '
                   '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include '
                   '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/internal '
                   '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/openssl '
                   '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
                   '-DPy_BUILD_CORE',
 'PY_CORE_LDFLAGS': '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/libs_collections/taskapp/armeabi-v7a '
                    '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3/obj/local/armeabi-v7a '
                    '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/.libs '
                    '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1 '
                    '-L/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/arm-linux-androideabi/21 '
                    '-march=armv7-a -Wl,--fix-cortex-a8   '
                    '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/libs_collections/taskapp/armeabi-v7a '
                    '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3/obj/local/armeabi-v7a '
                    '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/.libs '
                    '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1 '
                    '-L/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/arm-linux-androideabi/21',
 'PY_CPPFLAGS': '-IObjects -IInclude -IPython -I. '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/Include '
                '-DANDROID '
                '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/python-installs/taskapp/armeabi-v7a/include/python3.9 '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3 '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/include '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/internal '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/openssl '
                '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
                '-DANDROID '
                '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/python-installs/taskapp/armeabi-v7a/include/python3.9 '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3 '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/include '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/internal '
                '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/openssl '
                '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include',
 'PY_FORMAT_SIZE_T': '"z"',
 'PY_LDFLAGS': '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/libs_collections/taskapp/armeabi-v7a '
               '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3/obj/local/armeabi-v7a '
               '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/.libs '
               '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1 '
               '-L/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/arm-linux-androideabi/21 '
               '-march=armv7-a -Wl,--fix-cortex-a8   '
               '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/libs_collections/taskapp/armeabi-v7a '
               '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3/obj/local/armeabi-v7a '
               '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/.libs '
               '-L/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1 '
               '-L/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/arm-linux-androideabi/21',
 'PY_LDFLAGS_NODIST': '',
 'PY_SSL_DEFAULT_CIPHERS': 1,
 'PY_SSL_DEFAULT_CIPHER_STRING': 0,
 'PY_STDMODULE_CFLAGS': '-mfloat-abi=softfp -mfpu=vfpv3-d16 -Wno-unused-result '
                        '-Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv '
                        '-O3 -Wall -fPIC -DANDROID -fPIC -DANDROID -std=c99 '
                        '-Wextra -Wno-unused-result -Wno-unused-parameter '
                        '-Wno-missing-field-initializers -Wstrict-prototypes '
                        '-Werror=implicit-function-declaration '
                        '-fvisibility=hidden  '
                        '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/Include/internal '
                        '-IObjects -IInclude -IPython -I. '
                        '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/Include '
                        '-DANDROID '
                        '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
                        '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/python-installs/taskapp/armeabi-v7a/include/python3.9 '
                        '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3 '
                        '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/include '
                        '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include '
                        '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/internal '
                        '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/openssl '
                        '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
                        '-DANDROID '
                        '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include '
                        '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/python-installs/taskapp/armeabi-v7a/include/python3.9 '
                        '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/sqlite3/armeabi-v7a__ndk_target_21/sqlite3 '
                        '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/libffi/armeabi-v7a__ndk_target_21/libffi/include '
                        '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include '
                        '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/internal '
                        '-I/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/openssl/armeabi-v7a__ndk_target_21/openssl1.1/include/openssl '
                        '-I/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include',
 'Py_DEBUG': 0,
 'Py_ENABLE_SHARED': 1,
 'Py_HASH_ALGORITHM': 0,
 'Py_TRACE_REFS': 0,
 'QUICKTESTOPTS': '-x test_subprocess test_io test_lib2to3 \\',
 'READELF': '/home/brinfo-linux/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-readelf',
 'RESSRCDIR': 'Mac/Resources/framework',
 'RETSIGTYPE': 'void',
 'RUNSHARED': '',
 'SCRIPTDIR': '/usr/local/lib',
 'SETPGRP_HAVE_ARG': 0,
 'SHELL': '/bin/sh',
 'SHLIBS': '-ldl  -lsqlite3 -lffi -lcrypto1.1 -lssl1.1 -lz -lm',
 'SHLIB_SUFFIX': '.so',
 'SHM_NEEDS_LIBRT': 0,
 'SIGNED_RIGHT_SHIFT_ZERO_FILLS': 0,
 'SITEPATH': '',
 'SIZEOF_DOUBLE': 8,
 'SIZEOF_FLOAT': 4,
 'SIZEOF_FPOS_T': 8,
 'SIZEOF_INT': 4,
 'SIZEOF_LONG': 4,
 'SIZEOF_LONG_DOUBLE': 8,
 'SIZEOF_LONG_LONG': 8,
 'SIZEOF_OFF_T': 8,
 'SIZEOF_PID_T': 4,
 'SIZEOF_PTHREAD_KEY_T': 4,
 'SIZEOF_PTHREAD_T': 4,
 'SIZEOF_SHORT': 2,
 'SIZEOF_SIZE_T': 4,
 'SIZEOF_TIME_T': 4,
 'SIZEOF_UINTPTR_T': 4,
 'SIZEOF_VOID_P': 4,
 'SIZEOF_WCHAR_T': 4,
 'SIZEOF__BOOL': 1,
 'SOABI': 'cpython-39',
 'SRCDIRS': 'Parser Parser/pegen Objects Python Modules Modules/_io Programs',
 'SRC_GDB_HOOKS': '/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/Tools/gdb/libpython.py',
 'STDC_HEADERS': 1,
 'STRICT_SYSV_CURSES': "/* Don't use ncurses extensions */",
 'STRIPFLAG': '-s',
 'SUBDIRS': '',
 'SUBDIRSTOO': 'Include Lib Misc',
 'SYSLIBS': '-lm',
 'SYS_SELECT_WITH_SYS_TIME': 1,
 'TCLTK_INCLUDES': '',
 'TCLTK_LIBS': '',
 'TESTOPTS': '',
 'TESTPATH': '',
 'TESTPYTHON': './python',
 'TESTPYTHONOPTS': '',
 'TESTRUNNER': './python '
               '/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/Tools/scripts/run_tests.py',
 'TESTTIMEOUT': 1200,
 'TIMEMODULE_LIB': 0,
 'TIME_WITH_SYS_TIME': 1,
 'TM_IN_SYS_TIME': 0,
 'TZPATH': '/usr/share/zoneinfo:/usr/lib/zoneinfo:/usr/share/lib/zoneinfo:/etc/zoneinfo',
 'UNICODE_DEPS': '\\',
 'UNIVERSALSDK': '',
 'UPDATE_FILE': 'python3 '
                '/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/Tools/scripts/update_file.py',
 'USE_COMPUTED_GOTOS': 0,
 'VERSION': '3.9',
 'VPATH': '/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3',
 'WINDOW_HAS_FLAGS': 0,
 'WITH_DECIMAL_CONTEXTVAR': 1,
 'WITH_DOC_STRINGS': 1,
 'WITH_DTRACE': 0,
 'WITH_DYLD': 0,
 'WITH_LIBINTL': 0,
 'WITH_NEXT_FRAMEWORK': 0,
 'WITH_PYMALLOC': 1,
 'WITH_VALGRIND': 0,
 'X87_DOUBLE_ROUNDING': 0,
 'XMLLIBSUBDIRS': 'xml xml/dom xml/etree xml/parsers xml/sax',
 'abs_builddir': '/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3/android-build',
 'abs_srcdir': '/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3',
 'datarootdir': '/usr/local/share',
 'exec_prefix': '/usr/local',
 'prefix': '/usr/local',
 'srcdir': '/home/brinfo-linux/Documentos/Admin-Auxiliador/frontend/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/armeabi-v7a__ndk_target_21/python3'}
