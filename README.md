# PageSh

An interactive shell for browsing and querying tldr pages.

## Overview

PageSh is a REPL for browsing and querying [tldr pages](https://tldr.sh/), powered by the [Python command-line client](https://github.com/tldr-pages/tldr-python-client) for **tldr pages**.

## Features

- **Standalone**: Runs without requiring Python or any external dependencies.

- **Portable**: Distributed as a single-file executable.

## Usage

Download the latest release from the Releases page.

## Building from Source

1. **Requirements**<br>
    Install the required dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

2. **Build the executable**<br>
    Using PyInstaller:

    ```bash
    pyinstaller PageSh.spec
    ```

## Running from source

From the `src` directory, run:

```bash
python -m pagesh
```

## Example

```bash
PageSh> ls

  ls

  List directory contents.
  More information: https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html.
  ...
```

Note: The optional `tldr` prefix is accepted for CLI compatibility.

## License

This project is licensed under the MIT license. See the [LICENSE](./LICENSE) file for details.

## Credits

See [CREDITS](./CREDITS.md) for third-party software, assets, and acknowledgements.
