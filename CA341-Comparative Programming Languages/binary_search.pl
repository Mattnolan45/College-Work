node(_,_,_).


insert(empty, X, node(X,empty,empty)).
insert(T,X,T) :- T = node(X,_,_).
insert(node(V,L,R),X,node(V,Ln,R)) :- X < V, insert(L,X,Ln).
insert(node(V,L,R),X,node(V,L,Rn)) :- X > V, insert(R,X,Rn).


check(node(X, _, _), X).
check(node(K, L, _), X) :- X < K, check(L, X).
check(node(K, _, R), X) :- X > K, check(R, X).

inorder(node(_,L,_),X):- inorder(L,X).
inorder(node(X,_,_),X).
inorder(node(_,_,R),X):- inorder(R,X).


preorder(node(X,_,_),X).
preorder(node(_,L,_),X):- preorder(L,X).
preorder(node(_,_,R),X):- preorder(R,X).


postorder(node(_,L,_),X):- postorder(L,X).
postorder(node(_,_,R),X):- postorder(R,X).
postorder(node(X,_,_),X).
