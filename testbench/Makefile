
TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)
VERILOG_SOURCES   := $(PWD)/../dut/*.sv
TOPLEVEL          := alu_top
MODULE           := tb_NOP,tb_ADD,tb_ADC,tb_SUB,tb_AND,tb_OR,tb_XOR
#MODULE            := tb_AND


export PYTHONPATH := $(PWD)/model:$(PYTHONPATH)

include $(shell cocotb-config --makefiles)/Makefile.sim
