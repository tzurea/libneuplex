<<<
 List of properties of combination
---

- $$ C(n,r) = C(n,n-r) $$ 
- $$ C(n,r) = C(n,r') $$ then r + r' = n
- $$ C(n,r) + C(n,r-1) = C(n+1,r) $$ 


>>> 
<<<
 Proof of property of combination as C(n,r) = C(n,n-r)
---


- $$ C(n,n-r) = \frac{n!}{(n- n +r)!(n-r)!} = C(n,r) $$



>>> 
<<<
 Proof of property of combination as C(n,r) = C(n,r') then r + r' = n
---


- $$ C(n,r) = C(n,r') $$
- $$ C(n,r) = C(n,n - r') $$
- $$ r = n - r' $$
- $$ r + r' = n $$ 



>>> 
<<<
 Proof of property of combination as C(n,r) + C(n,r-1) = C(n+1,r)
---


- $$ C(n,r) = \frac{n!}{(n-r)!r!} $$ 
- $$ C(n,r-1) = \frac{n!}{(n - r +1)!(r-1)!} $$
- $$ C(n,r) + C(n,r-1) = \frac{n!}{(n-r)!(r-1)!}[ \frac{1}{r} + \frac{1}{n-r+1} ] $$
- $$ C(n,r) + C(n,r-1) = \frac{n!}{(n-r)!(r-1)!} \times \frac{n + 1}{r(n - r +1)} $$
- $$ C(n,r) + C(n,r-1) = \frac{(n+1)!}{(n-r+1)!r!} = C(n+1,r) $$








>>> 
