#____________________________
#CUTTING STOCK USING PATTERNS
#____________________________

param roll_width >0;

set WIDTHS;
param orders {WIDTHS} >0;

param nPAT integer >=0;
set PATTERNS := 1..nPAT;

param nbr {WIDTHS, PATTERNS} integer >=0;
	
	check {j in PATTERNS}:
		sum {i in WIDTHS} i*nbr[i,j] <=roll_width; var Cut {PATTERNS} integer>=0;

minimize Number:
	sum {j in PATTERNS} Cut[j];

subj to Fill {i in WIDTHS}:
	sum {j in PATTERNS} nbr[i,j] * Cut [j] >=orders[i];

#______________________________________
#KNACKSACK SUBPROLEM FOR CUTTING STOCK
#______________________________________

param price {WIDTHS} default 0.0;

var Use {WIDTHS} integer >=0;

minimize Reduced_Cost:
	1 - sum {i in WIDTHS} price[i] * Use[i];

subj to Width_Limit:
	sum {i in WIDTHS} i * Use[i] <= roll_width; #__________________________ #GILMORE-GOMORY METHOD FOR #CUTTING STOCK PROBLEM #__________________________ #option solver cplex; option solver osl; option solution_round 6; option display_1col 1000; model cut.mod; data cut.dat; problem Cutting_Opt: Cut, Number, Fill; option relax_integrality 1; problem Pattern_Gen: Use, Reduced_Cost, Width_Limit; option relax_integrality 0; let nPAT :="0;" for {i in WIDTHS} { let nPAT :="nPAT" +1; let nbr[i,nPAT] :="floor" (roll_width/i); let {i2 in WIDTHS: i2 <> i} nbr[i2,nPAT] :=0;
	};

repeat {
	solve Cutting_Opt;

	let {i in WIDTHS} price[i] := Fill[i].dual;

	solve Pattern_Gen;

	if Reduced_Cost <-0.00001 then { let nPAT :="nPAT" +1; let {i in WIDTHS} nbr[i,nPAT] :="Use[i];" } else break; }; option display_width 100; display nbr>nbr.results;
display Cut >cut_decimal.results;

option Cutting_Opt.relax_integrality 0;
solve Cutting_Opt;

display Cut >cut.results;