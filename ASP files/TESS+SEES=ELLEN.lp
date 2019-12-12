
#const base=10.

letter(t;e;s;l;n).
values(0..base-1).

1 { x(L,Val) : values(Val) } 1 :- letter(L).

{ x(L,Val) : letter(L) } 1 :- values(Val).

smm :- 
   values(T;E;S;L;N),
   x(t,T), x(e,E), x(s,S),
   x(l,L), x(n,N), 
   E > 0, 
   T > 0,

T*base**3 +E*base**2+S*base**1+S + S*base**3+E*base**2+E*base**1+S == E*base**4+L*base**3+L*base**2+E*base**1+N.

:- not smm.

#show x/2.
