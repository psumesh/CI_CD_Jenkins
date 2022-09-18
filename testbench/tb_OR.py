from pkg.base_pkg import *

@cocotb.test()
async def tb_OR(dut):
      
      D_var   = alu_library(dut)
      
      cocotb.start_soon(D_var.clock())
      cocotb.start_soon(D_var.alu_enable())
      dut.i_aluop.value = 5
      dut.i_RD.value    = 15
      dut.i_RA.value    = 10
      for i in range(4):
        await RisingEdge(dut.i_clk);
        pass
      assert dut.o_out == 15, print("AND operation mismatching")

      for i in range(25):
          await Timer(10, units = 'ns')       