from pynput.mouse import Button, Controller, Listener
from pynput import keyboard
import pickle
import os


#-------Secure-Data-------------------------->
def write_data(data):
    with open("data.pkl", "wb") as file:
        pickle.dump(data, file)
def read_data():
    with open("data.pkl", "rb") as file:
       data = pickle.load(file)
       return data




#-----Main-Functions-------------------->
def set_postitions(data, data_keys, choice, pointer):
    def on_click(x, y, button, pressed):
        if pressed and button == Button.left:
            print("{} at ({},{})".format(button,x,y))
            return False

    for key in data[choice] : #----> get-the-data-user-chose.
        print(f"position the mouse then Click to assing {choice} :{key.upper()}")
        with Listener(on_click=on_click) as listener:
            listener.join()
            data[choice][key] = pointer.position
    write_data(data)
#-------------------------------------------------------------------------------------          
def click_on_positions(positions,keys, choice, pointer):
    position_key = positions[choice]
    def on_press(key):
        shortCuts = {
            'a' : "1",
            'b' : "2",
            'c' : "3",
            'd' : "4",
            'next' : keyboard.Key.ctrl_l,
            'exit_key' : keyboard.Key.esc,
        }

        if getattr(key, "char", None) == shortCuts['a']:
            pointer.position = position_key["a"]
            pointer.press(Button.left)
            pointer.release(Button.left)
            print("a")
        if getattr(key, "char", None) == shortCuts['b']:
            pointer.position = position_key["b"]
            pointer.press(Button.left)
            pointer.release(Button.left)
            print("b")
        if getattr(key, "char", None) == shortCuts['c']:
            pointer.position = position_key["c"]
            pointer.press(Button.left)
            pointer.release(Button.left)
            print("c")
        if getattr(key, "char", None) == shortCuts['d']:
            pointer.position = position_key["d"]
            pointer.press(Button.left)
            pointer.release(Button.left)
            print("d")
        if getattr(key, "char", key) == shortCuts['next']:
            pointer.position = position_key["next"]
            pointer.press(Button.left)
            pointer.release(Button.left)
            print("next")
        if getattr(key, "char", key) == shortCuts['exit_key']:
            return False
    with keyboard.Listener(on_press = on_press) as key_listener:
        key_listener.join()
         
        
def Main():
    #-----Main--------------------------------------------->
    print(f"{'-'*60}")
    print(f"{'-'*20}Made-By-Osama-Abdelsattar{'-'*15}")
    print(f"{'-'*60}")
    pointer = Controller()
    choice_1 = input('press "1" for salah "2" for ahmed adel "3" for ghonem "4" for "english" : ')
    choice_2 = input('press "1" to change the positions "Enter" to continue : ')
    #-----Data------------------------------------->
    data = read_data()
    data_keys = list(data)
    choice = data_keys[int(choice_1)-1]
    
    #----Check-for-edits------------------------------->
    if choice_2 == "1":
        set_postitions(data, data_keys, choice, pointer)
        read_data() #===> Approve Editw
        
    #-----Start-The-App------------------------>
    print("App Started Press Esc to Exit")
    click_on_positions(data, data_keys, choice, pointer)
    os.system(f"taskkill /PID {os.getppid()} /F") if input('Enter To Close the app "1" to Continue restart : ') == "" else Main() 
    
if __name__ == "__main__":
    Main()
