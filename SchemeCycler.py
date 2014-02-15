#!/usr/bin/python
# -*- coding: utf-8 -*-

import sublime, sublime_plugin
import os


def dirname(path):
    return path.rsplit('/', 1)[0]


def basename(path):
    return path.rsplit('/', 1)[1]


def fix_path(path):
    return path.replace('\\', '/')


def friendly_name(filename):
    return basename(filename).decode('utf-8').rsplit('.', 1)[0]


def cycle_scheme(backward=False, purge=False):
    settings = sublime.load_settings('Preferences.sublime-settings')
    current_scheme = settings.get('color_scheme')

    raw_path = sublime.packages_path()
    package_path = fix_path(raw_path)

    schemes = ['/'.join([
            fix_path(dirpath[len(dirname(package_path)) + 1:]),
            filename,
        ])
        for dirpath, _, filenames in os.walk(package_path)
        for filename in filenames if filename.endswith('.tmTheme')
    ]
    schemes.sort(key=lambda x: basename(x))

    i = schemes.index(current_scheme) + (backward and -1 or 1)
    i = 0 if i == len(schemes) else len(schemes) - 1 if i == -1 else i

    scheme = schemes[i]
    if not scheme:
        return

    settings.set('color_scheme', scheme)
    sublime.save_settings('Preferences.sublime-settings')

    sublime.status_message(
        u'Color Scheme: ' + friendly_name(scheme)
    )

    if purge:
        purge_scheme(raw_path.rstrip('Packages'), current_scheme)



def purge_scheme(path, scheme):
    friendly = friendly_name(scheme);

    if sublime.ok_cancel_dialog('Are you sure you want to delete "'+friendly+'"?'):
        try:
            os.remove(path+scheme)
            sublime.status_message('Deleted '+friendly)
        except:
            sublime.status_message('Could not delete '+scheme+' from '+path)

        # Doesn't matter if we can't get rid of cache, so do it last
        os.remove(path+scheme+'.cache')
    else:
        sublime.status_message('Theme not removed, user cancelled operation')


class NextColorSchemeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cycle_scheme()

class DeleteThenNextColorSchemeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cycle_scheme(backward=False, purge=True)

class PreviousColorSchemeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cycle_scheme(backward=True)

class DeleteThenPreviousColorSchemeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cycle_scheme(backward=True, purge=True)
