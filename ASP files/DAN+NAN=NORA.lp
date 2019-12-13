#const base=10.
letter(d;a;n;o;r).
values(0..base-1).

1 { x(L,Val) : values(Val) } 1 :- letter(L).

{ x(L,Val) : letter(L) } 1 :- values(Val).

smm :- 
   values(D;A;N;O;R),
 x(d,D), x(a,A), x(n,N), x(o,O), x(r,R),
   D > 0, 
   N > 0,
 D*base**2+A*base**1+N + N*base**2+A*base**1+N == N*base**3+O*base**2+R*base**1+A.

:- not smm.

#show x/2.
