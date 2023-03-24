//Module ContentionTree
module contention_tree #(parameter integer LENGTH = 8, parameter PIXEL_WIDTH = 8)
	(
	input logic	[PIXEL_WIDTH-1:0]	pix_in_1
	input logic	[PIXEL_WIDTH-1:0]	pix_in_2
	input logic	[PIXEL_WIDTH-1:0]	pix_in_3
	input logic	[PIXEL_WIDTH-1:0]	pix_in_4 
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

integer req;
integer next_req;

// == Main Code ==================================
always_ff @(posedge clk)
begin 
	pix_out <= pix_in_1;
	send_z_buffer <= 0;

	if (rdy_z_buffer) begin
		req <= next_req;
		case (req)
      0: begin
				req_1 <= 0;
				req_2 <= 0;
				req_3 <= 0;
				req_4 <= 0;
			end
			1: begin
				req_1 <= 1;
				req_2 <= 0;
				req_3 <= 0;
				req_4 <= 0;
			end
			2: begin
				req_1 <= 0;
				req_2 <= 1;
				req_3 <= 0;
				req_4 <= 0;
			end
			3: begin
				req_1 <= 0;
				req_2 <= 0;
				req_3 <= 1;
				req_4 <= 0;
			end
			4: begin
				req_1 <= 0;
				req_2 <= 0;
				req_3 <= 0;
				req_4 <= 1;
			end
		endcase
		if (ack_1) begin
			pix_out <= pix_in_1;
			send_z_buffer <= 1;
			req_1 <= 0;
		end
		else if (ack_2) begin
			pix_out <= pix_in_2;
			send_z_buffer <= 1;
			req_2 <= 0;
		end
		else if (ack_3) begin
			pix_out <= pix_in_3;
			send_z_buffer <= 1;
			req_3 <= 0;
		end
		else if (ack_4) begin
			pix_out <= pix_in_4;
			send_z_buffer <= 1;
			req_4 <= 0;
		end
	end
	else begin
			req_1 <= 0;
			req_2 <= 0;
			req_3 <= 0;
			req_4 <= 0;
	end
end

always_comb
begin
  if (fill_1 == 0 && fill_2 == 0 && fill_3 == 0 && fill_4 == 0) begin
    next_req = 0;
  end
	else if (fill_1 >= fill_2 && fill_1 >= fill_3 && fill_1 >= fill_4) begin
		next_req = 1;
	end
	else if (fill_2 > fill_1 && fill_2 >= fill_3 && fill_2 >= fill_4) begin
		next_req = 2;
	end	 
	else if (fill_3 > fill_1 && fill_3 > fill_2 && fill_3 >= fill_4) begin
		next_req = 3;
	end
	else begin
		next_req = 4;
	end
end
endmodule