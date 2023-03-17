//==============================================================================
//  Filename    : Testbench of Filter                                              
//  Designer    : --
//  Description : Bench of filter with some stimuli
//                 1 - Dirac   : Enable to see coeff on output (!! divider)
//                 2 - Echelon : Enable to see saturation of filter (output must be close to 255 (5V) at DAC output
//                 3 - Sinus   : Measure Cut-off Frequency 
//==============================================================================
module tbench ();

timeunit      1ns;
timeprecision 1ns;

`define NUMBITS 8

bit clk;
bit reset;        
logic en, invert, load;
logic [`NUMBITS-1:0] data;
logic [`NUMBITS-1:0] count;



counter #(.BITS(`NUMBITS)) counter1 (  
	.clk							(clk),         
  .reset						(reset),       

  // Input counter
	.enable						(en),
  .inverseCounter		(invert), 
  .load							(load), 
  .data							(data), 

	// Output counter
	.count						(count) 
  
);

// Monitor Results format
initial $timeformat ( -9, 1, " ns", 12 );

// Clock and Reset Definition
`define PERIOD 20

always
    #(`PERIOD/2) clk = ~clk;



initial begin
		invert = 0;
		load = 0;
		data = 0;
		en = 1;
		reset = 1; 

		@(negedge clk)
		reset = 0;

		@(negedge clk)
		@(negedge clk)
		@(negedge clk)

		load = 1;
		data = 55;

		@(negedge clk)
		load = 0;
		@(negedge clk)
		@(negedge clk)
		@(negedge clk)
		@(negedge clk)
		invert = 1;
		@(negedge clk)
		@(negedge clk)
		@(negedge clk)
		@(negedge clk)
		data=1;
		load=1;
		@(negedge clk)
		@(negedge clk)
		@(negedge clk)
		invert=0
		@(negedge clk)
		@(negedge clk)
		@(negedge clk)
		en = 0;       
		reset=0;                                                    
	end

endmodule


















