from cocotb_test.simulator import run
import os, sys
import platform

#tests_dir = os.path.dirname(__file__)

pwd = os.getcwd()

verilog_top = ""
verilog_src = ""

if(platform.system() == 'Windows'):
  verilog_top = pwd+'\\..\\dut\\alu_top.sv'
  verilog_src = pwd+'\\..\\dut\\alu.sv'

elif(platform.system() == 'Linux'):
  verilog_top = pwd +'/../dut/alu_top.sv'
  verilog_src = pwd +'/../dut/alu.sv'

else:
   print("Operating system not detected by script. exiting...")
   sys.exit()


def run_sample(testname = "tb_ADD"):
   run( verilog_sources=[verilog_top, verilog_src], # sources
        toplevel="alu_top",                         # top level HDL
        module=testname                             # name of cocotb test module
   )


def test_run():
   #run_sample(testname = "tb_ADD")
   run_sample(testname = "tb_XOR")