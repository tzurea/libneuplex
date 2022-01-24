<<<
 Expression for integration of cosec x
---

$$ \int cosec x dx = \log(\tan{\frac{x}{2}}) + C $$ 



>>> 
<<<
 Derivation for expression of integration of cosec x
---

- $$ cosec x dx = \int \frac{1}{\sin x} dx $$
- $$ = \int \frac{dx}{2 \sin{\frac{x}{2}} \cos{\frac{x}{2}}} $$ 
- $$ = \frac{1}{2} \int \frac{1}{\sin{\frac{x}{2}} \cos{\frac{x}{2}}} \frac{\sec^{\frac{x}{2}}}{\sec^{2}{\frac{x}{2}}} dx $$ 
- $$ \frac{1}{2} \int \frac{\sec^{2}{\frac{x}{2}}}{\tan{\frac{x}{2}}} dx $$
- $$ cosec x dx = \log(\frac{x}{2}) + C $$ 


>>> 
<<<
 Expression for integration of sec x
---

$$ \int \sec x dx = \log(\tan( \frac{\pi}{4} + \frac{x}{2} )) + C $$ 

>>> 
<<<
 Derivation for expression of integration of sec x
---

- $$ \int \sec x dx = \int \frac{dx}{\cos x} $$
- $$ = \int \frac{1}{ \sin( \frac{\pi}{2} + x ) } $$
- $$ = \frac{1}{2} \frac{dx}{ \sin( \frac{\pi}{4} + \frac{x}{2} ) \cos ( \frac{\pi}{4} + \frac{x}{2} ) } $$ 
- $$ = \frac{1}{2} \int \frac{ \sec^{2}{\frac{\pi}{4} + \frac{x}{2}} }{\tan( \frac{\pi}{4} + \frac{x}{2} )} $$
- $$ \int \sec x dx = \log ( \tan( \frac{\pi}{4} + \frac{x}{2} ) ) + C $$ 



>>> 
<<<
 Derivation for general expression of integration of   ( a + b cosx ) in denominator in unresolved cases
---

- $$ \int \frac{dx}{a + b \cos(x)} \\   $$
- $$ =\int \frac{d x}{a\left(\cos ^{2} \frac{1}{2} x+\sin ^{2} \frac{1}{2} x\right)+b\left(\cos ^{2} \frac{1}{2} x-\sin ^{2} \frac{1}{2} x\right)} \\   $$
- $$ =\int \frac{1}{(a+b) \cos ^{2} \frac{1}{2} x+(a-b) \sin ^{2} \frac{1}{2} x} \times \frac{\sec ^{2} \frac{1}{2} x}{\sec ^{2} \frac{1}{2} x} dx \\   $$
- $$ = \int \frac{\sec^{2}\frac{1}{2}x}{(a + b ) + (a-b)\tan^{2}\frac{1}{2}x}   $$


>>> 
<<<
 Derivation for expression of  integration of ( a + b cosx ) in denominator when a > b in standard integrals of special trigonometric functions
---

- $$ \int \frac{\sec^{2}\frac{1}{2}x}{(a + b ) + \sqrt{(a-b)}\tan\frac{1}{2}x}^{2} \\  $$
- $$ y = \sqrt{a -b }\tan{\frac{1}{2}x} \\  $$
- $$ \frac{dy}{dx} = \frac{1}{2}\sqrt{a -b } \sec^{2}{\frac{1}{2}x} \\  $$
- $$ \sec^{2}{\frac{1}{2}x} = \frac{2 dy}{\sqrt{a - b }} \\  $$
- $$ I =  \frac{2}{\sqrt{a-b}} \int \frac{dy}{ (\sqrt{(a + b ) })^{2}+ y^{2 }}\\  $$
- $$ I = \frac{2}{\sqrt{a-b}} \times \frac{1}{ \sqrt{a+b}} \tan^{-1}(\frac{y}{\sqrt{a+b}}) \\  $$
- $$ I = \frac{2}{\sqrt{a^{2}- b^{2}}} \tan^{-1}(\sqrt{\frac{{a-b}}{a + b}} \tan{\frac{x}{2}})  $$
 

>>> 
<<<
 Derivation for expression of integration of  ( a + b cosx ) in denominator when b > a in standard integrals of special trigonometric functions
---

- $$ \int \frac{\sec^{2}\frac{1}{2}x}{(a + b ) - \sqrt{(b-a)}\tan\frac{1}{2}x}^{2} \\  $$
- $$ \text{Let } y = \sqrt{b -a  }\tan{\frac{1}{2}x} \\  $$
- $$ \frac{dy}{dx} = \frac{1}{2}\sqrt{b -a } \sec^{2}{\frac{1}{2}x} \\  $$
- $$ \sec^{2}{\frac{1}{2}x} = \frac{2 dy}{\sqrt{b - a }} \\  $$
- $$ I =  \frac{2}{\sqrt{b-a}} \int \frac{dy}{ (\sqrt{(a + b ) })^{2} -  y^{2 }}\\  $$
- $$ I = \frac{2}{\sqrt{b-a}} \times \frac{1}{ 2 \sqrt{a+b}} \log_{e}(\frac{\sqrt{a +b } + y }{\sqrt{a+b} -y }) \\  $$
- $$ I = \frac{1}{\sqrt{b^{2}- a^{2}}} \log_{e}(\frac{\sqrt{b + a} + \sqrt{b - a} \tan{\frac{1}{2}x}}{\sqrt{b + a} - \sqrt{b - a} \tan{\frac{1}{2}x}})  $$


>>> 
<<<
 Derivation for expression of  integration of ( a + b cosx ) in denominator when a = b in standard integrals of special trigonometric functions
---

- $$ I = \int \frac{dx}{a(1 + \cos(x))} \\  $$
- $$ = \frac{1}{a}  \int \frac{dx}{2 \cos^{2}(\frac{x}{2} )}dx  \\  $$
- $$ = \frac{1}{2a} \int \sec^{2}{\frac{x}{2}} dx \\  $$
- $$ = \frac{1}{2a}  \frac{\tan{\frac{x}{2}}}{\frac{1}{2}}  \\  $$
- $$ = \frac{1}{a} \tan{\frac{x}{2}}  $$

>>> 
<<<
  Expression for integration of special trigonometric function in the terms of ( a + b  cosx ) as denominator when  a > b
---

$$ \int \frac{dx}{a + b \cos{x}} =  \frac{2}{\sqrt{a^{2}- b^{2}}} \tan^{-1}(\sqrt{\frac{{a-b}}{a + b}} \tan{\frac{x}{2}}) $$

>>> 
<<<
  Expression for  integration of special trigonometric function in the terms of ( a + b  cosx ) as denominator when  b > a 
---


$$  \int \frac{dx}{a + b \cos{x}} = \frac{1}{\sqrt{b^{2}- a^{2}}} \log_{e}(\frac{\sqrt{b + a} + \sqrt{b - a} \tan{\frac{1}{2}x}}{\sqrt{b + a} - \sqrt{b - a} \tan{\frac{1}{2}x}}) $$

>>> 
<<<
  Expression for  integration of special trigonometric function in the terms of ( a + b  cosx ) as denominator when  a = b  
---

$$   \int \frac{dx}{a + b \cos{x}} = \frac{1}{a} \tan{\frac{x}{2}} $$




>>> 
<<<
 Derivation of integral of special trigonometric function in terms of ( a + b sinx ) as denominator when  a > b 
---


- $$ I = \int \frac{dx}{a + b \sin(x) } \\  $$
- $$ I = \int \frac{dx}{a \sin^{2}{\frac{x}{2}} + a \cos^{2}{\frac{x}{2}} + b 2 \sin(x) \cos(x)}  \\  $$
- $$ I = \int \frac{\sec^{2}{\frac{x}{2}}}{a \tan^{2}{\frac{x}{2}}   + a + 2b \tan(\frac{x}{2})} dx \\  $$
- $$ \text{Let} y = \tan{\frac{x}{2}} \\  $$
- $$ \frac{dy}{dx} = \frac{1}{2}\sec^{2}{\frac{x}{2}} \\  $$
- $$ \sec^{2}{\frac{x}{2}}dx = 2 dy \\  $$
- $$ I = \int \frac{2dy}{ay^{2} + 2by + a} \\  $$
- $$ I = 2 \int \frac{dy}{(\sqrt{a}y)^{2}  + 2 \sqrt{a}y \frac{b}{\sqrt{a}} + (\frac{b}{\sqrt{a}})^{2} + a - (\frac{b}{\sqrt{a}})^{2} } \\  $$
- $$ I = 2 \int \frac{dy}{(\sqrt{a}y + frac{b}{\sqrt{a}})^{2}  + (\sqrt{\frac{a^{2}-b^{2}}{a}})^{2} }\\  $$
- $$ I = \frac{2}{a \sqrt{a^{2}- b^{2}}} \tan^{-1}(\frac{\sqrt{a}\tan{\frac{x}{2}} + \frac{b}{\sqrt{a}}}{\frac{\sqrt{a^{2} - b^{2}}}{\sqrt{a}}}) \\  $$
- $$ I = \frac{2}{\sqrt{a^{2}- b^{2}}} \tan^{-1}(  \frac{ a \tan(\frac{x}{2}) + b}{\sqrt{a^{2} - b^{2}}} )  $$




>>> 
<<<
  Expression for integration of special trigonometric function in the terms of ( a + b  sinx ) as denominator where  a > b  
---


$$ \int \frac{dx}{a + b \sin(x)} = \frac{2}{\sqrt{a^{2}- b^{2}}} \tan^{-1}(  \frac{ a \tan(\frac{x}{2}) + b}{\sqrt{a^{2} - b^{2}}} ) $$ 




>>> 
<<<
 Derivation of integral of special trigonometric function in terms of ( a + b sinx ) as denominator when  b > a  
---


- $$ I = \int \frac{dx}{a + b \sin(x) } \\  $$
- $$ I = \int \frac{dx}{a \sin^{2}{\frac{x}{2}} + a \cos^{2}{\frac{x}{2}} + b 2 \sin(x) \cos(x)}  \\  $$
- $$ I = \int \frac{\sec^{2}{\frac{x}{2}}}{a \tan^{2}{\frac{x}{2}}   + a + 2b \tan(\frac{x}{2})} dx \\  $$
- $$ \text{Let} y = \tan{\frac{x}{2}} \\  $$
- $$ \frac{dy}{dx} = \frac{1}{2}\sec^{2}{\frac{x}{2}} \\  $$
- $$ \sec^{2}{\frac{x}{2}}dx = 2 dy \\  $$
- $$ I = \int \frac{2dy}{ay^{2} + 2by + a} \\  $$
- $$ I = 2 \int \frac{dy}{(\sqrt{a}y)^{2}  + 2 \sqrt{a}y \frac{b}{\sqrt{a}} + (\frac{b}{\sqrt{a}})^{2} + a - (\frac{b}{\sqrt{a}})^{2} } \\  $$
- $$ I = 2 \int \frac{dy}{    (\sqrt{a}y  +  \frac{b}{\sqrt{a} } )^{2}  - ( \sqrt{(\frac{b^2   - a^2  }{a}) } )^{2} }   \\  $$
- $$ I = \frac{1}{\sqrt{b^2 - a^2}}    \log_{e}{    \frac{   a \tan{  \frac{ x }{ 2 }  }  + b - \sqrt{b^2 - a^2}    }{  a \tan{   \frac{ x }{ 2 }  }  +b + \sqrt{  b^2  -  a^2  }  }      }  $$




>>> 
<<<
  Expression for integration of special trigonometric function in the terms of ( a + b  sinx ) as denominator when  b > a  
---


$$ I = \frac{1}{\sqrt{b^2 - a^2}}    \log_{e}{    \frac{   a \tan{  \frac{ x }{ 2 }  }  + b - \sqrt{b^2 - a^2}    }{  a \tan{   \frac{ x }{ 2 }  }  +b + \sqrt{  b^2  -  a^2  }  }      } $$


>>> 
<<<
 Derivation for the integration of special trigonometric function having  ( a + b sinx ) in denominator when     a = b 
---


- $$ \int \frac{dx}{a + b \sin x} $$ 
- $$ \int \frac{dx}{a + a \sin x} $$
- $$ \frac{1}{a} \int \frac{dx}{1 + \sin x} $$
- $$ \frac{1}{a} \int \frac{dx}{ \sin^{2}{\frac{x}{2}} + \cos^{2}{\frac{x}{2}} + 2 \sin\frac{x}{2} \cos \frac{x}{2} } $$ 
- $$ \frac{1}{a} \int  \frac{\sec^{2}\frac{x}{2} dx }{ \tan^{2}{\frac{x}{2}} + 2 \tan{\frac{x}{2}} + 1 } $$ 
- $$ y = \tan{\frac{x}{2}} $$ 
- $$ \frac{dy}{dx} = \frac{1}{2} \sec^{2}\frac{x}{2} $$
- $$ 2dy = \sec^{2}{\frac{x}{2}}dx $$
- $$ \frac{2}{a} \int \frac{dy}{(y + 1)^{2}} $$
- $$ \frac{2}{a} \frac{(y +1)^{-2+1}}{-1}  $$
- $$ \frac{-2}{a( y +1 )}  $$
- $$ \frac{-2}{a( \tan{\frac{x}{2}} + 1 )} $$ 



>>> 
<<<
 Expression for integration of  ( a + b sinx ) in denominator when a = b in special trigonometric function  
---


- $$ \frac{-2}{a( \tan{\frac{x}{2}} + 1 )} $$ 





>>> 
<<<
 Derivation for expression of integration of ( a sinx + b cosx ) in denominator in special trigonometric functions
---


- $$ a = r \cos \alpha $$ 
- $$ b = r \sin \alpha  $$ 
- $$ r = \sqrt{ a^{2} + b^{2} } $$
- $$ \alpha = \tan^{-1}( \frac{b}{a} ) $$
- $$ \int \frac{dx}{a \sin x + b \cos x} = \frac{1}{r} \int \frac{dx}{ \cos \alpha \sin x + \sin \alpha \cos x } $$ 
- $$ \frac{1}{r} \int \frac{dx}{ \sin(x + \alpha) } $$ 
- $$ \frac{1}{r} \int cosec(x+ \alpha) dx $$ 
- $$ \frac{1}{r} \log( \tan{\frac{x + \alpha}{2}} ) $$ 
- $$ \int \frac{dx}{a \sin x + b \cos x} = \frac{1}{\sqrt{a^{2} + b^{2}}} \log( \tan ( \frac{x + \tan^{-1}{\frac{b}{a}}}{2} ) ) $$ 


>>> 
<<<
 Expression for expression of integration of ( a sinx + b cosx ) in denominator in special trigonometric functions
---


- $$ \int \frac{dx}{a \sin x + b \cos x} = \frac{1}{\sqrt{a^{2} + b^{2}}} \log( \tan ( \frac{x + \tan^{-1}{\frac{b}{a}}}{2} ) ) $$ 












>>> 
