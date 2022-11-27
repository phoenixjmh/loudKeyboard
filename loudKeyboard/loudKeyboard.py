from pynput.keyboard import Key, Listener
import winsound
#CHANGE THE WAV MANUALLY, THERES CLAPS AND AIRHORN



spacePressed = False


    
    
def on_press(key):
    global spacePressed
    if key==Key.space:
        spacePressed = not spacePressed
    if  spacePressed:
        winsound.PlaySound("sounds/airhorn.wav", winsound.SND_ASYNC)
    else:
        winsound.PlaySound("sounds/clap.wav", winsound.SND_ASYNC)

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
