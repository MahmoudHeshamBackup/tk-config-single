# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
from sgtk.platform.qt import QtCore, QtGui
from .ui.dialog import Ui_Dialog

def show_dialog(app_instance, cmd_line):
    """
    Shows the dialog.
    """
    app_instance.engine.show_dialog("Error launching Application", app_instance, AppDialog, cmd_line)


class AppDialog(QtGui.QWidget):
    """
    Not found UI dialog.
    """
    
    def __init__(self, cmd_line):
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        QtGui.QWidget.__init__(self)
        
        # now load in the UI that was created in the UI designer
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)
        
        msg = ("<b style='color: rgb(252, 98, 70)'>Failed to launch application!</b> This is most likely because the path "
               "is not set correctly. The command that was used to attempt to launch is '%s'. "
               "<br><br>Click the button below to learn more about how to configure Toolkit to launch "
               "applications." %  cmd_line)
        
        self.ui.message.setText(msg)        
        self.ui.learn_more.clicked.connect(self._launch_docs)
        
    def _launch_docs(self):
        """
        Launches documentation describing how to configure the app launch
        """
        app = sgtk.platform.current_bundle()        
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(app.HELP_DOC_URL))
        self.close()
        
    @property
    def hide_tk_title_bar(self):
        """
        Tell the system to not show the std toolbar
        """
        return True
        
