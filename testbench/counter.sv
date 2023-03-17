// module counter
module counter #(parameter BITS = 8)
(

  input  logic       clk,               // Main Clock
  input  logic       reset,             // Synchronous Active High Reset (More Robust mapping on FPGA)

  // Input
  input  logic enable,
  input  logic inverseCounter, 
  input  logic load, 
  input  logic [BITS-1:0] data, 

	//Output
	output  logic [BITS-1:0] count 

);

// == Variables Declaration ====================================================


// == Main Code ================================================================


always_ff@(posedge clk) begin
	if(reset)begin
		count = 0;
	end
	else if(load)begin
		count = data;
	end	
	else if(enable)begin
		if (inverseCounter) begin
			count = count -1;
		end
		else begin
			count = count + 1;
		end
	end
		
end
	

endmodule
