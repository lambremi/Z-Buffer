// Module to control a fifo memory
module fifoController #(parameter MEM_LENGTH = 8)(
    input logic clk,
    input logic reset,  // Syncronous Active high reset (More Robust mapping on FPGA)

	// Inputs
    input logic load,
    input logic req_out,
    input logic [MEM_LENGTH-1:0] cursor1,
    input logic [MEM_LENGTH-1:0] cursor2,
	input logic [MEM_LENGTH-1:0] fill,

    // Outputs
    output logic cursor1_en,

    output logic cursor2_en,

    output logic fill_en,
    output logic fill_plus_minus,

    output logic [MEM_LENGTH-1:0] address,
    output logic RW,
    output logic enable
);


// == Variables Declaration ====================================================
typedef enum logic [3:0] {
	INIT,
    IDLE,
    GOING_TO_POP,
    POP,
    LOAD,
    WRITE_MEM,
	WRITE_THEN_POP
} fsm_state_t;

fsm_state_t current_state;
fsm_state_t next_state;


// == Main Code ================================================================
always @(posedge clk) begin
    if (reset) begin
        current_state = INIT;
    end
	
	else current_state = next_state;
end

always_comb begin
    case (current_state)
		INIT: begin
			next_state = IDLE;
			cursor1_en = 0;
        	cursor2_en = 0;
        	fill_en = 0;
        	fill_plus_minus = 0;
        	address = cursor1;
        	RW = 0;
        	enable = 0;
		end

        IDLE: begin
            if (req_out && (fill > 0)) next_state = GOING_TO_POP;
            else if (load && (fill < (1 << MEM_LENGTH) - 1)) next_state = LOAD;
            else next_state = IDLE;
            enable = 0;
        end

        GOING_TO_POP: begin
            next_state = POP;
            enable = 0;
            cursor1_en = 1;
            fill_plus_minus = 1;
            fill_en = 1;
        end

        POP: begin
            if (req_out && (fill > 0)) next_state = GOING_TO_POP;
            else if (load && (fill < (1 << MEM_LENGTH) - 1)) next_state = LOAD;
            else next_state = IDLE;
            cursor1_en = 0;
            fill_en = 0;
            RW = 0;
            address = cursor1;
            enable = 1;
        end

		LOAD: begin
			if (req_out && (fill > 0)) next_state = WRITE_THEN_POP;
            else next_state = WRITE_MEM;
            enable = 0;
            cursor2_en = 1;
            fill_plus_minus = 0;
            fill_en = 1;
        end

        WRITE_MEM: begin
            if (req_out && (fill > 0)) next_state = GOING_TO_POP;
            else if (load && (fill < (1 << MEM_LENGTH) - 1)) next_state = LOAD;
            else next_state = IDLE;
            cursor2_en = 0;
            fill_en = 0;
            RW = 1;
            address = cursor2;
            enable = 1;
        end

		WRITE_THEN_POP: begin
			next_state = POP;
			cursor2_en = 0;
			fill_en = 0;
			RW = 1;
            address = cursor2;
            enable = 1;
		end

		default: begin
			next_state = INIT;
		end

    endcase
end


endmodule
