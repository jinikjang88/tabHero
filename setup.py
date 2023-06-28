import sys
from cx_Freeze import setup, Executable

# 프로그램의 메인 스크립트 파일 이름
main_script = 'main.py'

# 윈도우 애플리케이션으로 패키지할 때 필요한 추가 모듈들
# 필요한 모듈들을 추가하거나 제거해야 할 수 있습니다.
build_exe_options = {
    'packages': ['tkinter'],
    'excludes': [],
    'includes': [],
    'include_files': []
}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

# 윈도우 애플리케이션으로 패키지할 설정
exe = Executable(
    script=main_script,
    base=base,
)

setup(
    name='MyApp',
    version='1.0',
    description='My Application',
    options={'build_exe': build_exe_options},
    executables=[exe]
)
