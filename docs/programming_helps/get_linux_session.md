Run this command in the terminal to check which display server protocol your Linux desktop session is using:

```bash
echo $XDG_SESSION_TYPE
````

Possible outputs:

* `x11` → your desktop session is running on X11
* `wayland` → your desktop session is running on Wayland

This library currently supports X11 sessions only.

On Wayland-based sessions, some window management and input automation features may not work due to protocol security restrictions.

