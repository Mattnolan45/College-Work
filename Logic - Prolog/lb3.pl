
myElm(X,[X | _]). 
myElm(X,[ _ | T]):- myElm(X,T).

myHead(X, [X | _]).

myLast(X, [X]).
myLast(X, [ _ | T]) :- myLast(X,T).

myTail(A,[_|A].

myAppend([],L,L).
myAppend([H|T],L,[H|L3]) :- myAppend(T,L,l3).

myReverse([ ],[ ]).
myReverse([X|T], Y):- myReverse(T,T1), myAppend(T1,[X],Y).

myDelete(X,[X | T],T).
myDelete(X,[Y | T],[Y | L ]):- myDelete(X,T,L).