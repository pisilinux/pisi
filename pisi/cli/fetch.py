# -*- coding:utf-8 -*-
#
# Copyright (C) 2009, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#
import gettext
import optparse
import os

import pisi.api
import pisi.cli.command as command
import pisi.context as ctx

__trans = gettext.translation('pisi', fallback=True)
_ = __trans.gettext


class Fetch(command.Command, metaclass=command.autocommand):
    __doc__ = _("""Fetch a package

Usage: fetch [<package1> <package2> ... <packagen>]

<packagei>: package name

Downloads the given pisi packages to working directory
""")

    def __init__(self,args):
        super(Fetch, self).__init__(args)

    name = ("fetch", "fc")

    def options(self):
        group = optparse.OptionGroup(self.parser, _("fetch options"))
        self.add_options(group)
        self.parser.add_option_group(group)

    def add_options(self, group):
        group.add_option("-o", "--output-dir", action="store", default=os.path.curdir,
                               help=_("Output directory for the fetched packages"))
        group.add_option("--runtime-deps", action="store_true", default=None,
                         help=_("Fetch runtime dependencies too"))

    def run(self):
        packages = pisi.db.packagedb.PackageDB()
        self.init(database=False, write=False)

        if not self.args:
            self.help()
            return

        runtime_dependencies = []

        if ctx.config.options.runtime_deps:
            for arg in self.args:
                package = packages.get_package(arg)
                runtime_dependencies = [dep.name() for dep in package.runtimeDependencies()]

        pisi.api.fetch(self.args + runtime_dependencies, ctx.config.options.output_dir)
