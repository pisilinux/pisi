# PISI - Packages Installed Succesfully as Intended
PISI is a package manager. In Turkish PISI means "kitty", and like a kitty, it is featureful and small.

Some of its distinctive features:

* Implemented in Python.
* Efficient and small.
* Package sources are written in XML and Python.
* Uses LZMA for a better compression ratio.
* Fast database access implemented with Berkeley DB.
* Integrates low-level and high-level package operations (dependency resolution).
* Framework approach to build applications and tools upon.
* Comprehensive CLI and a user-friendly QT GUI (distributed separately).
* Extremely simple package construction.


## Build Dependencies
Python 3.6+, Gettext, Intltool, COMAR


## Runtime Dependencies
Python 3.6+, File, Gettext, COMAR, Piksemel, Mudur


## Installation
```bash
sudo -H python setup.py install
```


## Usage
```shell
usage: pisi [options] <command> [arguments]

where <command> is one of:

           add-repo (ar) - Add a repository
              blame (bl) - Information about the package owner and release
              build (bi) - Build PiSi packages
                   check - Verify installation
                   clean - Clean stale locks
  configure-pending (cp) - Configure pending packages
       delete-cache (dc) - Delete cache files
              delta (dt) - Creates delta packages
       disable-repo (dr) - Disable repository
             emerge (em) - Build and install PiSi source packages from repository
         emergeup (emup) - Build and install PiSi source packages from repository
        enable-repo (er) - Enable repository
              fetch (fc) - Fetch a package
                   graph - Graph package relations
                help (?) - Prints help for given commands
            history (hs) - History of pisi operations
              index (ix) - Index PiSi files in a given directory
                    info - Display package information
            install (it) - Install PiSi packages
     list-available (la) - List available packages in the repositories
    list-components (lc) - List available components
     list-installed (li) - Print the list of all installed packages
        list-newest (ln) - List newest packages in the repositories
      list-orphaned (lo) - List orphaned packages
       list-pending (lp) - List pending packages
          list-repo (lr) - List repositories
       list-sources (ls) - List available sources
      list-upgrades (lu) - List packages to be upgraded
        rebuild-db (rdb) - Rebuild Databases
             remove (rm) - Remove PiSi packages
    remove-orphaned (ro) - Remove orphaned packages
        remove-repo (rr) - Remove repositories
             search (sr) - Search packages
        search-file (sf) - Search for a file
        update-repo (ur) - Update repository databases
            upgrade (up) - Upgrade PiSi packages

Use "pisi help <command>" for help on a specific command.


Options:
 --version                    : show program's version number and exit
 -h [--help]                  : show this help message and exit

 general options:
  -D [--destdir] arg          : Change the system root for PiSi commands
  -y [--yes-all]              : Assume yes in all yes/no queries
  -u [--username] arg         
  -p [--password] arg         
  -L [--bandwidth-limit] arg  : Keep bandwidth usage under specified KB's
  -v [--verbose]              : Detailed output
  -d [--debug]                : Show debugging information
  -N [--no-color]             : Suppresses all coloring of PiSi's output
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[GPLv2](https://choosealicense.com/licenses/gpl-2.0/)
