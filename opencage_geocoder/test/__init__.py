# import qgis libs so that ve set the correct sip api version
import atexit
import os
import tempfile

import qgis   # pylint: disable=W0611  # NOQA

from qgis.core import QgsApplication

# Initialise a headless QGIS application so the tests have a valid application
# path (silences "Application path not initialized"). The prefix is auto-detected.
if QgsApplication.instance() is None:
    # Write the QGIS profile (symbology-style.db, etc.) to a temp dir so test
    # runs don't litter the working tree.
    os.environ.setdefault("QGIS_CUSTOM_CONFIG_PATH",
                          tempfile.mkdtemp(prefix="qgis-test-"))
    _qgs_app = QgsApplication([], False)
    _qgs_app.initQgis()
    # Tear down cleanly on exit (silences "QThreadStorage ... destroyed").
    atexit.register(_qgs_app.exitQgis)