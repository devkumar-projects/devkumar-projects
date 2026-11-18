# Model-to-code consistency in integral pole placement and shifted LQR for a twin-rotor benchmark

Dev Kumar; Steevy Doumbe Moundy; Léa Couësme

Version 1.0 - 18 November 2026

## Abstract

An independent numerical reconstruction checks a twin-rotor integral-control package. The shifted LQR gain is reproduced with a relative Riccati residual below 10⁻¹². The reported eigenvalues are identified as the shifted synthesis spectrum rather than the physical closed-loop spectrum. A separate elevation controller reproduces the published gains only with an input coefficient different from the stated transfer function. The work provides explicit corrected interpretations while making no new hardware-performance claim.

## Origin

The underlying collective work was an academic mechatronics project at Arts et Metiers, with CNAM mentioned in the report. This 2026 independent reanalysis checks the archived mathematical and software artifacts; it does not assert a new laboratory campaign.

The source package contains a discrete SISO elevation controller and a continuous MIMO integral LQR. These are related experiments, not two controllers evaluated on one identical plant and objective. This study asks whether their mathematical descriptions reproduce the gains in the archived source. It uses an independent SciPy implementation of zero-order-hold discretization, pole assignment and the continuous algebraic Riccati equation [3,4].

The source MIMO state is [elevation rate, elevation, pitch rate, pitch, yaw rate]. The source parameters are Ke=0.29, Kt=1.336, Kl=-5.21894, natural frequency 0.7 rad/s, damping 0.08 and yaw time constant 10 s. The narrative instead mentions damping 0.05 and time constant 20 s in its identification discussion. No new identification data select between these variants; this analysis reproduces the executable values.

The augmented block matrices are Aa=[[A,0],[C,0]] and Ba=[B;0]. Two integral states use the actual C matrix, selecting elevation and yaw rate. The numerical augmented matrix printed in the report selects pitch in its last row, which is inconsistent with the declared regulated outputs. The reproduced system uses C from the source. Q=diag(0,0,0,0,0,40,40), R=I2, and the physical feedback is u=-Kx_a.

The augmented pair has controllability rank 7. The shifted Riccati equation is satisfied with relative residual 9.28e-13. The reproduced first row of K is 12.382973, 16.984740, 2.327588, 6.074207, -15.426461, 11.231216, -10.267889. It agrees with the reported rounded gain.

The reported eigenvalues -0.5607±0.9945j, -0.6338±1.3929j, -1.0098 and -1.5259±0.5786j match the shifted system. The physical poles are each shifted left by 0.5 s⁻¹. The report equation must therefore include A_alpha, or equivalently an added 2 alpha P term, when describing the solved Riccati equation.

The elevation transfer function K/(s²/ω0²+2ξs/ω0+1) requires the input coefficient b=Kω0² in the state model. The script instead uses Kω0. With K=0.3299 and ω0=0.8038 rad/s, these are 0.21314656 and 0.26517362. The latter reconstructs the source discrete G and published gains; the former respects the stated transfer-function DC gain. This discrepancy is consequential for actuation scaling, even when integral action removes nominal steady-state tracking error.

The discrete integral state accumulates the sampled output without an explicit sample-period multiplier. This convention is reproduced exactly; its integral gain cannot be compared directly to a continuous-time gain without accounting for the convention. The desired pole map uses exp(s Ts), Ts=0.05 s and the declared Tc=1 s horizon. No saturation, observer, motor dynamics or measurement-noise model is added.

The historical report describes dSPACE responses, settling times and manually applied disturbances. Those observations remain historical. The present computation neither reopens the physical rig nor verifies the original timing definitions, sensor calibration, trial count or disturbance magnitude. It cannot establish that one controller is experimentally superior to the other.

Conclusion. The LQR gain and coded discrete pole-placement gain are reproducible. Three corrections are needed for a faithful paper: distinguish the shifted and physical spectra, use the correct integral-output selection, and disclose the incompatible SISO input normalizations. These corrections strengthen the model-to-code traceability without manufacturing a new experimental result.

## References

Dev Kumar; Steevy Doumbe Moundy; Léa Couësme. Helicopter Control Report. Unpublished academic project report; original context stated above. https://github.com/devkumar-projects/Control-of-an-instable-system-using-digital-state-feedback/blob/dc72199f1f650a6ae7a78a650c573f99bb1a4afa/docs/Helicopter_Control_Report.pdf

Source software, immutable Git revision dc72199f1f650a6ae7a78a650c573f99bb1a4afa. https://github.com/devkumar-projects/Control-of-an-instable-system-using-digital-state-feedback/tree/dc72199f1f650a6ae7a78a650c573f99bb1a4afa

K. J. Astrom and R. M. Murray. Feedback Systems: An Introduction for Scientists and Engineers. Princeton University Press, 2008. Author-hosted edition: https://authors.library.caltech.edu/records/yzs24-xsx88

SciPy developers. scipy.linalg.solve_continuous_are. Official documentation, accessed 18 November 2026. https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_continuous_are.html
