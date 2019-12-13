#const base=10.

letter(a;t;e;s;w;o;u;h).
values(0..base-1).

1 { x(L,Val) : values(Val) } 1 :- letter(L).

{ x(L,Val) : letter(L) } 1 :- values(Val).

smm :- 
   values(A;T;E;S;W;O;U;H),
  x(a,A), x(t,T), x(e,E), x(s,S), x(w,W), x(o,O), x(u,U), x(h,H),
   A > 0, 
   E > 0,
   W > 0,
   S > 0,
  A*base**1+T + E*base**3+A*base**2+S*base**1+T + W*base**3+E*base**2+S*base**1+T == S*base**4+O*base**3+U*base**2+T*base**1+H.

:- not smm.

#show x/2.
