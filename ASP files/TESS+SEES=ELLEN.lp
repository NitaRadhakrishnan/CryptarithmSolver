%
% TESS+SEEN=ELLEN in any base in ASP.
%
% Change base by
%   clingo -c base=11 TESS+SEEN=ELLEN.lp
% 

#const base=10.

letter(t;e;s;l;n).
values(0..base-1).

% exact 1 occurrence of each letter
1 { x(L,Val) : values(Val) } 1 :- letter(L).

% 0..1 occurrences of each value
{ x(L,Val) : letter(L) } 1 :- values(Val).

% no digit can be given to two different symbols
% :- letter(L), letter(L1), x(L,V1), x(L1,V1), L != L1.

smm :- 
   values(T;E;S;L;N),
   x(t,T), x(e,E), x(s,S),
   x(l,L), x(n,N), 
   E > 0, 
   T > 0,

T*base**3 +E*base**2+S*base**1+S + S*base**3+E*base**2+E*base**1+S == E*base**4+L*base**3+L*base**2+E*base**1+N.


   

:- not smm.

#show x/2.
