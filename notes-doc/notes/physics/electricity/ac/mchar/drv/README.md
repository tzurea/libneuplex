Current in rotating coil in magnetic field  : 
[latex]
\[
E = E_{0} \sin \omega t \\
E = IR \\ 
I = \frac{E}{R} \\
I = \frac{E_{0} \sin \omega t}{R} \\
I = I_{0} \sin \omega t 
\]
[/latex]

Time period  : 
[latex]
\[
\text{Time period } = \frac{\text{Angular displacement in complete cycle}}{\text{Angular velocity }} \\
T = \frac{2 \pi}{\omega} 
\]
[/latex]


Frequency  : 
[latex]
\[
f = \frac{1}{T} \\
f = \frac{\omega}{2 \pi}
\]
[/latex]

Proof for the value of ac over a complete cycle as zero  : 
[latex]
\[
I = I_{0} \sin \omega t \\
I = \frac{dq}{dt} \\
dq = I dt \\
dq = I_{0} \sin \omega t dt  \\
\int dq = I_{0}[\frac{- \cos \omega t}{ \omega }]^{T}_{0} \\
q = \frac{-I_{0} T}{2 \pi} [\cos 2 \pi - \cos 0] \\
q = \frac{-I_{0}T}{2 \pi}[ 1 -1  ] \\
q = 0 \\
I = \frac{0}{t} \\
I = 0
\]
[/latex]

Relation between average value and peak value of ac  : 
[latex]
\begin{align*}
I = I_{0} \sin \omega t \\
dq = I dt \\
q = \int^{\frac{T}{2}}_{0} dq = \int^{\frac{T}{2}}_{0} I_{0} \sin \omega t dt \\
q = \frac{-I_{0T}{2\pi}} [ \cos{\pi} - \cos{0} ] \\
q = \frac{-I_{0}T}{2 \pi} \times - 2 \\
q = \frac{I_{0}T}{\pi} \\
\text{Average value of ac over first half cycle } = \frac{q}{\frac{T}{2}} 
I_{av} = \frac{I_{0}T 2}{\pi T} \\
I_{av} = \frac{2 I_{0}}{\pi}
\end{align*}
[/latex]


Relation between effective and peak value  : 
[latex]
\begin{align*}
I = I_{0} \sin \omega t \\
dH = I^{2} R dt \\
H = \int^{T}_{0} I^{2}R dt \\
H = I_{eff}^{2} RT \\
I_{eff}^{2}RT = \int_{0}^{T} I^{2}R dt \\
I_{eff}^{2} = \frac{1}{T} \int_{0}^{T} I^{2} dt \\
I_{eff} = I_{rms} = \sqrt{\frac{1}{T} \int_{0}^{T} I^{2}dt} \\
\int_{0}^{T} I^{2}dt = \int^{T}_{0} I_{0}^{2} \sin^{2} \omega t dt \\
= I_{0}^{2} \int_{0}^{T} \frac{1 - \cos2 \omega t}{2} dt \\
= \frac{I_{0}^{2}}{2}[t - \frac{\sin 2 \omega t}{2 \omega}]^{T}_{0} \\
= \frac{I_{0}^{2}}{2}[(T-0) - \frac{1}{2 \omega} | \sin \frac{4 \pi}{T}t |^{T}_{0}] \\
= \frac{I_{0}^{2}}{2}[T - \frac{1}{2 \omega}(\sin 4 \pi - \sin 0)] \\
= \frac{I_{0}^{2}}{2}[T - 0] \\
= \frac{I_{0}^{2} T}{2} \\
I_{rms} = \sqrt{ \frac{1}{T}. \frac{I_{0}^{2}T}{2} } \\
I_{rms} = \frac{I_{0}}{\sqrt{2}} \\
\end{align*}
[/latex]

Relation between rms value and peak value of an alternating emf  : 
[latex]
\begin{align*}
E = E_{0} \sin \omega t \\
dH = \frac{E^{2}}{R}dt \\
= \frac{E_{0}^{2}}{R} \sin^{2} \omega t dt \\
H = \int dH \\
= \int^{T}_{0} \frac{E_{0}^{2}}{R} \sin^{2} \omega t dt \\
= \frac{E_{0}^{2}}{R} \int_{0}^{T} \frac{1 - \cos 2 \omegat}{2} dt \\
= \frac{E_{0}^{2}}{2R} [t - \frac{\sin 2 \omega t}{2 \omega}]^{T}_{0} \\
= \frac{E_{0}^{2}}{2R}[(T-0) - \frac{1}{2 \omega}|\sin \frac{4 \pi}{T} t|^{T}_{0}]\\
= \frac{E_{0}^{2}}{2R}[R - \frac{1}{2 \omega} \sin(4 \pi - \sin 0 )] \\
H = \frac{E_{0}^{2}}{2R}[T - 0] \\
H = \frac{E_{0}^{2}T}{2R} \\
H = \frac{E_{rms}^{2}T}{R} \\
\frac{E_{rms}^{2}T}{R} = \frac{E_{0}^{2}T}{2R} \\ 
E_{rms} = \frac{E_{0}}{\sqrt{2}}
\end{align*}
[/latex]

Proof for same phase of current and voltage at resistor : 
[latex]
\begin{align*}
E = E_{0} \sin \omega t \\
E = IR \\
E_{0} \sin \omega t = IR \\
I = \frac{E_{0}}{R} \sin \omega t \\
I = I_{0} \sin \omega t
E = E_{0} \sin \omega t
\end{align*}
[/latex]

Current at capacitor at ac circuit : 
[latex]
\begin{align*}
Q = CE \\
Q = C E_{0} \sin \omega t \\
\frac{dQ}{dt} = C E_{0} \omega \cos \omega t \\
\frac{dQ}{dt} = C E_{0} \omega \sin (\omega t + \frac{\pi}{2})
I = I_{0} \sin ( \omega t + \frac{\pi}{2} )
\end{align*}
[/latex]

Relation of effective current and effective voltage at capacitor : 
[latex]
\begin{align*}
I_{rms} = \frac{I_{0}}{\sqrt{2}} \\
I_{rms} = \frac{ \omega C E_{0} }{\sqrt{2}} \\
I_{rms} = \frac{E_{rms}}{\frac{1}{\omega C}} \\
I_{rms} = \frac{E_{rms}}{X_{c}}
\end{align*}
[/latex]



