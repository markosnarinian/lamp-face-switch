from keyboard import add_hotkey
from keyboard import wait
from win10toast import ToastNotifier


def toggle_auto_mode():
    auto_file = open('C:/Users/manar/3D Objects/face_lamp/auto.txt', 'rt')
    auto_mode = auto_file.read()
    auto_file.close()

    auto_file = open('C:/Users/manar/3D Objects/face_lamp/auto.txt', 'wt')
    if auto_mode == 'ON':
        auto_file.write('OFF')
        ToastNotifier().show_toast('Auto detect face', 'OFF', duration=2, threaded=True)
    if auto_mode == 'OFF':
        auto_file.write('ON')
        ToastNotifier().show_toast('Auto detect face', 'ON', duration=2, threaded=True)
    auto_file.close()


add_hotkey('ctrl+alt+x', toggle_auto_mode)

wait()
