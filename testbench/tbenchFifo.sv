//==============================================================================
//  Filename    : Testbench of fifo module                                              
//  Designer    : --
//  Description : --
//==============================================================================
module tbenchFifo();

timeunit 1ns;
timeprecision 1ns;

`define MEM_LENGTH 8
`define PIX_WIDTH 16

bit clk;
bit reset;

// Stimulus
logic load;
logic req_out;
logic [`PIX_WIDTH-1:0] pix_in;

// Internal signals
logic [`MEM_LENGTH-1:0] cursor1, cursor1_en;
logic [`MEM_LENGTH-1:0] cursor2, cursor2_en;
logic fill, fill_en, fill_plus_minus;
logic [`MEM_LENGTH-1:0] address, RW, enable;

// Outputs
logic [`PIX_WIDTH-1:0] pix_out;
logic ack_out;



// == Modules ================================================================ 
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


//== Main Code ================================================================

// Monitor Results format
initial $timeformat ( -9, 1, " ns", 12 );

// Clock and Reset Definition
`define PERIOD 20

always
    #(`PERIOD/2) clk = ~clk;



initial begin
	reset = 1;
	load = 0;
	req_out = 0;
	pix_in = 0;
	@(negedge clk)
	reset = 0;
	
	@(negedge clk)
	req_out = 1;
	@(negedge clk)
	pix_in = 16'h50ff;
	load = 1;
	@(negedge clk)
	pix_in = 16'h308e;
	load = 1;
	@(negedge clk)
	pix_in = 16'h08f1;
	load = 1;
	req_out = 1;
	@(negedge clk)
	pix_in = 16'h2575;
	load = 0;
	req_out = 1;
	@(negedge clk)
	req_out = 0;
	@(negedge clk)
	load = 1;
	req_out = 1;
	@(negedge clk)
	pix_in = 16'hafe1;
	load = 0;
                                                          
	end

endmodule
