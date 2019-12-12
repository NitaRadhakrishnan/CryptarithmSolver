%
% DI+IS=ILL in any base in ASP.
%
% Change base by
%   clingo -c base=11 DI+IS=ILL.lp
% 

#const base=10.

letter(d;i;s;l).
values(0..base-1).

% exact 1 occurrence of each letter
1 { x(L,Val) : values(Val) } 1 :- letter(L).

% 0..1 occurrences of each value
{ x(L,Val) : letter(L) } 1 :- values(Val).

% no digit can be given to two different symbols
% :- letter(L), letter(L1), x(L,V1), x(L1,V1), L != L1.

smm :- 
   values(D;I;S;L),
 x(d,D), x(i,I), x(s,S), x(l,L),
   D > 0, 
   I > 0,
 D*base**1+I + I*base**1+S == I*base**2+L*base**1+L.

:- not smm.

#show x/2.
