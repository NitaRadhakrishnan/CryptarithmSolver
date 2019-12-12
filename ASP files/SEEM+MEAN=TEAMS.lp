
#const base=10.

letter(s;e;m;a;n;t).
values(0..base-1).

1 { x(L,Val) : values(Val) } 1 :- letter(L).

{ x(L,Val) : letter(L) } 1 :- values(Val).

smm :- 
   values(S;E;M;A;N;T),
  x(s,S), x(e,E), x(m,M), x(a,A), x(n,N), x(t,T),
   S > 0, 
   T > 0,
   M > 0,
  S*base**3 +E*base**2+E*base**1+M + M*base**3+E*base**2+A*base**1+N == T*base**4+E*base**3+A*base**2+M*base**1+S.


:- not smm.

#show x/2.
