### theme 
/usr/share/sddm/themes
## Configuration

The default configuration file for SDDM can be found at `/usr/lib/sddm/sddm.conf.d/default.conf`. For any changes, create configuration file(s) in `/etc/sddm.conf.d/`. See [sddm.conf(5)](https://man.archlinux.org/man/sddm.conf.5) for all options.

The [sddm-kcm](https://archlinux.org/packages/?name=sddm-kcm) package (included in the [plasma](https://archlinux.org/groups/x86_64/plasma/) group) provides a GUI to configure SDDM in Plasma's system settings. There is also a [Qt](https://wiki.archlinux.org/title/Qt "Qt")-based [sddm-config-editor-git](https://aur.archlinux.org/packages/sddm-config-editor-git/)AUR available in the [AUR](https://wiki.archlinux.org/title/AUR "AUR").

Everything should work out of the box, since Arch Linux uses [systemd](https://wiki.archlinux.org/title/Systemd "Systemd") and SDDM defaults to using `systemd-logind` for session management.

### order
Configuration loads all files in the configuration directories followed by the configuration file in the order listed below with the latter having highest precedence. **Changes should be made to the local configurations.**

/usr/lib/sddm/sddm.conf.d
               System configuration directory
/etc/sddm.conf.d
                Local configuration directory
/etc/sddm.conf
                Local configuration file for compatibility

https://man.archlinux.org/man/sddm.conf.5