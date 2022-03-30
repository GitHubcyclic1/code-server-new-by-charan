import time
import os
data=os.getenv("RCLONE_DATA")
app_name=os.getenv("APP_NAME")
#Config File
os.system(f'mkdir -p /.config/rclone/')
os.system(f'touch /.config/rclone/rclone.conf')
os.system(f'echo {data} | base64 -d > /.config/rclone/rclone.conf')
print('config File Created')
#Download
os.system(f'rclone sync test:{app_name} /app/WORKSPACE')
print('files Synced')
#upload Every 1 min
while True:
    os.system(f'rclone sync  /app/WORKSPACE test:{app_name}')
    print('Files Uploaded')
    time.sleep(60)
