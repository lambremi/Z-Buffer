// Module to store pixels
module memoryBlock #(parameter MEM_LENGTH = 8, PIX_WIDTH = 16)(
    input logic clk,
    input logic reset,  // Syncronous Active high reset (More Robust mapping on FPGA)

	// Inputs
    input logic [PIX_WIDTH-1:0] pix_in,
	input logic RW,
	input logic [MEM_LENGTH-1:0] address,
	input logic enable,

    // Outputs
    output logic [PIX_WIDTH-1:0] pix_out,
	output logic ack_out
);


// == Variables Declaration ====================================================
logic last_ack;

// == Main Code ================================================================
always @(posedge clk) begin
	if (reset) begin
		ack_out = 0;
		pix_out = 0;
	end

	if (enable && ~RW) begin
		ack_out = 1;
		pix_out = address;
		last_ack = 1;
	end
	else if(last_ack) last_ack = 0;
	else begin
		ack_out = 0;
		pix_out = 0;
	end
end

endmodule
