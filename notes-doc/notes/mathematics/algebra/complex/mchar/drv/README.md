Proof of product of two complex numbers in normal form : 
[latex]
\begin{align*}
z_1 = r_1( \cos \theta_1 + i \sin \theta_1 ) \\
z_2 = r_2( \cos \theta_2 + i \sin \theta_2 ) \\
z_1z_2 =r_1( \cos \theta_1 + i \sin \theta_1 ) r_2( \cos \theta_2 + i \sin \theta_2 ) \\
= r_1r_2( \cos \theta_1 \cos \theta_2 - \sin \theta_1 \sin \theta_2 ) + i ( \sin \theta_1 \cos \theta_2 + \cos \theta_1 \sin \theta_2 ) \\
= r_1 r_2 ( \cos( \theta_1 + \theta_2 ) + i \sin ( \theta_1 + \theta_2 ) ) 
\end{align*}
[/latex]


Proof of quotient of two complex numbers : 
[latex]
\begin{align*}
z_1 = r_1( \cos \theta_1 + i \sin \theta_1 ) \\
z_2 = r_2( \cos \theta_2 + i \sin \theta_2 ) \\
\frac{z_1}{z_2} = \frac{r_1 ( \cos \theta_1 + i \sin \theta_1 )}{r_2 ( \cos \theta_2 + i \sin \theta_2 )} \\
= \frac{r_1}{r_2} \frac{( \cos \theta_1 + i \sin \theta_1 )( \cos \theta_2 - i \sin \theta_2 )}{ ( \cos \theta_2 + i \sin \theta_2 )( \cos \theta_2 - i \sin \theta_2 ) } \\
= \frac{r_1 ( \cos \theta_1 + i \sin \theta_1 )[\cos - \theta_2 + i \sin - \theta_2]}{ r_2( \cos^{2} \theta_2 + \sin^{2} \theta_2 ) } \\
= \frac{r_1}{r_2}[ \cos ( \theta_1 - \theta_2 ) + i \sin (theta_1 - \theta_2) ]
\end{align*}
[/latex]

Proof of product of complex numbers by euler's form : 
[latex]
\begin{align*}
z_1 = r_1e^{i \theta_1} \\
z_2 = r_2e^{i \theta_2} \\
z_1z_2 = r_1r_2 e^{i ( \theta_1 + \theta_2 )} 
\end{align*}
[/latex]

Proof of quotient of complex numbers by euler's form : 
[latex]
\begin{align*}
z_1 = r_1 e^{i \theta_1} \\
z_2 = r_2 e^{i \theta_2} \\
\frac{z_1}{z_2} = \frac{r_1}{r_{2}} e^{i ( \theta_1 - \theta_2 )} 
\end{align*}
[/latex]

Proof of de moivre's theorem : 
[latex]
\begin{align*}
P(n) = [r( \cos \theta + i \sin \theta )]^{n}  = r^{n}( \cos n \theta +i \sin n \theta ) \\
P(1) = r( \cos \theta + i \sin \theta ) = r^1( \cos 1 \theta + i \sin 1 \theta ) \\
P(k) = [r( \cos \theta + i \sin \theta )]^{k} = r^{k}( \cos k \theta + i \sin k \theta ) \\
P(k+1) = [r( \cos \theta + i \sin \theta )]^{k +1} = r^{k+1}( cos k \theta + i \sin k \theta )(\cos \theta + \sin \theta) \\
= r^{k+1}( \cos( \theta(k+1) ) + i \sin ( \theta (k+1) ) ) \\
\end{align*}
[/latex]


Root of a complex number : 
[latex]
\begin{align*}
{R(\cos \phi + i \sin \phi)}^{n} = r( \cos \theta + i \sin \theta ) \\
R^{n}(\cos n \phi + i \sin n \phi) =  r(\cos \theta + i \sin \theta) \\
R^{n} = r \\
R = r^{1}{n} \\
\cos n \phi = \cos \theta \\
n \phi = 2k \pi + \theta \\
\phi = \frac{2k \pi + \theta}{n} \\
w = R( \cos \phi + i \sin \phi ) \\
z_{k} = r^{\frac{1}{k}} [ \cos \frac{k . 360 + \theta}{n} + i \sin \frac{k.360 + \theta}{n} ]   
\end{align*}
[/latex]

Cube roots of unity : 
[latex]
\begin{align*}
z^{3} = 1 \\
z^{3} =  1 + i.0 \\
z^{3} =  \cos 0 + i \sin 0 \\
z = [ \cos 0 + i \sin 0 ]^{\frac{1}{3}} \\
= 1^{\frac{1}{3}} [ \cos \frac{ k.360 + 0 }{3} + i \sin \frac{k.360 + 0}{3} ] \\
= \cos k.120 + i \sin k.120 \\
\text{where k = 0,1,2} \\ 
k = 0 \implies z = \cos 0 + \sin 0 = 1 + i0 = 1 \\
k = 1 \implies z = \cos 120 + i \sin 120 = - \frac{1}{2} + i \frac{\sqrt{3}}{2} = \frac{-1 + \sqrt{3} i}{2}
k = 1 \implies z = \cos 240 + i \sin 240 = - \frac{1}{2} - i \frac{\sqrt{3}}{2} = \frac{-1 - \sqrt{3} i}{2}
\end{align*}
[/latex]

Proof of imaginary cube root of unity as square of the other : 
[latex]
\begin{align*}
( \frac{-1 + \sqrt{3}i}{2} )^{2} = \frac{1 - 2 \sqrt{3}i  + 3i^{2}}{4} \\
= \frac{1 -2\sqrt{3}i - 3}{4} \\
= \frac{-1 - \sqrt{3}i}{2} \\
( \frac{-1 - \sqrt{3}i}{2} )^{2} = \frac{1 + 2 \sqrt{3}i  + 3i^{2}}{4} \\
= \frac{-2 +2\sqrt{3}i }{4} \\
= \frac{-1 + \sqrt{3}i}{2} \\
\end{align*}
[/latex]



Proof of product of two imaginary cube roots of unity as 1 : 
[latex]
\begin{align*}
\omega \omega^{2} = \frac{-1 + \sqrt{3} i}{2} \times \frac{-1 - \sqrt{3}i}{2} = \frac{1 - 3i^{2}}{4} = \frac{4}{4} = 1
\end{align*}
[/latex]

Proof of sum of three cube roots of unity : 
[latex]
\begin{align*}
1 + \omega + \omega^{2} = 1 + \frac{-1 + \sqrt{3}i}{2} + \frac{-1 - \sqrt{3}i}{2} \\
= \frac{2 - 1 + \sqrt{3}i - 1 - \sqrt{3}i }{2} = 0
\end{align*}
[/latex]






