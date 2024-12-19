import subprocess

def GetWifiStatus():
    # Gets the WiFi status using 'iwconfig' command

    try:
        output = subprocess.check_output(['iwconfig', 'wlan0'], stderr=subprocess.STDOUT)
        output = output.decode('utf-8')

        if "ESSID" in output:
            ssid_line = [line for line in output.split('\n') if "ESSID" in line][0]
            ssid = ssid_line.split(":")[1].strip().replace('"', '')
            return ssid
        else:
            return "Not connected"

    except subprocess.CalledProcessError:
        return "Error"

wifiStatus = GetWifiStatus()
print(f"WiFi: {wifiStatus}")
