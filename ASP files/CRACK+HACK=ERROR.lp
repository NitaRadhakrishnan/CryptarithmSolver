#const base=10.
letter(c;r;a;k;h;e;o).
values(0..base-1).
1 { x(L,Val) : values(Val) } 1 :- letter(L).
{ x(L,Val) : letter(L) } 1 :- values(Val).

smm :- 
   values(C;R;A;K;H;E;O),
   x(c,C), x(r,R), x(a,A),
   x(k,K), x(h,H), x(e,E), x(o,O),
   C > 0, 
   H > 0,
   E > 0,
C*base**4+R*base**3 +A*base**2+C*base**1+K + H*base**3+A*base**2+C*base**1+K == E*base**4+R*base**3+R*base**2+O*base**1+R.

:- not smm.

#show x/2.
