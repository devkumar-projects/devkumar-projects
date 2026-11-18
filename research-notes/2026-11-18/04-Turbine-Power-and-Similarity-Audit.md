# Power-budget and similarity checks for a compact axial-turbine design artifact

Dev Kumar; Thien Ho; Seyf Daab; Wilhem Abboura

Version 1.0 - 18 November 2026

## Abstract

An independent power and dimensional audit examines a compact axial-turbine design report. At the reported nominal flow and head, hydraulic input is 4920.696 W; 5 kW mechanical output would require efficiency above unity. A reported 1760 W CFD point implies 34.61% efficiency if its stated head and flow use consistent boundaries. An air-prototype coefficient is converted into conditional power and torque without equating it with hydraulic efficiency. The analysis separates compact design, air testing and industrial planning, and makes no new CFD or experimental claim.

## Origin

The original four-author work was an academic multidisciplinary turbine-design project, 2024. This independent 2026 note re-evaluates declared scalar quantities and the scope of the associated simulation and prototype evidence.

A multidisciplinary design narrative can combine internally valid calculations that refer to different systems. This note asks which power claims follow from the reported compact-runner operating points, and which cannot be transferred from an air prototype or an industrial planning scenario. It is an arithmetic and dimensional audit, not a repetition of CFD, water-loop testing or structural qualification.

The nominal input is Q=0.132 m³/s, H=3.8 m, N=1500 rpm, with water density 1000 kg/m³ and g=9.81 m/s². A second report point uses Q=0.144 m³/s, H=3.60 m and mechanical power 1760 W. These are treated as separate points, not silently mixed. Hydropower depends on water flow and available head [3]; any electrical output also needs generator and converter efficiencies.

The air prototype is a distinct system with R=0.075 m, air density 1.2 kg/m³, V=10 m/s, angular speed 190.5 rad/s and reported maximum Cp=0.239. The report's 2 MW unit, 167-unit fleet and 2 TWh/year goal are a planning scenario. They are not a scale-qualified realization of the compact rotor.

For the CFD point, mechanical torque inferred from power and speed is 11.2045 N m. The implied efficiency is 34.61%, provided head and power use the same control-volume definition and operating point. This consistency value does not independently validate the CFD result.

The declared air point has available kinetic power 10.6029 W. Cp=0.239 implies shaft power 2.5341 W, torque 0.013302 N m and tip-speed ratio 1.42875. These are consequences of the reported coefficients and assumptions, not remeasured outputs. The separately reported efficiency near 0.56 requires its own denominator and operating point; it is not interchangeable with Cp.

For a fixed geometry at comparable dimensionless conditions, the source affinity-law script uses Q proportional to N, H proportional to N² and hydraulic power proportional to N³. It calculates pre-efficiency hydraulic power, not electrical generation. Transfer between air and water additionally requires attention to Reynolds number, blockage, surface roughness, tip clearance, mechanical losses and the imposed pressure boundary. An optimum in the air curve does not establish water-loop efficiency.

The historical CFD uses a steady moving-reference-frame approach and reports a residual threshold and a mesh size. A converged residual is not a discretization-error estimate. No independent mesh-convergence study, turbulence-model comparison or raw monitor replay is performed in this note. The inherited J.-F. Charpentier FEMM template is credited in the source project and is outside the hydraulic source component considered here.

The industrial scenario may be discussed as planning, but neither an ROI nor a 2 MW unit follows from the compact prototype. Two 1760 W units yield 3520 W before generator losses; they do not by themselves meet a 5 kW mechanical target. System boundaries must accompany every performance number.

Conclusion. The nominal 5 kW mechanical target is incompatible with the declared 3.8 m / 0.132 m³/s input. A revised head, flow, target or architecture is needed. The source artifacts remain useful for design exploration, provided hydraulic, aerodynamic and industrial scenarios are reported separately.

## References

Dev Kumar; Thien Ho; Seyf Daab; Wilhem Abboura. Compact Axial Hydraulic Turbine Report. Unpublished academic project report; original context stated above. https://github.com/devkumar-projects/-Design-of-a-Turbomachine/blob/6026cc9ce8b5817080ff12fdecf395db7e332828/docs/Compact_Axial_Hydraulic_Turbine_Report.pdf

Source software, immutable Git revision 6026cc9ce8b5817080ff12fdecf395db7e332828. https://github.com/devkumar-projects/-Design-of-a-Turbomachine/tree/6026cc9ce8b5817080ff12fdecf395db7e332828

U.S. Department of Energy. Hydropower Basics. Official technical overview, accessed 18 November 2026. https://www.energy.gov/cmei/water/hydropower-basics
