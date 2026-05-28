# import qgis libs so that ve set the correct sip api version
import qgis   # pylint: disable=W0611  # NOQA

from qgis.core import QgsApplication

# Initialise a headless QGIS application so the tests have a valid application
# path (silences "Application path not initialized"). The prefix is auto-detected.
if QgsApplication.instance() is None:
    _qgs_app = QgsApplication([], False)
    _qgs_app.initQgis()