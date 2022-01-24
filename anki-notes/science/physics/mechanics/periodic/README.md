Simple Harmonic Motion
======================

**Objective:** *Define simple harmonic motion and state it’s equation.*

Background
----------

-   The motion which repeats itself after a *time* interval is
    **periodic motion**.

-   Oscillation, vibration, rotation, are *examples* of periodic motion.

Simple Harmonic Motion
----------------------

-   The motion in which the *restoring force* is directed towards a
    fixed point and is **proportional** to the *displacement* is
    **simple harmonic motion.**

-   A body in *simple harmonic motion* is called **harmonic
    oscillator.**

Equation for simple harmonic motion
-----------------------------------

-   The restoring force $F$ is directly proportional to displacement $x$
    .

$$\begin{aligned}
  F_{x} &= -kx \\
  F_{x} &= ma_x \\
  F_{x} &= m \frac{dv_x}{dt} \\
  F_{x} &= m \frac{d^2x}{dt^2} \\
  \frac{d^2x}{dt^2} &= \frac{-k}{m}x \\ \end{aligned}$$

-   The quantity $\frac{k}{m}$ can be expressed as $\omega^2$

<!-- -->

-   The differential equation for a body exhibiting **simple harmonic
    motion** is: $$\frac{d^2x}{dt^2} +  \omega^2x = 0$$

Acceleration in $S.H.M.$ 
------------------------

-   The equation expressing acceleration in $S.H.M.$ is:
    $$a = -\omega^2 x$$

Velocity in $S.H.M.$ 
--------------------

$$\begin{aligned}
      \frac{d^2x}{dt^2}  &= -\omega^2x \\
      \frac{dv}{dt} &= -\omega^2x \\
      \frac{dv}{dx}\times \frac{dx}{dt} &= -\omega^2x \\
      vdv &= -\omega^2xdx \\
      \int vdv &= -\omega^2 \int xdx \\
      \frac{v^2}{2} &= -\omega^2 \frac{x^2}{2} + C 
    \end{aligned}$$

-   At maximum displacement $x = A$ and $v = 0$.

$$\begin{aligned}
      C &= \omega^2 \frac{A^2}{2} \\
      \frac{v^2}{2} &= -\omega^2 \frac{x^2}{2} + \omega^2 \frac{A^2}{2} \\
      v^2 &= \omega^{2}(A^2 - x^2)
    \end{aligned}$$

-   The expression for **velocity** is given by:
    $$v = \omega \sqrt{A^2 - x^2}$$

Displacement in $S.H.M.$ 
------------------------

$$\begin{aligned}
      v &= \omega \sqrt{A^2 - x^2} \\
      \frac{dx}{dt} &= \omega \sqrt{A^2 - x^2} \\
      \frac{dx}{\sqrt{A^2 - x^2}} &= \omega dt \\
      \int \frac{dx}{\sqrt{A^2 -x^2}} &= \int \omega dt \\
      x &= A\sin{\theta} \\
      \frac{dx}{d\theta} &= A\cos \theta \\
      dx &= A \cos \theta d\theta \\
      \int \frac{A \cos \theta d\theta}{\sqrt{A^2 - x^2}} &= \omega t + \phi \\ 
      \int \frac{A \cos \theta d \theta}{\sqrt{A^2(1 - \sin^2 \theta)}} &= \omega t + \phi \\
      \int \frac{A \cos \theta d \theta}{A\cos \theta} &= \omega t + \phi \\
      \theta = \omega t + \phi 
    \end{aligned}$$

-   The equation for **displacement** $x$ is expressed as:
    $$x = A\sin(\omega t + \phi)$$

-   The equation for **velocity** can also be expressed as:
    $$v = \omega A \cos(\omega t + \phi)$$

-   The equation for **acceleration** can also be expressed as:
    $$a = -\omega^2 A\sin(\omega t + \phi)$$

Energy in $S.H.M$ 
=================

**Objective:** *Derive the expressions for energy in simple harmonic
motion.*

-   Energy in **simple harmonic motion** is exhibited in the form of
    both *kinetic and potential* energy.

Potential Energy in $S.H.M.$ 
----------------------------

-   The expression for force in relation with displacement is $F = -kx$.

-   $x$ and $F$ are opposite in direction.

$$\begin{aligned}
        dU &=  -dW \\
        dU &= kxdx \\
        \int dU &= \int kxdx \\
        U &= k \frac{x^2}{2} \\
        U &= \frac{1}{2}k A^2 \sin^2 (\omega t + \phi) \\
      \end{aligned}$$

-   The relation for **potential energy** in $S.H.M.$ is expressed as:
    $$U = \frac{1}{2} m \omega^2 A^2 \sin^2 (\omega t + \phi)$$

Kinetic Energy in $S.H.M.$ 
--------------------------

$$\begin{aligned}
      K &= \frac{1}{2}mv^2 \\
      K &= \frac{1}{2}m {\omega \sqrt{A^2 - x^2}}^2 \\
      K &= \frac{1}{2}m (\omega A \cos(\omega t + \phi))^2  
    \end{aligned}$$

-   The relation for **kinetic energy** in $S.H.M.$ is expressed as:
    $$K = \frac{1}{2} m \omega^2 A^2 \cos^2(\omega t + \phi)$$

Total Energy in $S.H.M.$ 
------------------------

$$\begin{aligned}
      E &= K + U \\ 
      E &= \frac{1}{2} \omega^2 A^2 \cos^2(\omega t + \phi) + \frac{1}{2} \omega^2 A^2 \sin^2 (\omega t + \phi) \\
      E &= \frac{1}{2}m \omega^2 A^2 
    \end{aligned}$$

-   The total energy in $S.H.M.$ is expressed as:
    $$E = \frac{1}{2} kA^2$$

Period
======

**Objective:** *Derive the expressions for period for vertical
oscillation of a mass suspended from coiled spring.*

Period in vertical oscillation
------------------------------

-   The restoring **force** acting on a body of mass $m$ due to
    **gravity** is proportional to the extension $e$ .

$$\begin{aligned}
    W &= mg \\
    W &= -ke \\
    mg &= -ke \\
  \end{aligned}$$

-   After further *extension* $y$ ,

$$\begin{aligned}
    F_1 &= -k(e +y) \\
    F &= F_1 -W \\
    F &= -k(e+y) + ke \\
    F &= -ke -ky + ke \\
    F &= -ky \\
    a &= \frac{-k}{m} y \\
    a &= -\omega^2 y \\
    \omega^2 &= \frac{k}{m} \\
    \omega &= 2 \pi f \\
    \omega &= \sqrt{\frac{k}{m}} \\
    f &= \frac{\omega}{2 \pi} \\
    f &= \frac{1}{2\pi}  \sqrt{\frac{k}{m}} \\
    T &= \frac{1}{f} \\ 
  \end{aligned}$$

-   The relation expressing *time period* in **vertical oscillation**
    is: $$T = 2\pi \sqrt{\frac{m}{k}}$$

Angular S.H.M.
==============

**Objective:** *Describe angular simple harmonic motion and find it’s
period.*

Angular Simple Harmonic Motion
------------------------------

-   The displacement is proportional **torque** $\tau$ acting on a body
    as : $$\tau \alpha \theta$$

-   The displacement and **torque** are opposite to each other.

-   The *restoring* **torque** can be expressed as: $$\tau = -k \theta$$

Period in Angular $S.H.M.$ 
--------------------------

$$\begin{aligned}
    \tau &= -k \theta \\
    \tau &= I \alpha \\
    I \alpha &= -k\theta \\
    \alpha &= \frac{-k}{I} \theta \\
    a &= - \omega^2 x \\
    \frac{-k}{I} \theta r &= - \omega^2 x \\
    \theta &= \frac{x}{r} \\
    \omega^2 &= \frac{k}{I} \\
    \omega &= \sqrt{\frac{k}{I}} \\
    f &= \frac{\omega}{2 \pi} \\
    f &= \frac{1}{2\pi}\sqrt{\frac{k}{I}} \\
    T &= \frac{1}{f} 
  \end{aligned}$$

-   The **time period** $T$ for **angular** $S.H.M.$ can be expressed
    as: $$T = 2\pi \sqrt{\frac{I}{k}}$$

Pendulum
========

**Objective:** *Derive expression for period of simple pendulum.*

Simple Pendulum
---------------

-   A bob of **mass** $m$ is taken.

-   The mass $m$ is suspended at a string of length $l$ .

-   Force acting on the *bob* at a **distance** $x$.

-   Angle $\theta$ is made at that distance.

-   The restoring force can be expressed in **two** components.

-   The **force** on *string* is balanced by the $cos$ component.

$$\begin{aligned}
    \tau = mg \cos \theta \\
  \end{aligned}$$

-   The **restoring** force for a *pendulum* is given by:
    $$F = -mg \sin \theta$$

Time Period for Simple Pendulum
-------------------------------

$$\begin{aligned}
      \sin \theta &= \theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} \\
    F &= -mg \theta \\
    \theta &= \frac{x}{l} \\ 
    a &= -\omega^2 x \\
    -\omega^2 x &= - g \frac{x}{l} \\
    \omega &= \sqrt{\frac{g}{l}} \\
    f &= \frac{\omega}{2 \pi} \\
    f &= \frac{1}{2\pi} \sqrt{\frac{g}{l}} \\
    f &= \frac{1}{T} 
  \end{aligned}$$

-   The relation expressing *time period* for simple pendulum is given
    by: $$T = 2\pi \sqrt{\frac{l}{g}}$$

Damped Oscillation
==================

**Objective:** *Explain damped oscillation.*

-   The gradual *decrement* of amplitude of a body in **simple harmonic
    motion** due to the *action* of resistive forces in it is
    **damping.**

-   The **oscillation** in damping is called **damped oscillation**

Forced Oscillation
==================

**Objective:** *Describe forced oscillation and resonance with suitable
examples.*

Forced Oscillation
------------------

-   **Forced oscillation** is the phenomenon of setting a body in
    *oscillation* with large **periodic** force.

Resonance
---------

-   **Resonance** is the phenomenon of setting a body to *oscillate* in
    it’s *natural frequency* by applying a **periodic** force of
    **same** magnitude of natural *frequency* of the body.

### Examples of resonance

-   **Resonance** is used in tuning *circuits* in radios to communicate
    in a particular **frequency.**

-   **Tachometers** detect the $rpm$ of motors by resonating *metal*
    strips.

-   *Sodium chloride* **crystals** resonate in *oscillating* electric
    field.

-   **Bridge** being marched by soldiers may collapse it **the
    marching** matches the **natural frequency** of the *bridge* .
