module alu_top(i_clk, i_en_alu, i_RD, i_RA, i_aluop, o_out, o_cy, o_zy);

	input i_clk, i_en_alu;
	input [7:0] i_RD;		   // RD 8 bit input 
	input [7:0] i_RA;  	   // RA 8 bit input
	input [4:0] i_aluop;         //alu operation 
	output [7:0] o_out;          //alu operation output
	output o_cy, o_zy;             //carry and zero flag

        reg i_reset;

        alu alu_dut(i_clk, i_en_alu, i_RD, i_RA, i_aluop, o_out, o_cy, o_zy, i_reset);

        initial begin
           $dumpfile("alu_wave.vcd");
           $dumpvars(0, alu_top);
        end

        initial begin
              i_reset = 0;
          #20 i_reset = 1;
          #30 i_reset = 0;
        end

endmodule