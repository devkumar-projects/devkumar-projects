<h1 align="center">Dev Kumar</h1>
<p align="center"><strong>R&D Engineering Consultant · Robotics · Control · Machine Learning · AI</strong></p>
<p align="center">
  <a href="https://dev-kumar.com/">Portfolio</a> ·
  <a href="https://www.linkedin.com/in/devkumar-robotics-ai-engineer">LinkedIn</a> ·
  <a href="https://www.kaggle.com/devkumarkaggle">Kaggle</a> ·
  <a href="https://huggingface.co/devkumarhf">Hugging Face</a> ·
  <a href="https://orcid.org/0009-0008-2279-9163">ORCID</a> ·
  <a href="https://cv.hal.science/dev-kumar">HAL CV</a> ·
  <a href="https://github.com/devkumar-projects?tab=repositories">Projects</a>
</p>

I am an Arts et Métiers engineering graduate specializing in mechatronics, robotics and AI. I explore how robots perceive their environment, estimate their state and make decisions — from control theory and computer vision to reinforcement learning.

**R&D engineering consultant — robotics, control, machine learning and AI.** Open to engineering and applied research opportunities in **Paris, France; Geneva & Zurich, Switzerland; San Francisco & New York, United States**. **Open to worldwide freelance projects.**

## Applied research focus

I investigate how learning-based robot behaviour, geometric perception and model-based control can be combined and evaluated reproducibly. My public work includes UR7e/UR5e reinforcement-learning environments, ICP registration, Kalman filtering, RST and state-feedback control, plus collaborative studies in metrology, turbomachinery and semiconductor modelling.

Current study directions include reward design and failure analysis for robot learning; sensitivity to noise and initialization in perception; and tracking, stability and disturbance rejection in control. These are engineering investigations supported by source code and documented experiments. Each project states its assumptions, contributors and validation limits; simulation results are kept distinct from hardware evidence.

## Find the right evidence

**GitHub:** engineering source, architecture and reproduction. **Hugging Face:** reusable trained models and live inference. **Kaggle:** measured datasets and executable experiments. **HAL:** scientific archival records. **ORCID:** research identity and linked contributions.

## Inspect the work interactively

| Resource | What you can inspect | Validation scope |
| --- | --- | --- |
| [UR7e frozen SAC model](https://huggingface.co/devkumarhf/ur7e-sac-line-following) | Original checkpoint, portable NumPy actor and live [Policy Lab](https://huggingface.co/spaces/devkumarhf/UR7e-Policy-Lab) | Existing trained policy; CPU inference; default position-only kinematics |
| [UR7e SAC vs DLS benchmark](https://www.kaggle.com/code/devkumarkaggle/ur7e-sac-vs-dls-reproducible-policy-benchmark) | 600 measured CPU episodes, strict completion audit, baseline and sensor perturbations | 100 prespecified trajectories reused across paired conditions; SAC completion and DLS accuracy trade-off |
| [Engineering Workbench](https://huggingface.co/spaces/devkumarhf/Engineering-Workbench) | A selection of public technical projects with pinned sources and attribution; live RST synthesis; original UR7e log explorer | Source-linked case studies, reduced linear-model calculations and descriptive simulation data |
| [3D ICP Lab](https://huggingface.co/spaces/devkumarhf/ICP-Lab) | Rotate synthetic 3D clouds, step through Horn point-to-point ICP and vary noise/initialization | Independent educational browser adaptation; local convergence is not global alignment |
| [UR7e dataset on Hugging Face](https://huggingface.co/datasets/devkumarhf/ur7e-line-following-training-log) | Original 520-episode Monitor log, schema, source commit and checksum | One sequential simulated training run; no held-out or hardware evaluation |
| [Executed Kaggle notebooks](https://www.kaggle.com/devkumarkaggle/code) | Reproducible CPU analyses of perception, estimation, control, metrology and auditable ranking | Each notebook identifies its data, assumptions and source |
| [GaN deck audit](https://www.kaggle.com/code/devkumarkaggle/auditing-gan-simulation-decks-with-python) | Parse the recovered lateral HEMT inputs and test contact consistency | Static artifact inspection; no proprietary solver or device-performance claim |

The [Hugging Face collection](https://huggingface.co/collections/devkumarhf/robotics-perception-and-control-engineering-workbench-6afce1df9187d7a33c6da1ec) connects the demos and dataset. Source code, full project reports and upstream contribution records remain in the repositories below.

## Featured work

### [UR7e Robot Learning Suite](https://github.com/devkumar-projects/UR7e-Reinforcement-Learning-Suite)

Robot trajectory following, target reaching and obstacle avoidance, combining reinforcement learning, ROS 2, vision and state estimation. The simple trajectory-following simulation reports **97% completion over 100 random trajectories**. The real-robot implementation remains partial: end-to-end sim-to-real transfer is not yet validated.

[![UR7e demonstration](https://img.youtube.com/vi/--WNZJovDO4/hqdefault.jpg)](https://youtube.com/shorts/--WNZJovDO4?feature=share)

### [TurtleBot3 Autonomous Navigation](https://github.com/devkumar-projects/TurtleBot3-ROS2-Navigation-Challenges)

A simulated robot navigates a corridor, follows a line and pushes a ball using LiDAR, camera and odometry within a unified ROS 2 state machine. Built with **David Tovmassian**. The repository documents an external course dependency needed to reproduce the Gazebo environment.

[Watch the robot demonstration](https://youtube.com/shorts/X09uviqkwvI?feature=share)

### [RST Control of an Inverted Pendulum](https://github.com/devkumar-projects/RST-controller-for-an-inverted-pendulum)

A control engineering study of an unstable cart-pendulum system, with RST polynomial control, pole placement, disturbance rejection and MATLAB/Simulink analysis.

### [Classical Computer Vision Toolkit](https://github.com/devkumar-projects/Classical-Computer-Vision-Toolkit)

Three geometric vision projects covering optical-flow tracking and pose estimation, 3D point-cloud registration, and Hough-based pore segmentation. The repository explains the external data required for some examples.

## More projects

**Robot learning and control**
- [UR5e RL Pick-and-Place](https://github.com/devkumar-projects/ur5e-ReinforcementLearning-pick-and-place) — grasp-and-place training with SAC and HER in ROS 2 and Gazebo.
- [Twin-Rotor Helicopter Control](https://github.com/devkumar-projects/Control-of-an-instable-system-using-digital-state-feedback) — experimental identification, integral state feedback and LQR, with Steevy Doumbe Moundy and Léa Couësme.

**Engineering research and design**
- [VertiGaN Transistor Research](https://github.com/devkumar-projects/HeMT-GaN-Transistor) — exploratory GaN device modeling and analysis; results require further validation.
- [Compact Axial Turbine Design](https://github.com/devkumar-projects/-Design-of-a-Turbomachine) — hydraulic design, CAD, CFD and prototyping, with Thien Ho, Seyf Daab and Wilhem Abboura.
- [Spatial Verification of a CMM](https://github.com/devkumar-projects/-Spatial-Verification-of-a-Coordinate-Measuring-Machine) — trajectory design and metrology, with Thien Ho and a MATLAB correction pipeline.

**Software applications**
- [ProcureLens AI](https://github.com/devkumar-projects/ProcureLens-AI) — a desktop and command-line toolkit for auditable product-price extraction.
- [The Game 2048](https://github.com/devkumar-projects/The-game-2048) — an educational Python, Tkinter and SQLite implementation, with Michel Attoum and Celine Fernandes.

## Areas of interest

**Robotics:** ROS 2, robot navigation, motion control  
**AI and perception:** reinforcement learning, computer vision, sensor fusion  
**Engineering:** state estimation, system modeling, MATLAB/Simulink  
**Programming:** Python, C++, MATLAB

Explore the projects and demonstrations on my [portfolio](https://dev-kumar.com/).