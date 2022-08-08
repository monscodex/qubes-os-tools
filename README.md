# qubes-os-tools
Scripts that have helped me have greater convenience in qubes-os.
These scripts are intended to be use as shortcuts.

## open_application_in_active_window.py
Open an application ***in*** the currently focused VM.

#### Example:
``` bash
./open_application_in_active_window.py alacritty xfce4-terminal
```
The ___first argument___ is the command that will run in the currently focused VM if the  ___current focused belongs to a VM___.
The ___second argument___ is the command that will be run in dom0 if the ___current focused window belongs to dom0___.

#### Other example:
``` bash
./open_application_in_active_window.py 'alacritty & gnome-terminal' xfce4-terminal
```

I only use alacritty on Fedora-based VMs and I only use gnome-terminal on Debian-based VMs.

With this command I can fire up a terminal in any of the two systems because if alacritty is installed gnome-terminal won't be and if gnome-terminal is installed alacritty won't be.

#### ***Be creative with your commands!***

## open_application_in_template_of_active_window.py
Open an application ***in*** the template of the currently focused VM.

#### Example:
``` bash
./open_application_in_template_of_active_window.py alacritty
```
The ___first and only argument___ is the command that will run in the template of the currently focused VM.

NOTE: if the currently focused window belongs to dom0 nothing will be executed.

## execute_command_to_active_vm.py
Execute a command in dom0 ***to*** the currently focused VMs.

#### Example:
``` bash
./execute_command_to_active_vm.py "qvm-shutdown <--Name-->"
```

The ___first and only argument___ is a command that ___will be executed in dom0___. "<--Name-->" is a placeholder for the name of the currently focused VMs.

## Inspiration:

[nil0x42's qubes-screenshooter](https://github.com/nil0x42/qubes-screenshooterhttps://github.com/nil0x42/qubes-screenshooter)
