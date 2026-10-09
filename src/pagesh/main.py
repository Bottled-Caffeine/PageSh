import os
import shlex
import subprocess
import sys

from termcolor import colored
from tldr import cli

from pagesh.domain import Command
from pagesh.version import __version__


def _clear_shell() -> None:
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def _exit_shell() -> None:
    raise SystemExit


def _run_command(args: list[str]) -> None:
    command = SHELL_COMMANDS.get(args[0])

    if command is None:
        print(f"Unknown shell command: {args[0]}\n")

        return

    command.handler()


def _run_tldr(args: list[str]) -> None:
    argv = sys.argv
    sys.argv = ["tldr", *args]

    try:
        cli()

    except SystemExit as e:
        if not isinstance(e.code, int):
            print(e, "\n")

    finally:
        sys.argv = argv

    if args[0].startswith("-"):
        print()


def _show_help() -> None:
    print(
        f"{colored('usage:', 'blue', attrs=['bold'])} "
        f"{colored('command [option]', 'magenta')}\n\n"
        f"PageSh: A tldr shell\n\n"
        f"{colored('positional arguments:', 'blue', attrs=['bold'])}\n"
        f"{colored('  {:<22}'.format('command'), 'green', attrs=['bold'])}command to look up\n\n"
        f"{colored('options:', 'blue', attrs=['bold'])}"
    )
    for command, value in SHELL_COMMANDS.items():
        description = value.description
        print(
            f"{colored('  {:<22}'.format(command), 'green', attrs=['bold'])}{description}"
        )
    print()


def _show_version() -> None:
    print(f"PageSh {__version__}")

    args = ["-v"]
    _run_tldr(args)


# Shell commands
SHELL_COMMANDS = {
    ":clear": Command(
        handler=_clear_shell,
        description="clear console",
    ),
    ":exit": Command(
        handler=_exit_shell,
        description="exit PageSh",
    ),
    ":help": Command(
        handler=_show_help,
        description="show this help message",
    ),
    ":version": Command(
        handler=_show_version,
        description="show PageSh and tldr version number",
    ),
}


def main() -> None:
    print(f"PageSh {__version__} — tldr-pages")
    print("Type ':help' for commands, '-help' for tldr commands.\n")

    while True:
        try:
            line = input("PageSh> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not line:
            continue

        args = shlex.split(line)

        if args[0].startswith(":"):
            try:
                _run_command(args)
            except SystemExit:
                break

            continue

        if args[0] == "tldr":
            del args[0]

        _run_tldr(args)


if __name__ == "__main__":
    main()
