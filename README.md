# SchemeCycler

This package for Sublime Text 2 lets you cycle through all available colour schemes with ease.
If you're using Dayle Rees' Colour Schemes (or any other large collection for that matter), you'd
be forgiven for being slightly overwhelmed by the sheer number of themes available. That's why
this package has the ability to delete the current scheme as you're cycling through them.

_Too bright? Too dark? Too pink?_ Delete it, at the touch of a button!
Eventually you'll be left with a small(er) set of schemes, all of which you like. Win!


## Installation

To install manually, open Sublime's Packages directory in a shell and clone this
repository and rename it to `SchemeCycler`. You can find the packages directory from
ST by going to `Preferences > Browse Packages`.

If you're on OSX, you can paste this into your Terminal:

```bash
cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
git clone https://github.com/dshoreman/sublime-scheme-cycler.git SchemeCycler

```


## Usage

Start typing `SchemeCycler` in the Command Palette and you'll see four commands.
You can cycle schemes forward and backward, or if you don't like the current scheme
you can delete it and change to the next/previous one.


## Keyboard Shortcuts

All shortcuts make use of <kbd>Page Up</kbd> and <kbd>Page Down</kbd>.
For OS-specific shortcuts, see below:

### Mac OS X

| Shortcut                                      | Command                                              |
| --------------------------------------------- |-------------------------------------------------------|
| <kbd>⌘</kbd>+<kbd>PageUp</kbd>                | Change to previous scheme                            |
| <kbd>⌘</kbd>+<kbd>PageDn</kbd>                | Change to next scheme                                |
| <kbd>⌘</kbd>+<kbd>⌥</kbd>+<kbd>PageUp</kbd>  | Delete current scheme and change to the previous one |
| <kbd>⌘</kbd>+<kbd>⌥</kbd>+<kbd>PageDn</kbd>  | Delete current scheme and change to the next one     |

### Windows / Linux

| Shortcut                                          | Command                                              |
| ------------------------------------------------- |------------------------------------------------------|
| <kbd>ctrl</kbd>+<kbd>PageUp</kbd>                 | Change to previous scheme                            |
| <kbd>ctrl</kbd>+<kbd>PageDn</kbd>                 | Change to next scheme                                |
| <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>PageUp</kbd>  | Delete current scheme and change to the previous one |
| <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>PageDn</kbd>  | Delete current scheme and change to the next one     |

### Custom Keymaps

If you'd rather use some other key bindings, you can copy the default keymaps from this
extension. Go to `Preferences > Package Settings > SchemeCycler` and you'll find two
options. *Do not edit the default file* as it will get overwritten if the package gets
updated! You *must* copy the bindings to the `Key Bindings - User` file.


## Credits

This package was forked from [Rémi Rérolle](https://github.com/rrerolle/sublime-scheme-cycler), so I
take no credit for the original work. I simply added some extra features and tweaked the code a bit.

Thanks also to [Marc-Andre Stoppert](https://github.com/mstoppert) and [Andreas Lutro](https://github.com/anlutro)
for inspiring me to finally get around to learning some Python to get this done.
