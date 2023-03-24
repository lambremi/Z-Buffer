//Test des fifo et contention tree reliés
module tbenchFifoContentionTree();

  timeunit 1ns;
  timeprecision 1ns;

  `define MEM_LENGTH 8
  `define PIXEL_WIDTH 16

  // == Déclaration des signaux ====================
  // == Signaux d'entrée ==
  bit clk;
  bit reset;
  logic [PIXEL_WIDTH-1:0] pix_in_1,pix_in_2,pix_in_3,pix_in_4;
  logic rdy_z_buffer;
  logic load_1, load_2, load_3, load_4;

  // == Signaux de sortie ==
  logic [PIXEL_WIDTH-1:0] pix_out;
  logic [MEM_LENGTH-1:0] fill_1, fill_2, fill_3, fill_4;
  logic req_1, req_2, req_3, req_4;
  logic send_z_buffer;

  // == Déclaration des modules ====================
  fifo_contention_tree #(.MEM_LENGTH(`MEM_LENGTH), .PIXEL_WIDTH(`PIXEL_WIDTH)) fifo_contention_tree_inst(
    // == Entrées ==
    .clk(clk),
    .reset(reset),
    .pix_in_1(pix_in_1),
    .pix_in_2(pix_in_2),
    .pix_in_3(pix_in_3),
    .pix_in_4(pix_in_4),
    .rdy_z_buffer(rdy_z_buffer),
    .load_1(load_1),
    .load_2(load_2),
    .load_3(load_3),
    .load_4(load_4),

    // == Sorties ==
    .pix_out(pix_out),
    .fill_1(fill_1),
    .fill_2(fill_2),
    .fill_3(fill_3),
    .fill_4(fill_4),
    .req_1(req_1),
    .req_2(req_2),
    .req_3(req_3),
    .req_4(req_4),
    .send_z_buffer(send_z_buffer)
  );

  // == Main code ====================
  // Monitor results format
  initial $timeformat(-9, 1,"ns", 12);

  // Clock and reset definition
  `define PERIOD 20
  always #(`PERIOD/2) clk = ~clk;

  initial begin
    reset = 1;
    load = 0;
    pix_in_1 = 0; pix_in_2 = 0; pix_in_3 = 0; pix_in_4 = 0;
    rdy_z_buffer = 0;
    @(negedge clk)
    reset = 0;

    @(negedge clk)
    pix_in_1 = 16'h0001; pix_in_2 = 16'h0002; pix_in_3 = 16'h0003; pix_in_4 = 16'h0004;
    load_1 = 1; load_2 = 1; load_3 = 1; load_4 = 1;
    @(negedge clk)
    load_1 = 0; load_2 = 0; load_3 = 0; load_4 = 0;
    @(negedge clk)
    pix_in_1 = 16'h0005; pix_in_2 = 16'h0006; pix_in_3 = 16'h0007; pix_in_4 = 16'h0008;
    load_1 = 1; load_2 = 1; load_3 = 1; load_4 = 1;
    @(negedge clk)
    load_1 = 0; load_2 = 0; load_3 = 0; load_4 = 0;
    @(negedge clk)
    pix_in_1 = 16'h0009; pix_in_2 = 16'h000A; pix_in_3 = 16'h000B; pix_in_4 = 16'h000C;
    load_1 = 1; load_2 = 1; load_3 = 1; load_4 = 1;
    @(negedge clk)
    load_1 = 0; load_2 = 0; load_3 = 0; load_4 = 0;
    #(1000*`PERIOD)
    $finish;
  end

endmodule