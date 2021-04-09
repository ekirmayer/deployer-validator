import os


def get_disks_info():
    try:
        print()
        os.system('lsblk -io KNAME,TYPE,SIZE,MODEL,FSTYPE,UUID,MOUNTPOINT')
    except Exception as error:
        print(f'Failed to get the disk information due to {error.__doc__}')

