from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5 import QtCore
import sys



class SecondUI(QMainWindow):
    def __init__(self):
        super(SecondUI, self).__init__()

        # Load interface
        loadUi ("colorimeter_startup_values_interface.ui", self)

        




    def colorimeter_reload_parameters_from_eeprom (self):

        print ("Colorimeter_reload_parameters_from_EEPROM launched!")

        # Read from device Autorange
        command_py = ":EEPROM:CONFigure:AUTOrange?\n"
        buffer_length = len (command_py)
        timeout_ms = 5000
        error_write = py_usbtmc_write(ptr_handle_colorimeter, command_py.encode('ASCII'), buffer_length, timeout_ms)
        bytecount = 4096
        read_data = ctypes.create_string_buffer (bytecount)
        error_read = py_usbtmc_read (ptr_handle_colorimeter, read_data, bytecount, timeout_ms)

        ar_read = read_data.value.decode("utf-8")[:error_read].strip()
        
        if (ar_read == "Closed") or (ar_read == "Opened"):
            # Reread Autorange
            print ("AUTORANGE: Closed/Opened received")
            self.colorimeter_reload_parameters_from_eeprom()
        elif (ar_read == ""):
            print ("AUTORANGE: No reply received")
            return
        else:
            print ("AUTORANGE: " + ar_read)
            self.comboBox_autorange_eeprom.blockSignals(True)
            self.comboBox_autorange_eeprom.setCurrentIndex (int(ar_read))
            self.comboBox_autorange_eeprom.blockSignals(False)
        

        # Read from device Int. Time
        # command_py = ":SENSe:INT?\n"
        # buffer_length = len (command_py)
        # timeout_ms = 5000
        # error_write = py_usbtmc_write(ptr_handle_colorimeter, command_py.encode('ASCII'), buffer_length, timeout_ms)
        # bytecount = 4096
        # read_data = ctypes.create_string_buffer (bytecount)
        # error_read = py_usbtmc_read (ptr_handle_colorimeter, read_data, bytecount, timeout_ms)
        # int_time_read = int (read_data.value.decode("utf-8")[:error_read])
        # self.lineEdit_int_time.setText (str(int_time_read))





 

        # Read from device Average - EEPROM
        command_py = ":EEPROM:CONFigure:AVG?\n"
        buffer_length = len (command_py)
        timeout_ms = 5000
        error_write = py_usbtmc_write(ptr_handle_colorimeter, command_py.encode('ASCII'), buffer_length, timeout_ms)
        bytecount = 4096
        read_data = ctypes.create_string_buffer (bytecount)
        error_read = py_usbtmc_read (ptr_handle_colorimeter, read_data, bytecount, timeout_ms)
        avg_read = int (read_data.value.decode("utf-8")[:error_read])
        self.lineEdit_eeprom_avg.setText (str(avg_read))

        # Read from device Gain
        # command_py = ":SENSe:GAIN?\n"
        # buffer_length = len (command_py)
        # timeout_ms = 5000
        # error_write = py_usbtmc_write(ptr_handle_colorimeter, command_py.encode('ASCII'), buffer_length, timeout_ms)
        # bytecount = 4096
        # read_data = ctypes.create_string_buffer (bytecount)
        # error_read = py_usbtmc_read (ptr_handle_colorimeter, read_data, bytecount, timeout_ms)
        # gain_read = int (read_data.value.decode("utf-8")[:error_read])
        # # print (f"Gain index from reload parameters is {gain_read}")
        # self.comboBox_gain.blockSignals(True)
        # self.comboBox_gain.setCurrentIndex (gain_read-1)
        # self.comboBox_gain.blockSignals(False)

        # Read from device Calibration Matrix
        # command_py = ":SENSe:SBW?\n"
        # buffer_length = len (command_py)
        # timeout_ms = 5000
        # error_write = py_usbtmc_write(ptr_handle_colorimeter, command_py.encode('ASCII'), buffer_length, timeout_ms)
        # bytecount = 4096
        # read_data = ctypes.create_string_buffer (bytecount)
        # error_read = py_usbtmc_read (ptr_handle_colorimeter, read_data, bytecount, timeout_ms)
        # sbw_read = read_data.value.decode("utf-8")[:error_read].strip()
        # # print (f"SBW is -{sbw_read}-")
        # index_comboBox_sbw = self.comboBox_sbw.findText (sbw_read)
        # # print (f"Index combo is {index_comboBox_sbw}")
        # self.comboBox_sbw.blockSignals(True)
        # self.comboBox_sbw.setCurrentIndex (index_comboBox_sbw)
        # self.comboBox_sbw.blockSignals(False)

        # Read from device Automode
        # command_py = ":SENSe:AUTOMODE?\n"
        # buffer_length = len (command_py)
        # timeout_ms = 5000
        # error_write = py_usbtmc_write(ptr_handle_colorimeter, command_py.encode('ASCII'), buffer_length, timeout_ms)
        # bytecount = 4096
        # read_data = ctypes.create_string_buffer (bytecount)
        # error_read = py_usbtmc_read (ptr_handle_colorimeter, read_data, bytecount, timeout_ms)
        # automode_read = int (read_data.value.decode("utf-8")[:error_read])
        # print (f"Automode is -{automode_read}-")
        # if automode_read == 255:
        #     automode_read = 5
        # self.comboBox_automode.blockSignals(True)
        # self.comboBox_automode.setCurrentIndex (automode_read)
        # self.comboBox_automode.blockSignals(False)

        # Read from device Autorange parameters
        # command_py = ":SENSe:ARPARMS?\n"
        # buffer_length = len (command_py)
        # timeout_ms = 5000
        # error_write = py_usbtmc_write(ptr_handle_colorimeter, command_py.encode('ASCII'), buffer_length, timeout_ms)
        # bytecount = 4096
        # read_data = ctypes.create_string_buffer (bytecount)
        # error_read = py_usbtmc_read (ptr_handle_colorimeter, read_data, bytecount, timeout_ms)
        # arparms_read = read_data.value.decode("utf-8")[:error_read].strip().split(",")
        # # print (f"Autorange parameters are -{arparms_read}-")
        # ar_freq = float (arparms_read[0])
        # self.lineEdit_ar_freq.setText (f"{ar_freq:0.6f}")
        # ar_adjmin = int (arparms_read[1])
        # self.lineEdit_ar_adjmin.setText (str (ar_adjmin))
        # ar_frames = int (arparms_read[2])
        # self.lineEdit_ar_frames.setText (str (ar_frames))
        # ar_max_int_time = int (arparms_read[3])
        # self.lineEdit_ar_max_int_time.setText (str(ar_max_int_time))
        # ar_avg = int (arparms_read[4])
        # self.lineEdit_ar_avg.setText (str(ar_avg))

        # Read from device DUT Autorange Freq
        # command_py = ":SENSe:FREQ?\n"
        # buffer_length = len (command_py)
        # timeout_ms = 5000
        # error_write = py_usbtmc_write(ptr_handle_colorimeter, command_py.encode('ASCII'), buffer_length, timeout_ms)
        # bytecount = 4096
        # read_data = ctypes.create_string_buffer (bytecount)
        # error_read = py_usbtmc_read (ptr_handle_colorimeter, read_data, bytecount, timeout_ms)
        # dut_freq_read = float (read_data.value.decode("utf-8")[:error_read])
        # # print (f"dut freq is {dut_freq_read}")
        # self.lineEdit_dut_ar_freq.setText (f"{dut_freq_read:0.3f}")




if __name__ == "__main__":
    
    # This will not run on import !

    # Enable High DPI display with PyQt5
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    # QApplication.setHighDpiScaleFactorRoundingPolicy (QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setHighDpiScaleFactorRoundingPolicy (QtCore.Qt.HighDpiScaleFactorRoundingPolicy.Ceil)
    
    app2 = QApplication (sys.argv)
    window2 = SecondUI()
    window2.show()
    app2.exec_()