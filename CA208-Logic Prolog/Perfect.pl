



perfectNumber(Number) :- perfectNumber(Number,2,1),!.

perfectNumber(Number,Number, Sum):-Number = Sum.
perfectNumber(Number,CurrDivisor,CurrSum) :-  not(CurrDivisor = Number), NewDivisor is CurrDivisor+1, 0 is mod(Number,CurrDivisor),  NewSum is CurrSum+CurrDivisor, perfectNumber(Number,NewDivisor,NewSum).

perfectNumber(Number,CurrDivisor,CurrSum) :- not(CurrDivisor = Number),NewDivisor is CurrDivisor+1,perfectNumber(Number,NewDivisor,CurrSum).

