//fifo module merging fifo controller, memory block and counter
module fifo #(parameter MEM_LENGTH = 8, PIX_WIDTH = 16) (
  // == Inputs ===============================================
  input logic clk, reset;
  input logic [PIX_WIDTH-1:0] pix_in;
  input logic req_out;
  input logic load;

  // == Internal signals =====================================
  logic [`MEM_LENGTH-1:0] cursor1, cursor1_en;
  logic [`MEM_LENGTH-1:0] cursor2, cursor2_en;
  logic fill, fill_en, fill_plus_minus;
  logic [`MEM_LENGTH-1:0] address, RW, enable;

  // == Outputs ==============================================
  output logic [PIX_WIDTH-1:0] pix_out;
  output logic [MEM_LENGTH-1:0] fill;
  output logic ack_out;
);

// == Modules ====================================
  counter #(.BITS(`MEM_LENGTH)) counter1(  
    .clk(clk),         
    .reset(reset),       

    // Input counter
    .enable(cursor1_en),
    .inverseCounter(1'b0), 
    .load(1'b0), 
    .data(`MEM_LENGTH'b0), 

    // Output counter
    .count(cursor1)  
  );


  counter #(.BITS(`MEM_LENGTH)) counter2(  
    .clk(clk),         
    .reset(reset),       

    // Inputs
    .enable(cursor2_en),
    .inverseCounter(1'b0), 
    .load(1'b0), 
    .data(`MEM_LENGTH'b0), 

    // Outputs
    .count(cursor2)  
  );


  counter #(.BITS(`MEM_LENGTH)) fillCounter(  
    .clk(clk),         
    .reset(reset),       

    // Inputs
    .enable(fill),
    .inverseCounter(fill_plus_minus), 
    .load(1'b0), 
    .data(`MEM_LENGTH'b0), 

    // Outputs
    .count(fill)  
  );


  fifoController #(.MEM_LENGTH(`MEM_LENGTH)) controller(
    .clk(clk),
    .reset(reset),
    
    // Inputs
    .load(load),
    .req_out(req_out),
    .cursor1(cursor1),
    .cursor2(cursor2),

    .cursor1_en(cursor1_en),

    .cursor2_en(cursor2_en),

    .fill_en(fill_en),
    .fill_plus_minus(fill_plus_minus),

    .address(address),
    .RW(RW),
    .enable(enable)
  );


  memoryBlock #(.MEM_LENGTH(`MEM_LENGTH), .PIX_WIDTH(`PIX_WIDTH)) memory(
    .clk(clk),
    .reset(reset),

    // Inputs
    .pix_in(pix_in),
    .RW(RW),
    .address(address),
    .enable(enable),

    // Outputs
    .pix_out(pix_out),
    .ack_out(ack_out)
  );
endmodule