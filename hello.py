import subprocess
import win32gui
import win32con

def run_hidden():
    python_script = r"C:\ProgramData\Quantex\QLoader.py"
    command = ["pythonw.exe", python_script]

    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = win32con.SW_HIDE

    subprocess.Popen(command, startupinfo=startupinfo)

if __name__ == "__main__":
    run_hidden()
