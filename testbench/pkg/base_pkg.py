import cocotb
from cocotb.triggers import Timer, RisingEdge, FallingEdge, Edge
from cocotb.clock import Clock
from random import randint
from cocotb_coverage.coverage import *

class alu_library(object):

       def __init__(self, dut):
           self.dut      = dut
           self.i_clk    = dut.i_clk
           self.i_en_alu = dut.i_en_alu
           self.i_RD     = dut.i_RD
           self.i_RA     = dut.i_RA
           self.i_aluop  = dut.i_aluop
           self.o_out    = dut.o_out
           self.o_cy     = dut.o_cy
           self.o_zy     = dut.o_zy

          

       @cocotb.coroutine
       def clock(self, periods=40, units='ns'):                    #global clock signal
        self.dut._log.info("Clock started")
        #self.i_RD.value = 10
        #self.i_RA.value = 5
        while True:
            self.i_clk.value = 0
            yield Timer(periods/2, units)
            self.i_clk.value = 1
            yield Timer(periods/2, units)

       @cocotb.coroutine
       def alu_enable(self):
         for i in range(2):
             yield RisingEdge(self.i_clk)
         self.dut._log.info("-----ALU is activated now-----")
         self.i_en_alu.value = 1
               

         