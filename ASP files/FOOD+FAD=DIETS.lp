
#const base=10.

letter(f;o;d;a;i;e;t;s).
values(0..base-1).

1 { x(L,Val) : values(Val) } 1 :- letter(L).

{ x(L,Val) : letter(L) } 1 :- values(Val).

smm :- 
   values(F;O;D;A;I;E;T;S),
   x(f,F), x(o,O), x(d,D), x(a,A),
   x(i,I), x(e,E), x(t,T), x(s,S), 
   F > 0, 
   D > 0,
   F*base**3 +O*base**2+O*base**1+D + F*base**2+A*base**1+D == D*base**4+I*base**3+E*base**2+T*base**1+S.

:- not smm.

#show x/2.
