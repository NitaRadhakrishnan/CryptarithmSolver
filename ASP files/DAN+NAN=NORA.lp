#const base=10.

letter(d;i;s;l).
values(0..base-1).
1 { x(L,Val) : values(Val) } 1 :- letter(L).

{ x(L,Val) : letter(L) } 1 :- values(Val).

smm :- 
   values(D;I;S;L),
 x(d,D), x(i,I), x(s,S), x(l,L),
   D > 0, 
   I > 0,
 D*base**1+I + I*base**1+S == I*base**2+L*base**1+L.

:- not smm.

#show x/2.
