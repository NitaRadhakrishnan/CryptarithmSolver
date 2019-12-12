%
% SEEM+MEAN=TEAMS in any base in ASP.
%
% Change base by
%   clingo -c base=11 SEEM+MEAN=TEAMS.lp
% 

#const base=10.

letter(s;e;m;a;n;t).
values(0..base-1).

% exact 1 occurrence of each letter
1 { x(L,Val) : values(Val) } 1 :- letter(L).

% 0..1 occurrences of each value
{ x(L,Val) : letter(L) } 1 :- values(Val).

% no digit can be given to two different symbols
% :- letter(L), letter(L1), x(L,V1), x(L1,V1), L != L1.

smm :- 
   values(S;E;M;A;N;T),
  x(s,S), x(e,E), x(m,M), x(a,A), x(n,N), x(t,T),
   S > 0, 
   T > 0,
   M > 0,
  S*base**3 +E*base**2+E*base**1+M + M*base**3+E*base**2+A*base**1+N == T*base**4+E*base**3+A*base**2+M*base**1+S.


:- not smm.

#show x/2.
