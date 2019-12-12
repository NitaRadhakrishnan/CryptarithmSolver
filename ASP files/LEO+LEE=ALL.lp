%
% LEO+LEE=ALL in any base in ASP.
%
% Change base by
%   clingo -c base=11 LEO+LEE=ALL.lp
% 

#const base=10.

letter(l;e;o;a).
values(0..base-1).

% exact 1 occurrence of each letter
1 { x(L,Val) : values(Val) } 1 :- letter(L).

% 0..1 occurrences of each value
{ x(L,Val) : letter(L) } 1 :- values(Val).

% no digit can be given to two different symbols
% :- letter(L), letter(L1), x(L,V1), x(L1,V1), L != L1.

smm :- 
   values(L;E;O;A),
 x(l,L), x(e,E), x(o,O), x(a,A),
   L > 0, 
   O > 0,
   A > 0,
 L*base**2+E*base**1+O +L*base**2+E*base**1+E == A*base**2+L*base**1+L.

:- not smm.

#show x/2.
