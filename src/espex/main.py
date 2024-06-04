import html
import os

import yaml

HOME = os.environ['HOME']
ESPANSO_YAML = os.path.join(HOME, 'Library', 'Application Support',
                            'espanso', 'match', 'base.yml')
PLIST_FILE = os.path.join(HOME, 'Library', 'Preferences',
                          '.GlobalPreferences')
PLIST_TEMPLATE = """<dict>
  <key>shortcut</key>
  <string>{trigger}</string>
  <key>phrase</key>
  <string>{replace}</string>
</dict>
"""

def to_plist(file=ESPANSO_YAML):
    with open(file, 'r') as f:
        rules = yaml.safe_load(f)

    plist = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
'''
    for rule in rules['matches']:
        if 'vars' in rule.values():
            continue
        plist = plist + PLIST_TEMPLATE.format(trigger=html.escape(rule['trigger']),
                                              replace=html.escape(rule['replace']))
    plist = plist + """</array>
</plist>"""

    return plist

def main():
    print(to_plist())
