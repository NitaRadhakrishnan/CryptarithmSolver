#const base=10.
letter(l;e;o;a).
values(0..base-1).

1 { x(L,Val) : values(Val) } 1 :- letter(L).

{ x(L,Val) : letter(L) } 1 :- values(Val).

smm :- 
   values(L;E;O;A),
 x(l,L), x(e,E), x(o,O), x(a,A),
   L > 0, 
   O > 0,
   A > 0,
 L*base**2+E*base**1+O +L*base**2+E*base**1+E == A*base**2+L*base**1+L.

:- not smm.

#show x/2.
