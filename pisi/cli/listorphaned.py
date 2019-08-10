# -*- coding:utf-8 -*-
#
# Copyright (C) 2014, marcin.bojara (at) gmail.com
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

import pisi.cli.command as command
import pisi.context as ctx
import pisi.db
import pisi.util as util

__trans = gettext.translation('pisi', fallback=True)
_ = __trans.gettext


class ListOrphaned(command.Command, metaclass=command.autocommand):
    __doc__ = _("""List orphaned packages

Usage: list-orphaned

Lists packages installed as dependency, but no longer needed by any other installed package.
""")

    def __init__(self, args):
        super(ListOrphaned, self).__init__(args)
        self.installdb = pisi.db.installdb.InstallDB()

    name = ("list-orphaned", "lo")

    def options(self):

        group = optparse.OptionGroup(self.parser, _("list-orphaned options"))
        group.add_option("-a", "--all", action="store_true",
                               default=False, help=_("Show all packages without reverse dependencies"))
        group.add_option("-x", "--exclude", action="append",
                     default=None, help=_("Ignore packages and components whose basenames match pattern."))
        self.parser.add_option_group(group)

    def run(self):

        self.init(database = True, write = False)
        orphaned = self.installdb.get_no_rev_deps() if self.options.all else self.installdb.get_orphaned()

        if self.options.exclude:
            orphaned = pisi.blacklist.exclude(orphaned, ctx.get_option('exclude'))

        if orphaned:
            ctx.ui.info(_("Orphaned packages:"))
            ctx.ui.info(util.format_by_columns(sorted(orphaned)))
        else: ctx.ui.info(_("No orphaned packages"))