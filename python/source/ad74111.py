# ----- Imports -----
# builtins
from __future__ import annotations
import logging
from dataclasses import dataclass
from enum import IntEnum

# external packages

# internal packages

# ----- Helper Functions -----

# ----- Helper Classes -----
# @dataclass
# class _Field():
#     wi

# class _Reg():
#     class _Field_

# class _Reg_A(_Reg):
#     # register fields
#     class 


# ----- Public API -----

class AD74111():
    def __init__(self) -> None:
        pass

    # --- register access ---
    # register a
    def adc_input_amp_enable(self) -> bool:
        pass

    def adc_input_amp_disable(self) -> bool:
        pass

    def adc_input_amp_is_enabled(self) -> bool:
        pass

    def adc_enable(self) -> bool:
        pass

    def adc_disable(self) -> bool:
        pass

    def adc_is_enabled(self) -> bool:
        pass

    def vref_enable(self) -> bool:
        pass

    def vref_disable(self) -> bool:
        pass

    def vref_is_enabled(self) -> bool:
        pass

    def vref_amp_enable(self) -> bool:
        pass

    def vref_amp_disable(self) -> bool:
        pass

    def vref_amp_is_enabled(self) -> bool:
        pass

    # register b
    mclk_divs = (1, 2, 3)

    mclk_div_one = {
        1 : 0b00,
        2 : 0b01,
        4 : 0b10,
    }

    mclk_div_two = {
        1 : 0b00,
        2 : 0b01,
        3 : 0b10,
    }

    mclk_div_three = {
        1 : 0b00,
        2 : 0b01,
        3 : 0b10,
    }

    def mclk_divider_set(self, div_num: int, div_val: int) -> bool:
        pass

    def mclk_divider_get(self, div_num: int) -> int:
        pass

    # register c
    word_widths = {
        16 : 0b00,
        20 : 0b01,
        24 : 0b10
    }

    filt_freqs_khz = {
        0   : 0b00,
        44.1: 0b01,
        32  : 0b10,
        48  : 0b11,
    }

    def word_width_set(self, width: int) -> bool:
        pass

    def word_width_get(self) -> int:
        pass

    def low_group_delay_enable(self) -> bool:
        pass

    def low_group_delay_disable(self) -> bool:
        pass

    def low_group_delay_is_enabled(self) -> bool:
        pass

    def dac_filt_freq_set(self, freq: int) -> bool:
        pass

    def dac_filt_freq_get(self) -> int:
        pass

    def adc_filt_enable(self) -> bool:
        pass

    def adc_filt_disable(self) -> bool:
        pass

    def adc_filt_is_enabled(self) -> bool:
        pass

    # register d
    def data_mode_enable(self) -> bool:
        pass

    def dsp_mode_width_set(self, width: int) -> bool:
        pass

    def dsp_mode_width_get(self) -> int:
        pass

    def fast_dclk_enable(self) -> bool:
        pass

    def fast_dclk_disable(self) -> bool:
        pass

    def fast_dclk_is_enabled(self) -> bool:
        pass

    # register e
    adc_gain_db = {
        0   : 0b000,
        3   : 0b001,
        6   : 0b010,
        9   : 0b011,
        12  : 0b100,
    }

    def adcl_peak_enable(self) -> bool:
        pass

    def adcl_peak_disable(self) -> bool:
        pass

    def adcl_peak_is_enabled(self) -> bool:
        pass

    def adc_gain_db_set(self, gain: int) -> bool:
        pass

    def adc_gain_db_get(self) -> int:
        pass

    def adc_mute_enable(self) -> bool:
        pass

    def adc_mute_disable(self) -> bool:
        pass

    def adc_mute_is_enabled(self) -> bool:
        pass

    def dac_mute_enable(self) -> bool:
        pass

    def dac_mute_disable(self) -> bool:
        pass

    def dac_mute_is_enabled(self) -> bool:
        pass

    # register f
    def adc_input_level_peak_get(self) -> int:
        pass

    # register g
    def dac_attenuation_set(self, atten_level: int) -> bool:
        pass