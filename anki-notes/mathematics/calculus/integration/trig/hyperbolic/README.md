<<<
 Expression for integration of hyperbolic function sinhx
---


- $$ \int sinh x dx = coshx + C $$ 

>>> 
<<<
 Derivation for expression for integration of hyperbolic function sinhx
---

- $$ \int sinh x dx = \int \frac{1}{2} ( e^{x} - e^{-x} ) dx $$
- $$  = \frac{1}{2}( e^{x} + e^{-x} ) + C $$
- $$ \int sinh x dx = coshx + C $$ 


>>> 
<<<
 Expression for integration of hyperbolic function coshx
---



- $$ \int cosh x dx = sinhx + C $$ 



>>> 
<<<
 Derivation for expression for integration of hyperbolic function coshx
---



- $$ \int cosh x dx = \int \frac{1}{2} ( e^{x} + e^{-x} ) dx $$
- $$ = \frac{1}{2}(e^{x} - e^{-x}) + C $$
- $$ \int cosh x dx = sinhx + C $$ 



>>> 
<<<
 Expression for integration of hyperbolic function tanhx
---


- $$ \log( coshx ) + C $$ 

>>> 
<<<
 Derivation for expression for integration of hyperbolic function tanhx
---


- $$ \int tanhx dx = \int \frac{sinhx}{coshx} dx $$
- $$ z = coshx $$ 
- $$ \int \frac{dz}{z} $$ 
- $$ \log(z) + C $$ 
- $$ \log( coshx ) + C $$ 



>>> 
<<<
 Expression for integration of hyperbolic function cothx
---

- $$ \int cothx = \log( sinhx ) + C $$ 


>>> 
<<<
 Derivation for expression for integration of hyperbolic function cothx
---

- $$ \int cothx = \int \frac{coshx}{sinhx} dx $$ 
- $$ \int cothx = \log( sinhx ) + C $$ 


>>> 
<<<
 Expression for integration of hyperbolic function cosechx
---

- $$ \int cosechx dx = \log( tanh (\frac{x}{2}) ) + C $$ 

>>> 
<<<
 Derivation for expression for integration of hyperbolic function cosechx
---


- $$  \int cosechx dx = \int \frac{1}{sinhx}dx $$ 
- $$ \int \frac{2}{e^{x} - e^{-x}} dx $$ 
- $$ \int \frac{2 e^{x}}{e^{2x} - 1} dx $$ 
- $$ y = e^{x} $$ 
- $$ 2 \int \frac{1}{y^{2} - 1} dy $$ 
- $$ = \log( \frac{y-1}{y+1} ) + C $$ 
- $$ = \log( \frac{e^{x} - 1}{e^{x} + 1} ) + C $$ 
- $$ \int cosechx dx = \log( tanh (\frac{x}{2}) ) + C $$ 



>>> 
<<<
 Expression for integration of hyperbolic function sechx
---

- $$ \int sechx dx = 2 \tan^{-1} ( tanh(\frac{x}{2}) ) + C $$ 




>>> 
<<<
 Derivation for expression for integration of hyperbolic function sechx
---

- $$ \int sechx dx = \int \frac{1}{coshx} dx $$ 
- $$ = \frac{dx}{ cosh^{2}( \frac{x}{2} ) + sinh^{2}( \frac{x}{2} ) } $$ 
- $$ = \int \frac{ sech^{2}{ \frac{x}{2} } }{ 1 + tanh^{2}{\frac{x}{2}} } dx  $$ 
- $$ z = tanh \frac{x}{2} $$ 
- $$ = 2 \int \frac{dz}{1 + z^{2}} $$ 
- $$ = 2 tan^{-1}z + C $$
- $$ \int sechx dx = 2 \tan^{-1} ( tanh(\frac{x}{2}) ) + C $$ 

>>> 
<<<
 Expression for integration of hyperbolic function square of sechx
---


$$ \int sech^{x}dx = tanhx $$ 

>>> 
<<<
 Expression for integration of hyperbolic function square of cosechx 
---

$$ \int cosech^{x}dx = - cothx $$ 


>>> 
<<<
 Expression for integration of hyperbolic function sechx times tanhx
---

$$ \int sechx tanhx dx = - sechx $$ 


>>> 
<<<
 Expression for integration of hyperbolic function cosechx times cothx
---

$$ \int cosechx cothx = - cosechx $$ 





>>> 
