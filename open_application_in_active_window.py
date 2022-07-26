#!/usr/bin/python3

from qubes_utils import get_name_of_front_vm
from sys import argv
import os


def main() -> None:
    vm_name = get_name_of_front_vm()

    command = get_command_to_execute(vm_name)
    
    os.system(command)


def get_command_to_execute(vm_name: str) -> str:
    if vm_name == "dom0":
        return argv[2]

    command_to_execute = argv[1]

    return f"qvm-run {vm_name} {command_to_execute}"


if __name__ == "__main__":
    main()
