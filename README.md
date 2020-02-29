# ModifiedFibonacciSequenceFind the number that is placed in the 26th location of the Fibonacci sequence.  

However for this modified Fibonacci sequence, when result of one of the numbers within the sequence is greater than 26, divide that number by 26 and replace the number that was greater than 26 in the sequence with the remainder.  For example, in the original Fibonacci sequence when you reach the 10th sequence location it is “34”, so you would divide 34 by 26, with the remainder being “8” thus changing the result in the Fibonacci sequence to “8” and iterating until you reach the 26th sequence location. 

For example the original Fibonacci sequence is: 
Sequence Location	1	2	3	4	5	6	7	8	9	10	11	… …	26
Fibonacci sequence	0	1	1	2	3	5	8	13	21	34	55	… …	75025

For the Coding Problem find the modified Fibonacci sequence as per the outlined description above…

Sequence Location	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	 …  ...   ...  26
Fibonacci sequence	0	1	1	2	3	5	8	13	21	34	55	89	 	 	 	 	 		
 	 	 	 	 	 	 	 	 	 	                          = 34/26, resulting in a remainder of 8
                                                                                                        "8" now replaces "34" in the 10th sequence 
                                                                                                         location
		
Sequence Location	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	 …  ...   ...  26
Modified Fibonacci sequence	 	 	 	 	               21	 8	29	 	 	 	 	 	 		
							                                                      = 29/26, resulting in a remainder of 3
                                                                                                           "3" now replaces "29" in the 11th sequence 
                                                                                                            location

Sequence Location	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	 …  ...   ...  26	
Revised Fibonacci sequence	 	 	 	 	 	                 8	 3	11	14	25	39	 …	 …	…	
                                                                                                                                          =39/26, resulting in ....

Result....
Sequence Location	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	…  ...   ...  26
Modified Fibonacci 	0	1	1	2	3	5	8	13	21	  8     3    11   14    25   ...     ...    ...   ...  ...   ...   n
 

Implement this function/method and submit a link to your code (answer) below.
You can share via a link to your code using free websites like https://gist.github.com/ or http://ideone.com.




Resources I used:
http://mathworld.wolfram.com/FibonacciNumber.html