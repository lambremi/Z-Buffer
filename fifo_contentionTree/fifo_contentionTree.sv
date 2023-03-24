//Module fifo and contention tree merged
module fifo_contention_tree #(parameter MEM_LENGTH = 8, PIXEL_WIDTH = 16) (
// == Inputs =============================================================================  
  input logic clk, reset;
  input logic [PIXEL_WIDTH-1:0] pix_in_1, pix_in_2, pix_in_3, pix_in_4;
  input logic rdy_z_buffer;
  input logic load_1, load_2, load_3, load_4;

// == Outputs ============================================================================
  output logic [PIXEL_WIDTH-1:0] pix_out;
  output logic [MEM_LENGTH-1:0] fill_1, fill_2, fill_3, fill_4;
  output logic req_1, req_2, req_3, req_4;
  output logic send_z_buffer;
);

// == Internal signals ===========================================================================
  logic [PIXEL_WIDTH-1:0] pix_out_1, pix_out_2, pix_out_3, pix_out_4;
  logic ack_1, ack_2, ack_3, ack_4;

// == Modules ============================================================================
  fifo #(MEM_LENGTH, PIXEL_WIDTH) fifo_1 (
    .clk(clk),
    .reset(reset),
    .pix_in(pix_in_1),
    .req_out(req_1), 
    .load(load_1),

    .pix_out(pix_out_1), 
    .fill(fill_1),
    .ack_out(ack_1)
  );

  fifo #(MEM_LENGTH, PIXEL_WIDTH) fifo_2 (
    .clk(clk),
    .reset(reset),
    .pix_in(pix_in_2),
    .req_out(req_2), 
    .load(load_2),

    .pix_out(pix_out_2), 
    .fill(fill_2),
    .ack_out(ack_2)
  );

  fifo #(MEM_LENGTH, PIXEL_WIDTH) fifo_3 (
    .clk(clk),
    .reset(reset),
    .pix_in(pix_in_3),
    .req_out(req_3), 
    .load(load_3),

    .pix_out(pix_out_3), 
    .fill(fill_3),
    .ack_out(ack_3)
  );

  fifo #(MEM_LENGTH, PIXEL_WIDTH) fifo_4 (
    .clk(clk),
    .reset(reset),
    .pix_in(pix_in_4),
    .req_out(req_4), 
    .load(load_4),

    .pix_out(pix_out_4), 
    .fill(fill_4),
    .ack_out(ack_4)
  );

  contention_tree #(MEM_LENGTH, PIXEL_WIDTH) contention_tree1 (
    // == Inputs =============================================================================
    .pix_in_1(pix_out_1),
    .pix_in_2(pix_out_2),
    .pix_in_3(pix_out_3),
    .pix_in_4(pix_out_4),
    .clk(clk),
    .fill_1(fill_1),
    .fill_2(fill_2),
    .fill_3(fill_3),
    .fill_4(fill_4),
    .rdy_z_buffer(rdy_z_buffer),
    .ack_1(ack_1),
    .ack_2(ack_2),
    .ack_3(ack_3),
    .ack_4(ack_4),

    // == Outputs ============================================================================
    .req_1(req_1),
    .req_2(req_2),
    .req_3(req_3),
    .req_4(req_4),
    .send_z_buffer(send_z_buffer)
    .pix_out(pix_out)
  );
endmodule
