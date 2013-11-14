# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

from .menu_generation import MenuGenerator
from .qt_parent_window import get_qt_parent_window

import sys
if sys.platform == "win32":
    from .win32 import find_windows

def apply_color_scheme():
    # This import needs to be defered to make sure that
    # the sgtk Qt initialization is finished.
    from .color_scheme import QMayaColorScheme
    scheme = QMayaColorScheme()
    scheme.apply()
