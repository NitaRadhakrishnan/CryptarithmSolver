%
% FOOD+FAD=DIETS in any base in ASP.
%
% Change base by
%   clingo -c base=11 FOOD+FAD=DIETS.lp
% 

#const base=10.

letter(f;o;d;a;i;e;t;s).
values(0..base-1).

% exact 1 occurrence of each letter
1 { x(L,Val) : values(Val) } 1 :- letter(L).

% 0..1 occurrences of each value
{ x(L,Val) : letter(L) } 1 :- values(Val).

% no digit can be given to two different symbols
% :- letter(L), letter(L1), x(L,V1), x(L1,V1), L != L1.

smm :- 
   values(F;O;D;A;I;E;T;S),
   x(f,F), x(o,O), x(d,D), x(a,A),
   x(i,I), x(e,E), x(t,T), x(s,S), 
   F > 0, 
   D > 0,
   F*base**3 +O*base**2+O*base**1+D + F*base**2+A*base**1+D == D*base**4+I*base**3+E*base**2+T*base**1+S.

:- not smm.

#show x/2.
