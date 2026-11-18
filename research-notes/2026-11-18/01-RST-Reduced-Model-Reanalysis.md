# Nominal tracking and fixed-controller stability in a reduced inverted-pendulum RST design

Dev Kumar

Version 1.0 - 18 November 2026

## Abstract

An independent coefficient reconstruction and length-sweep analysis is applied to an existing inverted-pendulum RST artifact. The nominal Bezout identity and DC/sinusoidal tracking constraints are checked in Python. A printed coefficient sign is corrected, and the full characteristic polynomial is tested with fixed controller coefficients over 221 lengths. All sampled reduced plants are Hurwitz; the largest observed real part is -0.490188 s⁻¹. The analysis separates resynthesis from robustness, and does not claim nonlinear, actuator or physical validation.

## Origin

The source originates in a Semester 10 control project at Arts et Metiers, 2026. The present text is a new independent computational reanalysis of its reduced model, not the original student report relabelled as a research publication.

Can the published RST source be reconstructed independently, and what stability statement survives when controller coefficients are frozen while pendulum length varies? The question is narrower than nonlinear stabilization of a cart-pendulum. The artifact under study replaces the fast cart servo by unit gain and retains an unstable second-order plant. Feedback fundamentals and the distinction between local linear analysis and nonlinear stability follow [3].

The control law is S(s)u(s)=T(s)r(s)-R(s)y(s). With S(s)=s(s²+1)(s+c1), a fourth-order R is obtained by matching D=A S+B R. The target D=(s+a)²(s+β)(s+γ)((s+β)²+1) uses L0=0.35 m, β=0.5 s⁻¹, γ=30 s⁻¹ and a sinusoidal reference at 1 rad/s. This is a conventional pole-assignment construction, not a new control architecture.

The extra feedforward degrees of freedom enforce T(0)=R(0) and T(j)=R(j), producing unit reference response at zero frequency and at 1 rad/s whenever the closed loop is stable. These equalities describe steady-state tracking for the declared linear model. They say nothing about actuator saturation or the admissible pendulum angle.

Reproduce.py uses descending coefficient arrays, NumPy polynomial products and a two-by-two linear solve for the feedforward coefficients. The coefficient residual of the Bezout identity is normalized by the largest absolute coefficient of D, so the reported check is independent of polynomial scale.

The independent reconstruction gives a relative Bezout residual of 1.2e-16. Both H(0) and H(j) agree with one within 10⁻¹⁰. The initial design β=1, γ=10 yields r2=-51.579972, correcting the positive sign printed in the original report, printed p.13. The source code and direct coefficient matching agree on the negative sign.

A grid of 221 lengths between 0.16 and 0.60 m gives a largest observed real part of -0.490188 s⁻¹ for the frozen design. No sampled characteristic polynomial is unstable. Finite-grid verification is evidence for those samples; it is not a proof over the continuous interval.

The algebraic and numerical checks support nominal linear synthesis and sampled fixed-controller stability. They do not justify the original report's broad language of global stability. In particular, resynthesis at each uncertain length cannot establish robustness of one fixed controller. The complete polynomial D_L is evaluated without cancelling modes, so the test is not limited to an apparently well-behaved reference transfer after pole-zero cancellation.

A transparent coefficient record is R = -15.532074, -91.642997, -68.488086, -102.29662, -18.75; S = 1, 42.088403, 1, 42.088403, 0. Coefficients are ordered by descending powers. T = -1.3866913, -43.352848, -54.342703, -54.006476, -18.75. These values, rather than rounded report screenshots, define the reproduced nominal controller.

The original report includes a sign-inconsistent nonlinear-to-linear derivation and reported time traces. This note starts explicitly from the reduced transfer function implemented in the synthesis script; it does not certify that derivation or rerun the complete Simulink model. The reported ±5 V command bound, disturbance times and angular excursions are historical observations, not outputs of the present computation.

The next defensible validation step is a frozen-controller analysis with the fast servo restored, followed by delay and saturation models and nonlinear trajectories. A stability proof on an interval would require an analytic or validated numerical argument. A hardware claim would additionally require raw measurements, configuration and repeatability records.

Conclusion. The nominal source can be reproduced to floating-point accuracy, a printed sign is corrected, and the selected frozen controller is Hurwitz at all 221 sampled reduced plants. These are conditional computational results, not a guarantee of global nonlinear stabilization.

## References

Dev Kumar. RST Inverted Pendulum Report. Unpublished academic project report; original context stated above. https://github.com/devkumar-projects/RST-controller-for-an-inverted-pendulum/blob/ce3c6200df78a0f2e1578a4eae7dd80bdf542978/docs/RST_Inverted_Pendulum_Report.pdf

Source software, immutable Git revision ce3c6200df78a0f2e1578a4eae7dd80bdf542978. https://github.com/devkumar-projects/RST-controller-for-an-inverted-pendulum/tree/ce3c6200df78a0f2e1578a4eae7dd80bdf542978

K. J. Astrom and R. M. Murray. Feedback Systems: An Introduction for Scientists and Engineers. Princeton University Press, 2008. Author-hosted edition: https://authors.library.caltech.edu/records/yzs24-xsx88

NumPy developers. numpy.linalg.svd: Singular Value Decomposition. Official documentation, accessed 18 November 2026. https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html
