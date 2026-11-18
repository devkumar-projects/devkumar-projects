# Evidence boundaries and static verification of a recovered GaN simulation deck

Dev Kumar

Version 1.0 - 18 November 2026

## Abstract

A recovered lateral GaN HEMT device/stimulus pair is examined with a reproducible static parser and a corrupted-contact negative control. The defined contact and format checks pass for the archived pair, while the negative control is rejected. The study separates this source evidence from image-only claims concerning an exploratory vertical concept, and specifies cross-sweep and normalization checks required for a device-performance claim. No proprietary TCAD run, vertical-device replication, breakdown rating or patentability claim is made.

## Origin

The original work was a 2022 research internship at GeePs, CNRS UMR 8507 / CentraleSupelec. This 2026 independent note analyzes the recovered public artifacts rather than republishing the internship report as a new research report.

Can the public simulation artifacts substantiate the device-performance narrative, and which claims can be checked without a proprietary solver? This note examines the recovered lateral HEMT device and stimulus files, then distinguishes those executable inputs from image-only statements about an exploratory vertical concept. It is an artifact-verification study, not a new transistor-performance simulation.

The parser extracts balanced blocks for contacts, material regions and biases, records explicit physics switches and geometry bounds, and compares each named stimulus contact with the device definitions. The actual files are fingerprinted with SHA-256. The negative control changes one stimulus contact to NONEXISTENT_CONTACT while leaving the device unchanged. Parser extraction is a limited static analysis: unsupported syntax or external material files may escape these checks.

Gate-controlled charge in AlGaN/GaN structures is grounded in heterointerface physics [3]. That background does not establish that the recovered deck represents the proposed mirrored vertical device. In this public package the runnable source component is explicitly lateral. A vertical topology shown in a report image is not equivalent to a released vertical input deck.

A current per depth requires a declared extrusion width W. Differential resistance requires a stated gate bias, temperature and near-origin drain interval. Area-normalized resistance additionally needs an active area convention. These definitions prevent direct ranking of curves with incompatible normalization.

The defined device/stimulus consistency checks pass. The deliberately corrupted stimulus yields an unknown-contact error, demonstrating that the validator does not simply accept every pair. Neither result certifies the external material parameters, boundary conditions, solver convergence or physical accuracy. The proprietary Ecorce solver is not invoked.

Device SHA-256: dd1c59909412c5e360e68de0ac3baa11061605d09514d0b33b23cb2350d64a27. Stimulus SHA-256: ec7bec7922ab86202007d6b9067fd165b303120340221bc4d41c3322e51ee079. The full parser record is included in results.json.

The report transcribes a vertical-concept transfer trace near 10⁻¹⁴ A/cm and a separate output endpoint near 45.6 A/cm. If both refer to the same geometry, gate/drain state, terminal grouping and normalization, they cannot simultaneously describe the same steady solution. The appropriate next step is to recover that shared state and export raw terminal tables; it is not to combine favourable labels into one device specification.

Likewise, no avalanche-like rise through a requested 5 kV sweep does not establish breakdown above 5 kV. A credible threshold needs an explicit current criterion and resolved dynamic range; a breakdown value needs declared physics and criterion, mesh and field checks, and a reproducible bias sequence. This note does not use the recovered lateral switch settings to infer which physics was enabled in an unrecovered vertical run.

For future work, the minimal record per sweep is: immutable geometry and material identifiers, out-of-plane width, terminal map, initial state, sweep direction/step, enabled models, solver residuals and current balance. At shared bias points, transfer and output currents should agree within a declared tolerance. Mesh refinement should be performed before comparing architectures.

The historical concept was proposed during the GeePs internship under Tanguy Phulpin's supervision, with Ecorce support from Alain Michez. Attribution of the architectural hypothesis is retained; neither novelty, patentability, manufacturability nor a validated device rating is inferred. The report's scientific roadmap is future work, not a completed experimental program.

Conclusion. The public lateral pair is statically inspectable and the validator detects the chosen negative control. The available source does not reproduce the vertical concept or substantiate a combined high-current, normally-off, high-voltage specification. A narrower artifact-verification claim is reproducible now.

## References

Dev Kumar. VertiGaN CNRS Research Internship Report. Unpublished academic project report; original context stated above. https://github.com/devkumar-projects/HeMT-GaN-Transistor/blob/be700a57ed5af173f8d1b93d1dbd7ad10af33173/report/VertiGaN_CNRS_Research_Internship_Report.pdf

Source software, immutable Git revision be700a57ed5af173f8d1b93d1dbd7ad10af33173. https://github.com/devkumar-projects/HeMT-GaN-Transistor/tree/be700a57ed5af173f8d1b93d1dbd7ad10af33173

O. Ambacher et al. Two-dimensional electron gases induced by spontaneous and piezoelectric polarization charges in N- and Ga-face AlGaN/GaN heterostructures. Journal of Applied Physics 85, 3222-3233 (1999). https://doi.org/10.1063/1.369664
