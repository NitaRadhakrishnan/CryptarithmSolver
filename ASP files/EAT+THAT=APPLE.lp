#const base=10.
letter(e;a;t;h;p;l).
values(0..base-1).

1 { x(L,Val) : values(Val) } 1 :- letter(L).

{ x(L,Val) : letter(L) } 1 :- values(Val).

smm :- 
   values(E;A;T;H;P;L),
   x(e,E), x(a,A), x(t,T), x(h,H),
   x(p,P), x(l,L),
   E > 0, 
   A > 0,
   T > 0,
   E*base**2+A*base**1+T + T*base**3+H*base**2+A*base**1+T == A*base**4+P*base**3+P*base**2+L*base**1+E.

:- not smm.

#show x/2.
