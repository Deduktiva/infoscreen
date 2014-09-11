## Setup

### base setup procedure on embedded boards

 - mkfs (ext3, ext4) on SD card, first sector: +100M
 - `dd(1)` uBoot + kernel (device specifig) to SD card
 - mount SD card, `cd(1)` into mountpoint
 - `debootstrap --foreign --arch armhf --verbose wheezy . http://ftp.at.debian.org/debian/`
 - edit `/etc/inittab`:
```
T0:23:respawn:/sbin/getty -L ttymxc0 115200 vt100
T1:23:respawn:/sbin/getty -L ttymxc1 115200 vt100
T2:23:respawn:/sbin/getty -L ttymxc2 115200 vt100
T3:23:respawn:/sbin/getty -L ttymxc3 115200 vt100
```
 - boot, login
 - `cd /debootstrap ; debootstrap --second-stage`
 - reboot, configure ethernet (DHCP)
 - edit `/etc/apt/sources.list`:
```
deb http://debian.inode.at/debian/ wheezy main
deb http://security.debian.org/ wheezy/updates main
```
 - `apt-get update ; apt-get install usbutils matchbox-window-manager openssh-server xserver-xorg xserver-xorg-video-fbdev x11-xserver-util python3 python3-pip iceweasel -y`
 - `pip-3.2 install selenium`

### infoscreen software installation
 - add a new user `infoscreen` with password disabled
 - `mkdir -p /opt/infoscreen ; chown infoscreen:infoscreen
   /opt/infoscreen`
 - checkout the git repo in `/opt/infoscreen` or copy over an archive
 - configure `sbin/run.py` if need be

### device settings / bootup

 - `dpkg-reconfigure x11-common` -> anybody
 - add rc.local:
   ```
   /opt/infoscreen/sbin/boot &
   ```

#### engicam specific:
```
sudo dd if=/srv/default_image/uImage of=/dev/sdb bs=1M seek=1
sudo tar xf /srv/default_image/rootfs.tgz
```

bootloader config:
```
set bootargs set bootargs noinitrd console=ttymxc3,115200 arm_freq=800 engi_board=\${board} video=\${video_type},\${lcd_panel} fbmem=14M video=mxcfb1:off video=mxcfb2:off vt.global_cursor_default=0 fec_mac=\${fecaddr}
```


### TODO:

 - firefox settings in /etc/iceweasel/prefs
 - ???
