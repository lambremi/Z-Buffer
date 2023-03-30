//Module ContentionTree
module contention_tree #(parameter integer LENGTH = 8, parameter PIXEL_WIDTH = 8)
	(
	input logic	[PIXEL_WIDTH-1:0]	pix_in_1,
	input logic	[PIXEL_WIDTH-1:0]	pix_in_2,
	input logic	[PIXEL_WIDTH-1:0]	pix_in_3,
	input logic	[PIXEL_WIDTH-1:0]	pix_in_4,
	input logic							clk,
	input logic	 [LENGTH-1:0] fill_1,
	input logic	 [LENGTH-1:0] fill_2,
	input logic	 [LENGTH-1:0] fill_3,
	input logic	 [LENGTH-1:0] fill_4,
	input logic							rdy_z_buffer,
	input logic							ack_1,
	input logic							ack_2,
	input logic							ack_3,
	input logic							ack_4,
	output logic						req_1,
	output logic						req_2,
	output logic						req_3,
	output logic						req_4,
	output logic 						send_z_buffer,
	output logic	[PIXEL_WIDTH-1:0]	pix_out
);
// == Variable Declaration =======================
	
typedef enum logic [2:0] {
		RESET,
		HARVEST,
		SEND,
		WAIT,
} fsm_state_t;

fsm_state_t current_state;
fsm_state_t next_state;

// == Main Code ==================================
always_ff @(posedge clk)
begin 
	if (reset) begin
		current_state <= RESET;
	end
	else begin
		current_state <= next_state;
	end
end

always_comb
begin
	case(current_state)
	 RESET: begin
			req_1 = 0;
			req_2 = 0;
			req_3 = 0;
			req_4 = 0;
			send_z_buffer = 0;
			assign pix_out = PIXEL_WIDTH'bz;
			if (rdy_z_buffer) next_state = HARVEST;
			else next_state = RESET;
	 end

	 HARVEST: begin
			if (fill_1 == 0 && fill_2 == 0 && fill_3 == 0 && fill_4 == 0) begin
				next_state = HARVEST;
			end
			else if (fill_1 >= fill_2 && fill_1 >= fill_3 && fill_1 >= fill_4) begin
				req_1 = 1;
				next_state = SEND;
			end
			else if (fill_2 > fill_1 && fill_2 >= fill_3 && fill_2 >= fill_4) begin
				req_2 = 1;
				next_state = SEND;
			end	 
			else if (fill_3 > fill_1 && fill_3 > fill_2 && fill_3 >= fill_4) begin
				req_3 = 1;
				next_state = SEND;
			end
			else begin
				req_4 = 1;
				next_state = SEND;
			end
	 end

	 SEND: begin
			if (ack_1) begin
				assign pix_out = pix_in_1;
				send_z_buffer = 1;
				next_state = WAIT;
			end
			else if (ack_2) begin
				assign pix_out = pix_in_2;
				send_z_buffer = 1;
				next_state = WAIT;
			end
			else if (ack_3) begin
				assign pix_out = pix_in_3;
				send_z_buffer = 1;
				next_state = WAIT;
			end
			else if (ack_4) begin
				assign pix_out = pix_in_4;
				send_z_buffer = 1;
				next_state = WAIT;
			end
	 end	

	 WAIT: begin
			if (!rdy_z_buffer) begin
				send_z_buffer = 0;
				next_state = RESET;
			end
			else begin
				next_state = WAIT;
			end
	 end
	endcase
end
endmodule