


perfect(N):- perfect(N,2,1),!.

perfect(N,N,Sum):- N = Sum.

perfect(N,D,Sum):- not(D = N),0 is mod(N,D), newsum(N,D,Sum).

newsum(N,D,Sum) :- Nsum is Sum+D,perfect(N,D,NSum).

perfect(N,D,Sum):-newdivisor(N,D,Sum).	

newdivisor(N,D,Sum):- D1 is D+1,perfect(N,D1,Sum).
