#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Dvbs2 Tx
# GNU Radio version: 3.7.13.5
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import dtv
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import limesdr
import pmt
import sip
import sys
from gnuradio import qtgui


class dvbs2_tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Dvbs2 Tx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Dvbs2 Tx")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "dvbs2_tx")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Variables
        ##################################################
        self.symbol_rate = symbol_rate = 5000000
        self.vga2_gain = vga2_gain = 10
        self.vga1_gain = vga1_gain = -8
        self.tx_gain = tx_gain = 50
        self.taps = taps = 100
        self.samp_rate = samp_rate = symbol_rate * 2
        self.rolloff = rolloff = 0.2
        self.center_freq = center_freq = 1280e6

        ##################################################
        # Blocks
        ##################################################
        self._vga2_gain_range = Range(0, 25, 1, 10, 200)
        self._vga2_gain_win = RangeWidget(self._vga2_gain_range, self.set_vga2_gain, "vga2_gain", "counter_slider", int)
        self.top_grid_layout.addWidget(self._vga2_gain_win)
        self._vga1_gain_range = Range(-35, -4, 1, -8, 200)
        self._vga1_gain_win = RangeWidget(self._vga1_gain_range, self.set_vga1_gain, "vga1_gain", "counter_slider", int)
        self.top_grid_layout.addWidget(self._vga1_gain_win)
        self._tx_gain_range = Range(0, 89, 1, 50, 200)
        self._tx_gain_win = RangeWidget(self._tx_gain_range, self.set_tx_gain, "tx_gain", "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_gain_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.limesdr_sink_0 = limesdr.sink('000907060247230D', 0, '', '')
        self.limesdr_sink_0.set_sample_rate(samp_rate)
        self.limesdr_sink_0.set_center_freq(center_freq, 0)
        self.limesdr_sink_0.set_bandwidth(5e6,0)
        self.limesdr_sink_0.set_gain(10,0)
        self.limesdr_sink_0.set_antenna(255,0)
        self.limesdr_sink_0.calibrate(16e6, 0)

        self.fft_filter_xxx_0 = filter.fft_filter_ccc(1, (firdes.root_raised_cosine(0.9, samp_rate, samp_rate/2, rolloff, taps)), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self.dtv_dvbs2_physical_cc_0 = dtv.dvbs2_physical_cc(dtv.FECFRAME_NORMAL, dtv.C9_10, dtv.MOD_16APSK, dtv.PILOTS_ON, 0)
        self.dtv_dvbs2_modulator_bc_0 = dtv.dvbs2_modulator_bc(dtv.FECFRAME_NORMAL,
        dtv.C9_10, dtv.MOD_16APSK, dtv.INTERPOLATION_OFF)
        self.dtv_dvbs2_interleaver_bb_0 = dtv.dvbs2_interleaver_bb(dtv.FECFRAME_NORMAL, dtv.C9_10, dtv.MOD_16APSK)
        self.dtv_dvb_ldpc_bb_0 = dtv.dvb_ldpc_bb(dtv.STANDARD_DVBS2, dtv.FECFRAME_NORMAL, dtv.C9_10, dtv.MOD_OTHER)
        self.dtv_dvb_bch_bb_0 = dtv.dvb_bch_bb(dtv.STANDARD_DVBS2, dtv.FECFRAME_NORMAL, dtv.C9_10)
        self.dtv_dvb_bbscrambler_bb_0 = dtv.dvb_bbscrambler_bb(dtv.STANDARD_DVBS2, dtv.FECFRAME_NORMAL, dtv.C9_10)
        self.dtv_dvb_bbheader_bb_0 = dtv.dvb_bbheader_bb(dtv.STANDARD_DVBS2, dtv.FECFRAME_NORMAL, dtv.C9_10, dtv.RO_0_20, dtv.INPUTMODE_NORMAL, dtv.INBAND_OFF, 168, 4000000)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/nithish/Downloads/advatsc.ts', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.dtv_dvb_bbheader_bb_0, 0))
        self.connect((self.dtv_dvb_bbheader_bb_0, 0), (self.dtv_dvb_bbscrambler_bb_0, 0))
        self.connect((self.dtv_dvb_bbscrambler_bb_0, 0), (self.dtv_dvb_bch_bb_0, 0))
        self.connect((self.dtv_dvb_bch_bb_0, 0), (self.dtv_dvb_ldpc_bb_0, 0))
        self.connect((self.dtv_dvb_ldpc_bb_0, 0), (self.dtv_dvbs2_interleaver_bb_0, 0))
        self.connect((self.dtv_dvbs2_interleaver_bb_0, 0), (self.dtv_dvbs2_modulator_bc_0, 0))
        self.connect((self.dtv_dvbs2_modulator_bc_0, 0), (self.dtv_dvbs2_physical_cc_0, 0))
        self.connect((self.dtv_dvbs2_physical_cc_0, 0), (self.fft_filter_xxx_0, 0))
        self.connect((self.fft_filter_xxx_0, 0), (self.limesdr_sink_0, 0))
        self.connect((self.fft_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "dvbs2_tx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.set_samp_rate(self.symbol_rate * 2)

    def get_vga2_gain(self):
        return self.vga2_gain

    def set_vga2_gain(self, vga2_gain):
        self.vga2_gain = vga2_gain

    def get_vga1_gain(self):
        return self.vga1_gain

    def set_vga1_gain(self, vga1_gain):
        self.vga1_gain = vga1_gain

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.fft_filter_xxx_0.set_taps((firdes.root_raised_cosine(0.9, self.samp_rate, self.samp_rate/2, self.rolloff, self.taps)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)
        self.fft_filter_xxx_0.set_taps((firdes.root_raised_cosine(0.9, self.samp_rate, self.samp_rate/2, self.rolloff, self.taps)))

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.fft_filter_xxx_0.set_taps((firdes.root_raised_cosine(0.9, self.samp_rate, self.samp_rate/2, self.rolloff, self.taps)))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)
        self.limesdr_sink_0.set_center_freq(self.center_freq, 0)


def main(top_block_cls=dvbs2_tx, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
