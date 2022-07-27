# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from logging import disable
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
import libqtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess
import os
# from plasma import Plasma

mod = "mod4"
alt = "mod2"
shift = "shift"
ctrl = "control"
plasma_grow = 30
home = os.path.expanduser('~')
terminal = guess_terminal()

# Hooks
@hook.subscribe.startup_once
def autostart():
    autost = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([autost])

class MyStyle:
    primaryFont = 'Roboto Medium'
    iconsFont = 'mononoki Nerd Font Mono'
    clockFont = 'Titillium Web'
    palette = ['F5C63C', 'F47F6B', 'BB5098', '7A5197', '5344A9','0D0C1D', '474973']
    barBG = '000000'


myStyle = MyStyle()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Same but with arrow keys
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),

    #Key([mod], "space", lazy.layout.next(),
     #   desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, shift], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, shift], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, shift], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, shift], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, ctrl], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, ctrl], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, ctrl], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, ctrl], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, shift], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, shift], "Return", lazy.spawn("xfce4-terminal"), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, ctrl], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, ctrl], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Plasma layout
    # TODO add descriptions
    # move
    # Key([mod, shift], 'Left', lazy.layout.move_left()),
    # Key([mod, shift], 'Down', lazy.layout.move_down()),
    # Key([mod, shift], 'Up', lazy.layout.move_up()),
    # Key([mod, shift], 'Right', lazy.layout.move_right()),

    # # intergrate
    # Key([mod, ctrl], 'Left', lazy.layout.integrate_left()),
    # Key([mod, ctrl], 'Down', lazy.layout.integrate_down()),
    # Key([mod, ctrl], 'Up', lazy.layout.integrate_up()),
    # Key([mod, ctrl], 'Right', lazy.layout.integrate_right()),
    # # scale
    # Key([mod, ctrl, shift], 'Left', lazy.layout.grow_width(plasma_grow)),
    # Key([mod, ctrl, shift], 'Down', lazy.layout.grow_height(plasma_grow)),
    # Key([mod, ctrl, shift], 'Up', lazy.layout.grow_height(-plasma_grow)),
    # Key([mod, ctrl, shift], 'Right', lazy.layout.grow_width(-plasma_grow)),

    # KeyChord([mod, shift], 'n', [
    #     # moving
    #     Key([], 'h', lazy.layout.move_left()),
    #     Key([], 'j', lazy.layout.move_down()),
    #     Key([], 'k', lazy.layout.move_up()),
    #     Key([], 'l', lazy.layout.move_right()),
    # ]),

    # Custom
    Key([mod], "p", lazy.spawn("dmenu_run -c -l 10"), desc="Run dmenu"), 
    Key([mod], "n", lazy.spawn("= --"), desc="menu-calc"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"),
    Key([mod], "o", lazy.hide_show_bar("top"), desc="toggle top bar"),
    Key([mod], "t", lazy.spawn("thunar"), desc="open file manager (thunar)"),
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Screenshot"),
    Key([mod, shift], "s", lazy.spawn("flameshot gui"), desc="Screenshot (windows hotkey)"),
    Key([mod, ctrl, shift], 's', lazy.spawn("shutdown 0"), desc="Shutdown"),
    Key([mod, ctrl, shift], 'a', lazy.spawn("systemctl suspend"), desc="Suspend to RAM"),
    Key([mod, ctrl, shift], 'r', lazy.spawn("reboot"), desc="Reboot"),
#   Key([alt], 'Shift_L', lazy.widget["keyboardlayout"].next_keyboard(), desc="Change Layout"),
    KeyChord([mod], 'm', [
        Key([], 'n', lazy.spawn(home + "/Scripts/dm-confedit.sh"))
    ]),
]

groupNames =  ['1', '2', '3', '4', '5', '6', '7', '8', '9']
groupIcons = ['', '', '', '', '', '', '', '', '']

groups = list()

for i in range(len(groupNames)):
    groups.append(
        Group(
            name=groupNames[i],
            label=groupIcons[i],
        )
    )
ind = 0

for i in range(len(groups)):
    currentGroup = groups[i]
    if (i == 3 or i == 4 or i == 5):
        # shortcuts
        alternativeKey = str(i - 2)
        keys.extend([
            Key([mod, ctrl], alternativeKey, lazy.group[currentGroup.name].toscreen(),
                desc="Alternative Switch to group {}".format(currentGroup.name)),
            Key([mod, ctrl, shift], alternativeKey, lazy.window.togroup(currentGroup.name, switch_group=True),
                desc="Alternative move focused window to group {}".format(currentGroup.name)),
        ])

    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], currentGroup.name, lazy.group[currentGroup.name].toscreen(),
            desc="Switch to group {}".format(currentGroup.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, shift], currentGroup.name, lazy.window.togroup(currentGroup.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(currentGroup.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, shift], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


# LAYOUTS
layouts = [

    layout.Columns(
        margin=4,
        border_width=3,
        border_focus=myStyle.palette[0],
        border_normal=myStyle.palette[4],
        fair=False,
        num_columns=2,
        margin_on_single=0,
    ),

    layout.MonadTall(
        border_width=3,
        margin=7,
        border_focus='#ffc048',
        border_normal='#d2dae2',
        single_border_width=0,
        single_margin=0,
        ratio=.55,
    ),
    
    # Plasma(
    #     border_normal=myStyle.palette[3],
    #     border_focus=myStyle.palette[0],
    #     border_normal_fixed='#006863',
    #     border_focus_fixed='#00e8dc',
    #     border_width=2,
    #     border_width_single=0,
    #     margin=3
    # ),
        
    layout.Max(),
]

widget_defaults = dict(
    font='mononoki-Regular',
    fontsize=12,
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    scale=.7,
                    background=myStyle.palette[3],
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata\-dz for Powerline",
                    fontsize="33",
                    padding=0,
                    background=myStyle.palette[3],
                    foreground=myStyle.palette[4],
                ),
                widget.GroupBox(
                    disable_drag=True,
                    font=myStyle.iconsFont,
                    fontsize=22,
                    borderwidth=2,
                    inactive='ffffff',
                    active='ffffff',
                    margin=3,
                    highlight_method='line',
                    highlight_color=[myStyle.palette[4], myStyle.palette[4]],
                    this_current_screen_border=myStyle.palette[0],
                    background=myStyle.palette[4],
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata\-dz for Powerline",
                    fontsize="33",
                    padding=0,
                    background=myStyle.palette[4],
                    foreground=myStyle.palette[5],

                ),
                widget.Spacer(
                    20,
                    background=myStyle.palette[5],
                ),
                widget.WindowName(
                    background=myStyle.palette[5],
                    font=myStyle.primaryFont,
                    max_chars=33,
                    format='{state} {name}',
                ),
                widget.Spacer(
                    200,
                    background=myStyle.palette[5],
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata\-dz for Powerline",
                    fontsize="33",
                    padding=0,
                    background=myStyle.palette[5],
                    foreground=myStyle.palette[0],
                ),
                widget.Systray(
                    padding=12,
                    background=myStyle.palette[0],
                ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata\-dz for Powerline",
                    fontsize="33",
                    padding=0,
                    background=myStyle.palette[0],
                    foreground=myStyle.palette[1],
                ),
                widget.Clock(
                    format='%b %d, %a',
                    font=myStyle.clockFont,
                    background=myStyle.palette[1],
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata\-dz for Powerline",
                    fontsize="33",
                    padding=0,
                    background=myStyle.palette[1],
                    foreground=myStyle.palette[2],
                ),
                widget.Clock(
                    fontsize=14,
                    format='%H:%M',
                    font=myStyle.clockFont,
                    background=myStyle.palette[2],
                ),
                widget.Sep(
                    background=myStyle.palette[2],
                    foreground=myStyle.palette[2],
                    linewidth=3,
                ),
            ],
            28,
            background=myStyle.barBG,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
    ],
    border_width=0,
    fullscreen_border_width=0,
    max_border_width=0,
    border_focus='FFFFFF',
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# @libqtile.hook.subscribe.startup_once
# def runner():
# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
