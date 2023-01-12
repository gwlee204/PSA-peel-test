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


from ui_mainwindow import Ui_MainWindow


def set_path(ui: Ui_MainWindow):
    import tkinter.filedialog as fd

    data_path = fd.askdirectory(title='select peel test file path')

    ui.ui_datapath.setText(data_path)
    if data_path:
        set_filelist(ui)


def set_filelist(ui: Ui_MainWindow):
    import os

    all_files = os.listdir(ui.ui_datapath.text())
    csv_files = []

    for file in all_files:
        if file != 'results.csv' and file[-3:] == 'csv':
            csv_files.append(file)

    if len(csv_files) == 0:
        ui.statusbar.showMessage('Data directory does not have csv files')
        return

    ui.ui_filelist.addItems(csv_files)


def set_datatable(ui: Ui_MainWindow):
    from peel import peel_test
    from PyQt5 import QtWidgets

    filename = ui.ui_filelist.currentItem().text()
    filepath = f'{ui.ui_datapath.text()}/{filename}'
    data, average, stdev = peel_test(filepath)

    ui.ui_datatable.setRowCount(data.shape[0])
    ui.ui_datatable.setColumnCount(data.shape[1])
    ui.ui_datatable.setHorizontalHeaderLabels(data.columns)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ui.ui_datatable.setItem(i, j, QtWidgets.QTableWidgetItem(str(data.iloc[i, j])))

    ui.ui_average.setText(str(average))
    ui.ui_stdev.setText(str(stdev))

    set_graph(ui, data)


def init_graph(ui: Ui_MainWindow):
    ui.ui_graph.setBackground('w')
    ui.ui_graph.plotItem.setLabel('bottom', 'Displacement (mm)', color='#000000')
    ui.ui_graph.plotItem.setLabel('left', 'Peel strength (N/25mm)', color='#000000')


def set_graph(ui: Ui_MainWindow, data):
    import pyqtgraph as pg

    ui.ui_graph.plotItem.clear()
    ui.ui_graph.plotItem.plot(data.iloc[:, 2].to_list(), data.iloc[:, 3].to_list(), pen='r')
    max_displacement = max(data.iloc[:, 2].to_list())
    ui.ui_graph.plotItem.addItem(pg.InfiniteLine(max_displacement / 4))
    ui.ui_graph.plotItem.addItem(pg.InfiniteLine(max_displacement / 4 * 3))


def save_data(ui: Ui_MainWindow):
    import os
    import pandas as pd
    from peel import peel_test

    import tkinter.filedialog as fd

    result_file_path = fd.asksaveasfilename(
        title='select result file save path',
        defaultextension='csv',
        filetypes=(('csv file', '.csv'),),
        initialfile='results',
    )

    if result_file_path == '':
        return

    all_files = os.listdir(ui.ui_datapath.text())
    csv_files = []

    for file in all_files:
        if file != 'results.csv' and file[-3:] == 'csv':
            csv_files.append(file)

    results = []
    for filename in csv_files:
        try:
            result = peel_test(f'{ui.ui_datapath.text()}/{filename}')
        except:
            pass
        results.append([f'{filename}', result[1], result[2]])
    results_df = pd.DataFrame(
        results, columns=['filename', 'average peel strength (N/25mm)', 'standard deviation']
    )
    results_df.to_csv(result_file_path)

    ui.statusbar.showMessage('SAVING RESULT SUCCESS!')
