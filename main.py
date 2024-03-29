# MIT License

# Copyright (c) 2023 Geon-woo Lee

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


if __name__ == '__main__':
    import sys
    from PyQt6 import QtWidgets
    from ui_mainwindow import Ui_MainWindow
    from qt_material import apply_stylesheet
    from peel_ui import set_path, set_datatable, init_graph, save_data

    app = QtWidgets.QApplication(sys.argv)

    extra = {
        'density_scale': '-1',
    }
    apply_stylesheet(app, theme='light_blue.xml', invert_secondary=True, extra=extra)

    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    init_graph(ui)

    ui.ui_datapath_btn.clicked.connect(lambda: set_path(ui))
    ui.ui_filelist.currentItemChanged.connect(lambda: set_datatable(ui))
    ui.ui_save.clicked.connect(lambda: save_data(ui))

    MainWindow.show()
    sys.exit(app.exec())
