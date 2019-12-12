%
% AT+EAST+WEST=SOUTH in any base in ASP.
%
% Change base by
%   clingo -c base=11 AT+EAST+WEST=SOUTH.lp
% 

#const base=10.

letter(a;t;e;s;w;o;u;h).
values(0..base-1).

% exact 1 occurrence of each letter
1 { x(L,Val) : values(Val) } 1 :- letter(L).

% 0..1 occurrences of each value
{ x(L,Val) : letter(L) } 1 :- values(Val).

% no digit can be given to two different symbols
% :- letter(L), letter(L1), x(L,V1), x(L1,V1), L != L1.

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
