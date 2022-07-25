# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    A = 30
    B = 2

    # input driving
    dut.inp30.value = B
    dut.sel.value = A

    await Timer(2, units='ns')

    assert dut.out.value ==B , "test failed"

@cocotb.test()
async def test_mux1(dut):
   
    cocotb.log.info('##### CTB: Develop your test here ########')
    c = 12
    d = 1

    # input driving
    dut.inp12.value = d
    dut.sel.value = c

    

    await Timer(2, units='ns')

    assert dut.out.value ==d , "test failed"
