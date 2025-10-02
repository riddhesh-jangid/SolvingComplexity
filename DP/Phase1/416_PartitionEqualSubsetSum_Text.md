Tabulation vs Top-Down
1. Base case
	Generally in top-down the base case is something which either generate the result or atleast start the domino effect.
	
	In tabulation, we filled the zero sum as TRUE which covers base condition SUM == EQUAL returning TRUE. we filled whole remaining table as FALSE 
	which covers SUM > EQUAL (sum - element) returning false in certain cases.
	
2. Making the recursion (making the choice)
	In top-down it's choices like include or exclude
	
	In tabulation, it's same again as we are taking 'or' operation between as in either take previous (exclude) or previous + element (include)

How we are building results from previous result?
1. If the element is greater than the sum itself -> take just above result
2. If the element is lesser than the sum itself -> there would be a or operation between
	2.1 the just above result 
	2.2 sum - element result 
