#!/usr/bin/python3

import subprocess
import re

def get_name_of_front_vm():
    window_id = get_front_window_id()

    vm_name = get_vm_name_with_window_id(window_id)

    return vm_name


def get_name_of_templatevm_of_vm(vm_name):
    # Using %s placeholder because had to escape awk's {} using an f-string. Cleaner this way.
    command = "qvm-ls %s | awk 'FNR == 2 {print $5}'" % vm_name

    templatevm_name = get_output_of_system_command(command)

    return templatevm_name.strip()


def get_front_window_id():
    window_id_output = get_output_of_system_command("xprop -notype -root _NET_ACTIVE_WINDOW")

    window_id = re.search("^_NET_ACTIVE_WINDOW: window id # (0x[0-9a-f]+), 0x0$", window_id_output)

    if not window_id:
        return

    return window_id.group(1)

def get_vm_name_with_window_id(window_id):
    vm_name_output = get_output_of_system_command(f'xprop -id "{window_id}" -notype _QUBES_VMNAME')

    vm_name = re.search('^_QUBES_VMNAME = \"(.*)\"$', vm_name_output)

    if vm_name:
        return vm_name.group(1)

    # If there isn't a match for the vm_name, it's because it's a dom0 window
    return 'dom0'


def get_output_of_system_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    output = result.stdout

    return output.decode("utf-8")
