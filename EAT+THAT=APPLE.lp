%
% EAT+THAT=APPLE in any base in ASP.
%
% Change base by
%   clingo -c base=11 EAT+THAT=APPLE.lp
% 

#const base=10.

letter(e;a;t;h;p;l).
values(0..base-1).

% exact 1 occurrence of each letter
1 { x(L,Val) : values(Val) } 1 :- letter(L).

% 0..1 occurrences of each value
{ x(L,Val) : letter(L) } 1 :- values(Val).

% no digit can be given to two different symbols
% :- letter(L), letter(L1), x(L,V1), x(L1,V1), L != L1.

smm :- 
   values(E;A;T;H;P;L),
   x(e,E), x(a,A), x(t,T), x(h,H),
   x(p,P), x(l,L),
   E > 0, 
   A > 0,
   T > 0,
   E*base**2+A*base**1+T + T*base**3+H*base**2+A*base**1+T == A*base**4+P*base**3+P*base**2+L*base**1+E.

:- not smm.

#show x/2.
