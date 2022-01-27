import subprocess
import re

command_output = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], 
                                capture_output=True).stdout.decode(
                                    'utf-8', errors="backslashreplace")

# finding all available wifi networks
profiles = re.findall("All User Profile     : (.*)\r", command_output)

password_list = [] #stores password info of all devices
if profiles:
    for name in profiles:
        try:
            wifi_profile = {}
            # getting the meta data of the particular wifi provider
            wifi_info = subprocess.run(['netsh', 'wlan', 'show', 'profiles', name, 
                              'key=clear'], capture_output=True).stdout.decode(
                                            'utf-8', errors="backslashreplace")
            # seaches the security key status                                
            if re.search("Security key           : Absent", wifi_info):
                wifi_profile[name] = None
            else:
                profile_password = subprocess.run(['netsh', 'wlan', 'show', 'profiles', 
                                    name, 'key=clear'], capture_output=True).stdout.decode(
                                            'utf-8', errors="backslashreplace")
                # extracting the password
                password = re.search("Key Content            : (.*)\r", profile_password)
                if password == None:
                    wifi_profile[name] = None
                else:
                    wifi_profile[name] = password[1]
                password_list.append(wifi_profile)
        except:
            pass

for device in password_list:
    print(device)