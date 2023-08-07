# Generic Install Wizard in Python

This is a generic install wizard made in python that can be configured to install anything*!</br>
The goal is to avoid having to make a custom wizard for each application,
since every message, every step of the installation can be configured in a single json.

For now, it only supports file and folder copying,
and has a start, end and error dialog.</br>
It is planned to have an actual window with a progress bar and other stuff
but for now it's really simple (because I needed the core functionality fast).

To ship it with your project, you can use [pyinstaller](https://pyinstaller.org/en/stable/usage.html) (`--onefile` flag advised),
or use one of the builds my future self will probably make.

*anything that only requires files or folders to be copied for now...