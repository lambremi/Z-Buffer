//==============================================================================
//  Filename    : Testbench of contention tree                                             
//  Designer    : --
//  Description : test de l'arbre de contention
//==============================================================================
module tbench ();

  timeunit      1ns;
  timeprecision 1ns;

  `define LENGTH 8
  `define PIXEL_WIDTH 8

  bit clk;
  logic [PIXEL_WIDTH-1:0] pix_in_1, pix_in_2, pix_in_3, pix_in_4, pix_out;
  logic [LENGTH-1:0] fill_1, fill_2, fill_3, fill_4;
  logic rdy_z_buffer, send_z_buffer, ack_1, ack_2, ack_3, ack_4, req_1, req_2, req_3, req_4;

  contention_tree #(.LENGTH(`LENGTH), .PIXEL_WIDTH(`PIXEL_WIDTH)) contention_tree1 (
    .clk(clk),
    .pix_in_1(pix_in_1),
    .pix_in_2(pix_in_2),
    .pix_in_3(pix_in_3),
    .pix_in_4(pix_in_4),
    .pix_out(pix_out),
    .fill_1(fill_1),
    .fill_2(fill_2),
    .fill_3(fill_3),
    .fill_4(fill_4),
    .rdy_z_buffer(rdy_z_buffer),
    .send_z_buffer(send_z_buffer),
    .ack_1(ack_1),
    .ack_2(ack_2),
    .ack_3(ack_3),
    .ack_4(ack_4),
    .req_1(req_1),
    .req_2(req_2),
    .req_3(req_3),
    .req_4(req_4)
  );

  // Monitor results format
  initial $timeformat(-9, 1, "ns", 12);

  // Clock generation
  `define PERIOD 20
  always #(`PERIOD/2) clk = ~clk;

  // Testbench
  initial begin
    pix_in_1 = 8'hE2;
    pix_in_2 = 8'hA5;
    pix_in_3 = 8'h78;
    pix_in_4 = 8'h4B;
    fill_1 = 8'h00;
    fill_2 = 8'h00;
    fill_3 = 8'h00;
    fill_4 = 8'h00;
    rdy_z_buffer = 1'b1;
    send_z_buffer = 1'b0;
    ack_1 = 1'b0;
    ack_2 = 1'b0;
    ack_3 = 1'b0;
    ack_4 = 1'b0;
    req_1 = 1'b0;
    req_2 = 1'b0;
    req_3 = 1'b0;
    req_4 = 1'b0;

  #(`PERIOD*20)
    fill_1 = 8'h01;
    fill_2 = 8'h00;
    fill_3 = 8'h00;
    fill_4 = 8'h00;

  #(`PERIOD*20)
    fill_1 = 8'h00;
    fill_2 = 8'h01;
    fill_3 = 8'h00;
    fill_4 = 8'h00;

  #(`PERIOD*20)
    fill_1 = 8'h00;
    fill_2 = 8'h00;
    fill_3 = 8'h01;
    fill_4 = 8'h00;

  #(`PERIOD*20)
    fill_1 = 8'h00;
    fill_2 = 8'h00;
    fill_3 = 8'h00;
    fill_4 = 8'h01;

  #(`PERIOD*20)
    fill_1 = 8'h01;
    fill_2 = 8'h01;
    fill_3 = 8'h01;
    fill_4 = 8'h01;

  #(`PERIOD*20)
    fill_1 = 8'h24;
    fill_2 = 8'hAF;
    fill_3 = 8'h7E;
    fill_4 = 8'h9D;
  
  #(`PERIOD*100)
    $finish;
  end
endmodule