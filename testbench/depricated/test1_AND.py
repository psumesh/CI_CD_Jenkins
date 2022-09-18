#from cocotb_test.simulator import run
#import pytest
#import os

#tests_dir = os.path.dirname(__file__)

#@pytest.mark.skipif(os.getenv("SIM") == "ghdl", reason="Verilog not suported")

#def test_dff_verilog():
#    run(verilog_sources=[os.path.join(tests_dir, "dff.sv")], toplevel="dff_test", module="dff_cocotb", waves=True)  # sources  # top level HDL  # name of cocotb test module

#if __name__ == "__main__":
#    test_dff_verilog()

