# SPDX-FileCopyrightText: 2022-2025 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: CC0-1.0
import pytest
from pytest_embedded import Dut
from pytest_embedded_idf.utils import idf_parametrize


@pytest.mark.generic
@idf_parametrize('target', ['esp32', 'esp32s3'], indirect=['target'])
def test_ipc_isr_xtensa(dut: Dut) -> None:
    dut.expect_exact('example: Start')
    dut.expect_exact('example: PS_INTLEVEL = 0x5')
    dut.expect_exact('example: PS_EXCM = 0x0')
    dut.expect_exact('example: PS_UM = 0x1')
    dut.expect_exact('example: in[0] = 0x1')
    dut.expect_exact('example: in[1] = 0x2')
    dut.expect_exact('example: in[2] = 0x3')
    dut.expect_exact('example: out[0] = (in[0] | in[1] | in[2]) = 0x3')
    dut.expect_exact('example: out[1] = (in[0] + in[1] + in[2]) = 0x6')
    dut.expect_exact('example: out[2] = in[2] = 0x3')
    dut.expect_exact('example: out[3] = PS of other cpu = 0x25')
    dut.expect_exact('example: End')
