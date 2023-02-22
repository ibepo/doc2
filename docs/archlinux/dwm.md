### keybind
```shell
### dwm.config.h
```shell
    { MODKEY,              XK_Return,       spawn,            SHCMD("alacritty") },
    { MODKEY,              XK_e,            spawn,            SHCMD("thunar") }, 
    { MODKEY,			         XK_l,         		spawn,        	  {.v=(const char*[]){TERMINAL,"-e","lf",NULL}}},
    { MODKEY,			         XK_r,         		spawn,        	  {.v=(const char*[]){TERMINAL,"-e","htop",NULL}}},
    { MODKEY|ShiftMask,	   XK_r,         		spawn,        	  {.v=(const char*[]){TERMINAL,"-e","btop",NULL}}},
    { ShiftMask,           XK_Escape,       spawn,            SHCMD("flameshot gui -c -p ~/Pictures/screenshots") },
    { MODKEY,              XK_d,            spawn,            SHCMD("rofi -show drun -theme ~/.config/rofi/rofi.rasi") },
    { MODKEY,              XK_p,            spawn,            SHCMD("rofi -show drun -theme ~/.config/rofi/config2.rasi") },
    { MODKEY,              XK_space,        spawn,            SHCMD("rofi -show window -theme ~/.config/rofi/config2.rasi") },
    { MODKEY,              XK_w,            spawn,            SHCMD("microsoft-edge-dev") },
    { ShiftMask|ControlMask, XK_c,          spawn,            SHCMD("xclip -o | xclip -selection c") },
```

```