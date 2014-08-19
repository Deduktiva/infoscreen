## infoscreen

### base setup procedure on embedded boards

 - mkfs (ext3, ext4) on SD card
 - `dd(1)` uBoot + kernel to SD card
 - mount SD card, `cd(1)` into mountpoint
 - `debootstrap --foreign --arch armhf --verbose wheezy . http://ftp.at.debian.org/debian/`
 - edit inittab:
```
T0:23:respawn:/sbin/getty -L ttymxc0 115200 vt100
T1:23:respawn:/sbin/getty -L ttymxc1 115200 vt100
T2:23:respawn:/sbin/getty -L ttymxc2 115200 vt100
T3:23:respawn:/sbin/getty -L ttymxc3 115200 vt100
```
 - boot, login, configure ethernet (DHCP)
 - `cd /debootstrap ; debootstrap --second-stage`
 - reboot
 - `apt-get install xserver-xorg xserver-xorg-video-fbdev iceweasel
   x11-apps -y`

#### engicam specific: XXX(azet)
```
sudo fdisk /dev/sdb


Command (m for help): n
Partition type:
   p   primary (0 primary, 0 extended, 4 free)
   e   extended
Select (default p):
Using default response p
Partition number (1-4, default 1):
Using default value 1
First sector (2048-15353855, default 2048): +100M
Last sector, +sectors or +size{K,M,G} (204800-15353855, default
15353855): +2G

Command (m for help): p

Disk /dev/sdb: 7861 MB, 7861174272 bytes
4 heads, 4 sectors/track, 959616 cylinders, total 15353856 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x0ca97dd8

   Device Boot      Start         End      Blocks   Id  System
/dev/sdb1          204800     4399103     2097152   83  Linux

 sudo dd if=/srv/default_image/uImage of=/dev/sdb bs=1M seek=1
 2553  sudo mkfs.ext4 /dev/sdb1

 2554  sudo mount /dev/sdb1 /mnt -t ext4
 2555  cd /mnt
 2556  sudo tar xf /srv/default_image/rootfs.tgz
 2558  sudo chown -R root: /mnt
``` 
