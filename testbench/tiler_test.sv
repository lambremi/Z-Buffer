//==============================================================================
//  Filename    : Testbench of Tiler                                             
//  Designer    : Hugo Rivier
//  Description : Bench of Tiler 
//                 verification du point de sortie ( si il est dans le triangle)
//			 verification de son intensité lumineuse en fonction de l'entrée
//			 comparer avec la sortie en python
//==============================================================================

integer N=9;
module tiler_bench ();
timeunit      1ns;
timeprecision 1ns;

bit clk;
bit reset;        
integer i,j;
logic [N-1:0] lecture;
logic [3:0][N-1:0] A,B,C,pixel;
logic load, fin_calcul;
integer file,file_lecture;
logic pixel_out;

reg [N-1:0] data [0:dimension][0:dimension];

//affectation à faire avec le bloc creer par guillaume


// Monitor Results format
initial $timeformat ( -9, 1, " ns", 12 );


// Clock and Reset Definition
`define PERIOD 20

always
    #(`PERIOD/2) clk = ~clk;

// initial begin
//   i=0;
//   j=0;
//   file_lecture=$fopen("nom_triangle","r");
//   if (file_lecture == `NULL) begin
//     $display("file_lecture handle was NULL");
//     $finish;
//   end
//   while (!$feof(file_lecture)) begin
//       $fscanf(file_lecture, "%d", lecture);
// 	j=j+1;
// 	$display("Data read from file: %d", data);
// 	if(i==0) 
//         begin
// 		A[j]=lecture;
// 		end
// 	if(i==1) 
//         begin
// 		B[j]=lecture;
// 		end
// 	if(i==2) 
//         begin
// 		C[j]=lecture;
// 		end
// 	if (j==3) 
//         begin
// 		i=i+1;
// 		j=0;
// 		end
//     end
// 	$fclose(file_lecture);
// end

initial
  begin
  
	file=$fopen("resultat.out");
	reset=1;
	load=0;
	#500;
	reset=0;
	i=0;
  	j=0;
  	file_lecture=$fopen("nom_triangle","r");
 	 if (file_lecture == `NULL) begin
    	$display("file_lecture handle was NULL");
    		$finish;
 	 end
 	 while (!$feof(file_lecture)) begin
      	$fscanf(file_lecture, "%d", lecture);
		j=j+1;
		$display("Data read from file: %d", data);
		if(i==0) begin
			A[j]=lecture;
			end
		if(i==1) begin
			B[j]=lecture;
			end
		if(i==2) begin
			C[j]=lecture;
			end
		if (j==3) begin
			i=i+1;
			j=0;
			end
    	end
	$fclose(file_lecture);
	#5000
	load=1;
	//initialise la matrice de base
	for(i=0; i<dimension;i=i+1)
		begin
			for(j=0;j<2*dimension;j=j+1)
				begin
				data[i][j]=0;	
				end
		end
    @(posedge fin_lecture)
    for(i=0; i<dimension;i=i+1)
		begin
			for(j=0;j<2*dimension;j=j+1)
				begin
				fdisplay(file,data[i][j]);	
				end
		end
	$fclose(file);

  end

always @(posedge clk)
begin
    if (pixel_out==1 && fin_calcul==0)
    begin
        data[pixel[0]][2*pixel[1]]=pixel[2];
        data[pixel[0]][2*pixel[1]+1]=pixel[3];//rajouter le luminecense à coté 
    end
end
    
	

	
//stocker dans une matrice et quand elle est fini on fait l'ecriture
//arrete quand fin calcul =0
//	fdisplay(file,"ce que je veux ecrire")
	
	

//comparer directement avec les resultats du fichier python


