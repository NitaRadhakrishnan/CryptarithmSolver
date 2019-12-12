%
% CRACK+HACK=ERROR in any base in ASP.
%
% Change base by
%   clingo -c base=11 CRACK+HACK=ERROR.lp
% 

#const base=10.

letter(c;r;a;k;h;e;o).
values(0..base-1).

% exact 1 occurrence of each letter
1 { x(L,Val) : values(Val) } 1 :- letter(L).

% 0..1 occurrences of each value
{ x(L,Val) : letter(L) } 1 :- values(Val).

% no digit can be given to two different symbols
% :- letter(L), letter(L1), x(L,V1), x(L1,V1), L != L1.

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
