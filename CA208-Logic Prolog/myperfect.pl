





perfect(N):- N>0,perfect(N,2,1),!.

perfect(N,N,Sum):- N = Sum. 

perfect(N,D,Sum):-Result = sqrt(N), not(D = Result),0 is mod(N,D), newsum(N,D,Sum).

newsum(N,D,Sum) :- Nsum is Sum+D,D1 is D+1,perfect(N,D1,Nsum).

perfect(N,D,Sum):- Result = sqrt(N), not(D=Result), D1 is D+1,perfect(N,D1,Sum).