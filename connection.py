import subprocess
import keyboard

def toggle_network_connection(interface_name="Ethernet"):
    try:
        # Check current status of the network interface
        status_result = subprocess.check_output(f'netsh interface show interface "{interface_name}"', shell=True).decode()
        if 'Enabled' in status_result:
            # If the interface is enabled, disable it
            subprocess.run(f'netsh interface set interface "{interface_name}" admin=disable', shell=True, check=True)
            print(f"{interface_name} disabled.")
        else:
            # If the interface is disabled, enable it
            subprocess.run(f'netsh interface set interface "{interface_name}" admin=enable', shell=True, check=True)
            print(f"{interface_name} enabled.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to toggle the network connection: {e}")
        print(f"Command output: {e.output.decode()}")

def check_shift_x():
    # Check if both 'shift' and 'x' are being pressed
    if keyboard.is_pressed('shift') and keyboard.is_pressed('x'):
        toggle_network_connection()

# Use a loop to continuously check for 'SHIFT + X'
while True:
    keyboard.add_hotkey('shift+x', check_shift_x)
    keyboard.wait('esc')  # Use 'esc' to stop the script
