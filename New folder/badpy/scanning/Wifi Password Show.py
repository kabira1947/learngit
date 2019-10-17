import subprocess

a=subprocess.check_output(['netst','wlan','show','profiles']).decode('utf-8').split('\n')
a= [i.split(':')[i][i:-1] for i in a 'if all user profile' in i:]