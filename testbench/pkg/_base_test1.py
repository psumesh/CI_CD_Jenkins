import cocotb
from cocotb.triggers import Timer
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

       def NOP(self):
          self.i_aluop <= 0;
          self.i_RD    <= 255
          self.i_RA    <= 255

       def ADD(self, RA, RD):
          self.i_aluop <= 1
          self.i_RA    <= RA
          self.i_RD    <= RD

       def ADC(self, RA, RD):
          self.i_aluop <= 2
          self.i_RA    <= RA
          self.i_RD    <= RD

       def SUB(self, RA, RD):
          self.i_aluop <= 3
          self.i_RA    <= RA
          self.i_RD    <= RD

       def AND(self, RA, RD):
          self.i_aluop <= 4
          self.i_RA    <= RA
          self.i_RD    <= RD

       def OR(self, RA, RD):
          self.i_aluop <= 5
          self.i_RA    <= RA
          self.i_RD    <= RD

       def XOR(self, RA, RD):
          self.i_aluop <= 6
          self.i_RA    <= RA
          self.i_RD    <= RD

       def INC(self, RA, RD):
          self.i_aluop <= 7
          self.i_RA    <= RA
          self.i_RD    <= RD

       def DEC(self, RA, RD):
          self.i_aluop <= 8
          self.i_RA    <= RA
          self.i_RD    <= RD

       def COMP(self, RA, RD):
          self.i_aluop <= 9
          self.i_RA    <= RA
          self.i_RD    <= RD

       def LSR(self, RA, RD):
          self.i_aluop <= 10
          self.i_RA    <= RA
          self.i_RD    <= RD

       def CP_CPI(self, RA, RD):
          self.i_aluop <= 11
          self.i_RA    <= RA
          self.i_RD    <= RD

       def ROR(self, RA, RD):
          self.i_aluop <= 12
          self.i_RA    <= RA
          self.i_RD    <= RD

       def COMP_2(self, RA, RD):
          self.i_aluop <= 13
          self.i_RA    <= RA
          self.i_RD    <= RD

       def ASR(self, RA, RD):
          self.i_aluop <= 14
          self.i_RA    <= RA
          self.i_RD    <= RD

       def SWAP(self, RA, RD):
          self.i_aluop <= 15
          self.i_RA    <= RA
          self.i_RD    <= RD
          

       @cocotb.coroutine
       def clock(self, periods=40, units='ns'):                    #global clock signal
        self.dut._log.info("Clock started")
        while True:
            self.i_clk <= 0
            yield Timer(periods/2, units)
            self.i_clk <= 1
            yield Timer(periods/2, units)

       @cocotb.coroutine
       def alu_enable(self):
         self.dut._log.info("AlU is activated now")
         yield Timer(1, units='ns')
         self.i_en_alu.value = 1

       @cocotb.coroutine
       async def tb_generator(self, aluop, RD=15, RA=10):
           self.i_aluop <= aluop
           self.i_RD    <= RD
           self.i_RA    <= RA
           #write test case based on alu_op
           if(aluop==0):
              self.NOP()
           elif(aluop==1):
              self.ADD(RA, RD)
           elif(aluop==2):
              self.ADC(RA, RD)
           elif(aluop==3):
              self.SUB(RA, RD)
           elif(aluop==4):
              self.AND(RA, RD)
           elif(aluop==5):
              self.OR(RA, RD)
           elif(aluop==6):
              self.XOR(RA, RD)
           elif(aluop==7):
              self.INC(RA, RD)
           elif(aluop==8):
              self.DEC(RA, RD)
           elif(aluop==9):
              self.COMP(RA, RD)
           elif(aluop==10):
              self.LSR(RA, RD)
           elif(aluop==11):
              self.CP_CPI(RA, RD)
           elif(aluop==12):
              self.ROR(RA, RD)
           elif(aluop==13):
              self.COMP_2(RA, RD)
           elif(aluop==14):
              self.ASR(RA, RD)
           elif(aluop==15):
              self.SWAP(RA, RD)
               
        