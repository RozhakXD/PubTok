from Run import Jalankan_Cython
import platform

try:
    if '64bit' in str(platform.architecture()):
        Jalankan_Cython()
    else:
        print("Kode ini hanya untuk CPU 64 bit!")
        exit()
except (Exception, KeyboardInterrupt) as e:
    exit(f"[Error] {str(e).capitalize()}!")
