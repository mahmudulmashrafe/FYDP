# Final Year Design Project (FYDP) Defense — Presentation Slides (PPT)
## A Closed-Loop Wearable EEG Framework for Migraine Mitigation via Binaural Beat Entrainment
**Institution**: United International University (UIU)  
**Department**: Computer Science and Engineering  
**Total Duration**: 15 Minutes (15 Slides — 1 Slide / Minute)  
**Team Members**:
- Speaker 1: Abu Hurayra Mahbe (0112230043) — Slides 1 to 3
- Speaker 2: Md. Shakibul Hassan Prince (0112230048) — Slides 4 to 6
- Speaker 3: Anisa Azmi (0112230292) — Slides 7 to 9
- Speaker 4: Jarin Tabassum (0112230836) — Slides 10 to 12
- Speaker 5: Mahmudul Mashrafe (0112230115) — Slides 13 to 15

---

## ChatGPT / Gamma / Canva Prompting Guide
> **To generate PowerPoint directly**: Copy any slide block below and paste into ChatGPT with the prompt:
> *"Create a professional, high-contrast, modern dark-mode medical technology slide using the following slide title, layout, bullet points, and visual cues."*

---

# SECTION 1: INTRODUCTION & NEUROPHYSIOLOGY (SPEAKER 1)

---

### Slide 1: Title & Project Overview
- **Slide Type**: Title / Splash Slide
- **Slide Title**: A Closed-Loop Wearable EEG Framework for Real-Time Migraine Mitigation via Binaural Beat Entrainment
- **Subtitle**: Bridging Deep Learning Diagnostics with Patient-Tailored Acoustic Neuromodulation
- **Presenters**:
  - Abu Hurayra Mahbe (0112230043)
  - Md. Shakibul Hassan Prince (0112230048)
  - Anisa Azmi (0112230292)
  - Jarin Tabassum (0112230836)
  - Mahmudul Mashrafe (0112230115)
- **Academic Details**: Bachelor of Science in Computer Science and Engineering, United International University (UIU)
- **Visual Design Elements**:
  - Dark slate/navy blue background (`#0B132B`) with cyan/teal neuro-wave accents (`#48CAE4`)
  - United International University (UIU) Logo placed at the top-left or header
  - Central Loop Iconography: `Scalp EEG` $\rightarrow$ `STFT Spectrogram` $\rightarrow$ `Deep Learning CNN` $\rightarrow$ `Colormap Inversion` $\rightarrow$ `Binaural Audio` $\rightarrow$ `Brainstem Entrainment`

---

### Slide 2: Clinical Motivation & Neurophysiological Foundations
- **Slide Type**: Problem Statement & Medical Background
- **Slide Title**: Clinical Motivation: Thalamocortical Dysrhythmia & The Alpha Deficit
- **Layout**: 2-Column Comparative Layout
  - **Left Card: The Pathology (Interictal Migraine Brain)**:
    - **Global Prevalence**: Affects >1 Billion people; #2 global cause of years lived with disability (YLD).
    - **Cortical Hyperexcitability**: Heightened sensory processing and failure of habituation during silent attack-free periods.
    - **Thalamocortical Dysrhythmia (TCD)**: Desynchronization of thalamic pacemakers driving cortical rhythm collapse.
    - **Alpha Deficit & High TAR**: Significant depression of inhibitory alpha oscillations (8.0–13.0 Hz); elevated Theta-to-Alpha Ratio (TAR).
    - **Pharmaceutical Failure**: Medication Overuse Headaches (MOH), cardiovascular contraindications, and high attrition.
  - **Right Card: The Bio-Acoustic Mechanism (Binaural Beats)**:
    - **Dichotic Presentation**: Feeding frequency $f_1$ to the left ear and $f_2$ to the right ear via stereo earphones.
    - **Superior Olivary Complex (SOC)**: Brainstem calculates the phase differential and perceives an illusory beat: $\Delta f = |f_1 - f_2|$.
    - **Auditory Steady-State Response (ASSR)**: Neural phase-locking entrains cortical firing into rhythm $\Delta f$.
    - **The Personalized Mandate**: Entrainment only works if $\Delta f$ matches the patient's exact Individual Alpha Frequency (IAF).

---

### Slide 3: Project Scope & End-to-End System Architecture
- **Slide Type**: Architecture & Engineering Objectives
- **Slide Title**: Project Scope & End-to-End System Architecture
- **Layout**: 5-Stage Horizontal Process Flowchart
  - **Stage 1 (Acquisition & Preprocessing)**:
    - 128-channel UHD-EEG ($f_s = 2048 \rightarrow 512$ Hz) $\rightarrow$ CAR Reference $\rightarrow$ Zero-Phase Butterworth (1–50 Hz) $\rightarrow$ 60 Hz Notch.
  - **Stage 2 (Single-Channel Localization & STFT)**:
    - Occipital Channel #80 (Oz/O1 boundary) $\rightarrow$ 256-pt Hamming window (50% overlap) $\rightarrow$ 2D Viridis Spectrogram ($224 \times 224 \times 3$).
  - **Stage 3 (Deep Transfer Learning Diagnostic)**:
    - Pre-trained CNNs (VGG16, ResNet50, EfficientNetB7) $\rightarrow$ Automated Interictal Migraine Detection.
  - **Stage 4 (Mathematical Colormap Inversion)**:
    - 256-bin Viridis LUT Euclidean distance minimization $\rightarrow$ Reconstruct continuous linear PSD ($\mu\text{V}^2/\text{Hz}$) without raw data.
  - **Stage 5 (Closed-Loop Binaural Audio Synthesis)**:
    - Extract patient IAF $\rightarrow$ Generate stereo sine tones ($f_c = 216$ Hz, $\Delta f = \text{IAF}$) with 1.5s anti-click fade $\rightarrow$ 16-bit WAV.
- **Key Design Objective Banner**: *93.75% diagnostic accuracy on a single electrode, complete privacy preservation, and instant personalized non-invasive therapy.*

---

# SECTION 2: LITERATURE REVIEW & SIGNAL PREPROCESSING (SPEAKER 2)

---

### Slide 4: State of the Art & Research Gaps
- **Slide Type**: Literature Benchmarking & Gap Analysis
- **Slide Title**: State of the Art & Identified Research Gaps
- **Layout**: Comparative Matrix Table with Highlighted Gap
  | Research Domain | Representative Works | Primary Strengths | Critical Gaps Addressed by FYDP |
  | :--- | :--- | :--- | :--- |
  | **Multi-Channel AI Diagnosis** | Orhanbulucu et al. (2023), Aslan (2023), Göker (2023) | High diagnostic accuracy (94%–100%) | Requires 128 wet channels (\$25k+); strictly offline; **Zero therapeutic output** |
  | **Acoustic Entrainment Trials** | Alonso et al. (2024), Bhowmik et al. (2024), Battù et al. (2025) | Clinical proof of alpha-band pain modulation | Open-loop, static 10 Hz tones; **No automated diagnostic integration** |
  | **Evoked Potentials & Biomarkers** | Chamanzar et al. (2021), Hsiao et al. (2024) | High spatial resolution mapping of dysrhythmia | Unwearable laboratory setups; complex manual feature extraction |
  | **Our Closed-Loop Framework** | **Proposed FYDP (2026)** | **Single-channel (#80); 93.75% accuracy; <$250 wearable target** | **Unified Closed Loop: Auto-detection $\rightarrow$ Inversion $\rightarrow$ Custom Sound** |

---

### Slide 5: Dataset & Signal Conditioning Pipeline
- **Slide Type**: Methodology — Data Engineering
- **Slide Title**: Ultra-High-Density EEG Dataset & Signal Preprocessing
- **Layout**: 2-Column Split: Data Specs (Left) vs. Filtering Math (Right)
  - **Left Box: Carnegie Mellon University (CMU) UHD-EEG Dataset**:
    - **Cohort**: Clinically diagnosed interictal migraineurs and matched healthy controls.
    - **Equipment**: 128-channel BioSemi ActiveTwo laboratory system.
    - **Sampling**: $f_s = 2048$ Hz downsampled to 512 Hz (anti-aliasing Nyquist protection).
    - **Paradigms**: Eyes-Closed Resting State, Visual SSVEP, and Auditory SSAEP.
  - **Right Box: 3-Stage Signal Conditioning**:
    1. **Common Average Referencing (CAR)**:
       $$V_i^{\text{CAR}}(t) = V_i(t) - \frac{1}{N}\sum_{j=1}^N V_j(t)$$
       *Erases global spatial environmental electrical noise.*
    2. **Zero-Phase 4th-Order Butterworth Bandpass (1.0–50.0 Hz)**:
       *Forward-backward dual pass ($H(s) \cdot H(-s)$) ensures zero phase distortion and eliminates DC baseline wander.*
    3. **60 Hz Notch Filtering**:
       *Eradicates North American mains AC power-line hum.*

---

### Slide 6: Channel #80 Localization & STFT Spectrogram Generation
- **Slide Type**: Methodology — Time-Frequency Transformation
- **Slide Title**: Occipital Channel #80 Isolation & 2D Time-Frequency Transformation
- **Layout**: Visual Mapping & Waveform-to-Image Diagram
  - **Occipital Channel #80 (Oz/O1 Boundary)**:
    - Overlies the primary visual cortex (V1).
    - Origin of maximum physiological alpha rhythm generation.
    - Core generator of visual aura, photophobia, and sensory hyperexcitability.
    - Enables translation from a 128-cap to a sleek 1-electrode consumer headband.
  - **Short-Time Fourier Transform (STFT) Transformation**:
    $$X(\tau, \omega) = \int_{-\infty}^{\infty} x(t) w(t - \tau) e^{-j\omega t} dt$$
    - **Window Function**: 256-sample Hamming window ($T_w = 0.5$ seconds).
    - **Overlap**: 50% overlap (128 samples) to prevent boundary information loss.
    - **Colormap Standard**: 2D Viridis representation (perceptually linear, colorblind-safe).
    - **Standardized Dynamic Range**: $[-10\text{ dB}, +30\text{ dB}]$, exported at $224 \times 224 \times 3$ RGB.

---

# SECTION 3: DEEP LEARNING & MATHEMATICAL INVERSION (SPEAKER 3)

---

### Slide 7: Deep Transfer Learning Classification
- **Slide Type**: Methodology — Machine Learning
- **Slide Title**: Deep Transfer Learning Architectures & Training Strategy
- **Layout**: Architecture Comparison Cards + Hyperparameter Specs
  - **Model Architectures Benchmarked**:
    - **VGG16**: Deep sequential convolutional model; $3 \times 3$ receptive fields; 138M params.
    - **ResNet50**: Residual bottleneck blocks with identity skip connections; resolves vanishing gradient; 25.6M params.
    - **EfficientNetB7**: State-of-the-art compound scaling (depth $d=3.1$, width $w=2.0$, resolution $r=2.0$); MBConv inverted residual blocks; 66M params.
  - **Transfer Learning Protocol**:
    - Pre-trained on ImageNet (leverages edge, texture, and spectral pattern filters).
    - Top classification heads replaced: `GlobalAveragePooling2D` $\rightarrow$ `Dropout(0.5)` $\rightarrow$ `Dense(2, Softmax)`.
    - **Optimizer**: Adam ($\eta = 10^{-4}$), Loss: Categorical Cross-Entropy.
    - Stratified train/test validation splits with early stopping ($\Delta\text{loss} < 10^{-3}$).

---

### Slide 8: The Engineering Bottleneck: The 'Black-Box' Spectrogram
- **Slide Type**: Core Problem Formulation
- **Slide Title**: The Technical Bottleneck: The 'Black-Box' Spectrogram
- **Layout**: Dilemma / Challenge Illustration
  - **The Telemedicine / Edge Computing Dilemma**:
    - Raw multi-megabyte EEG streams consume heavy network bandwidth and breach HIPAA/GDPR data-sovereignty mandates during cloud transmission.
    - Modern digital health applications transmit compressed, standardized 2D time-frequency images (PNGs).
  - **The Missing Link**:
    - A standard spectrogram image quantizes continuous floating-point power into 24-bit RGB pixel color values.
    - To build a personalized acoustic prescription, **we need exact numeric physical power in $\mu\text{V}^2/\text{Hz}$ to pinpoint the patient's alpha peak.**
  - **The Challenge**:
    - Standard machine learning libraries treat spectrogram images as one-way visual outputs.
    - **How do we reverse-engineer continuous physical Power Spectral Density directly from RGB pixels without access to the original voltage timeseries?**

---

### Slide 9: The Analytical Minimum Euclidean Distance LUT Inversion
- **Slide Type**: Core Mathematical Innovation
- **Slide Title**: Formulating the Analytical RGB-to-PSD Inversion Algorithm
- **Layout**: Step-by-Step Mathematical Flow with Validation Callout
  - **Step 1: Color Lookup Table (LUT) Reference**:
    - Discretize the Viridis colormap into $K = 256$ normalized RGB reference vectors:
      $$\mathbf{c}_k = [R_k, G_k, B_k] \in [0, 1]^3 \quad \text{for } k \in \{0, 1, \dots, 255\}$$
  - **Step 2: 3D Euclidean Distance Minimization**:
    $$\hat{k}(i, j) = \arg\min_{k \in \{0, \dots, 255\}} \left\| \mathbf{P}_{\text{RGB}}(i, j) - \mathbf{c}_k \right\|_2 = \arg\min_k \sqrt{(R - R_k)^2 + (G - G_k)^2 + (B - B_k)^2}$$
  - **Step 3: Power Spectral Density Reconstruction**:
    $$\text{PSD}_{\text{dB}}(i, j) = \text{dB}_{\min} + \left(\frac{\hat{k}(i, j)}{255}\right) \cdot (\text{dB}_{\max} - \text{dB}_{\min}) \quad (\text{where } \text{dB} \in [-10, +30])$$
    $$P_{\text{linear}}(f) = 10^{\frac{\text{PSD}_{\text{dB}}(f)}{10}} \quad [\mu\text{V}^2/\text{Hz}]$$
  - **Empirical Validation**:
    - **Correlation Coefficient**: $R^2 > 0.998$ against numerical Welch transforms.
    - Accurately recovers narrow-band alpha peaks directly from rendered images.

---

# SECTION 4: BIOMARKERS, AUDIO SYNTHESIS & RESULTS (SPEAKER 4)

---

### Slide 10: Patient-Specific Neuro-Biomarker Extraction
- **Slide Type**: Methodology — Biomarker Quantitation
- **Slide Title**: Extraction of Electrophysiological Biomarkers
- **Layout**: 3 Formula Cards + Spectral Peak Curve
  - **1. Individual Alpha Frequency (IAF)**:
    $$\text{IAF} = \arg\max_{f \in [8.0, 13.0]} P_{\text{linear}}(f)$$
    *Captures patient-specific thalamocortical resonant peak frequency.*
  - **2. Relative Band Power & Alpha Deficit**:
    $$P_{\alpha}^{\text{rel}} = \frac{\int_{8}^{13} P(f)df}{\int_{1}^{50} P(f)df} \times 100\%, \quad \Delta P_\alpha = P_{\alpha,\text{normative}}^{\text{rel}} - P_{\alpha,\text{patient}}^{\text{rel}}$$
  - **3. Theta-to-Alpha Ratio (TAR)**:
    $$\text{TAR} = \frac{P_\theta^{\text{rel}}}{P_\alpha^{\text{rel}}} = \frac{\int_{4}^{8} P(f)df}{\int_{8}^{13} P(f)df}$$
  - **Diagnostic Confirmation**: Elevated TAR (>1.2) and negative alpha deficit confirm interictal cortical hyperexcitability and thalamocortical dysrhythmia.

---

### Slide 11: Dichotic Binaural Beat Audio Synthesis Engine
- **Slide Type**: Methodology — Audio Engineering
- **Slide Title**: Closed-Loop Binaural Audio Synthesis Engine
- **Layout**: Signal Equations + Waveform Diagram + Audio Specifications
  - **Dichotic Pure Tone Generation**:
    $$s_{\text{left}}(t) = A \cdot \sin\left(2\pi \left(f_c - \frac{\text{IAF}}{2}\right) t\right), \quad s_{\text{right}}(t) = A \cdot \sin\left(2\pi \left(f_c + \frac{\text{IAF}}{2}\right) t\right)$$
    - **Carrier Frequency ($f_c = 216.0$ Hz)**: Close to A3 concert pitch (220 Hz); optimal brainstem phase-locking ($<1.5$ kHz); soothing warm timbre.
    - **Binaural Entrainment Offset**: $\Delta f = |f_{\text{right}} - f_{\text{left}}| = \text{IAF}$ (Patient-specific, e.g., 9.87 Hz).
  - **1.5-Second Squared Half-Cosine Anti-Click Envelope**:
    $$E[n] = \sin^2\left(\frac{\pi n}{2 N_{\text{fade}}}\right) \quad \text{for } 0 \le n < N_{\text{fade}}$$
    *Guarantees zero high-frequency switching clicks to protect phonophobic ears.*
  - **Export Specifications**: 16-bit stereo PCM WAV ($[-32768, +32767]$), $f_s = 44.1$ kHz, calibrated to 60–65 dB SPL.

---

### Slide 12: Experimental Results & Patient M10 Case Study
- **Slide Type**: Results & Performance Evaluation
- **Slide Title**: Empirical Benchmarking & Single-Subject Case Study
- **Layout**: Model Comparison Table (Left) vs. Patient M10 Validation (Right)
  - **Left: Model Benchmarking Table (Single Channel #80)**:
    | Architecture | Accuracy | Precision | Recall | F1-Score | MCC | AUC |
    | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
    | VGG16 | 90.63% | 91.20% | 90.63% | 0.908 | 0.798 | 0.9062 |
    | ResNet50 | 87.50% | 88.40% | 87.50% | 0.879 | 0.741 | 0.8750 |
    | **EfficientNetB7** | **93.75%** | **100.0%** | **87.50%** | **0.933** | **0.875** | **0.9375** |
  - **Right: Patient M10 Case Study Validation**:
    - **Diagnosis**: Detected as Migraineur with 98.4% model confidence.
    - **Extracted IAF**: **9.87 Hz** (vs. Healthy Control C10 at 10.25 Hz).
    - **Biomarkers**: Alpha Deficit = **$-1.24~\mu\text{V}^2/\text{Hz}$**; TAR = **1.48** (vs. C10: 0.82).
    - **Generated Sound Prescription**:
      - Left Ear: **211.06 Hz** | Right Ear: **220.94 Hz** | Beat: **9.87 Hz** alpha entrainment.

---

# SECTION 5: CONSTRAINTS, COSTING, ACCREDITATION & CONCLUSION (SPEAKER 5)

---

### Slide 13: Standards Compliance & Realistic Design Constraints
- **Slide Type**: Real-World Engineering Constraints
- **Slide Title**: Engineering Standards Compliance & Design Constraints
- **Layout**: 6-Card Grid
  - **1. IFCN 10–20 Electrode Standard**: Channel #80 corresponds exactly to Oz/O1, ensuring anatomical repeatability on wearable headbands.
  - **2. WHO & OSHA Acoustic Safety**: Playback strictly bounded to 60–65 dB SPL (well below 85 dBA limits) to prevent cochlear fatigue.
  - **3. Health & Safety**: IEC 60601-1 electrical isolation (leakage $<10~\mu\text{A}$); zero photic flashing eliminates epileptic seizure risk.
  - **4. Social Constraint & Usability**: Replaces intimidating 128-cap headgear with a stylish fabric headband, de-stigmatizing workplace wear.
  - **5. Political & Privacy (SaMD)**: FDA 21 CFR Part 882 & EU MDR pathway; GDPR/HIPAA end-to-end AES-256 neural biometric encryption.
  - **6. Environmental Sustainability**: Non-drug digital therapy eliminates pharmaceutical manufacturing pollution and wastewater contamination; low-power SoC ($<100$ mW) curbs e-waste.

---

### Slide 14: Cost Analysis & Complex Engineering Mapping (P1–P7, EA1–EA5)
- **Slide Type**: Financial Viability & Washington Accord Mapping
- **Slide Title**: Cost Analysis & Complex Engineering Problem Solving
- **Layout**: 2-Column Split: Financial Economics (Left) vs. Accreditation Matrix (Right)
  - **Left: Cost Analysis & Business Model**:
    - **Academic R&D Budget**: **\$1,200.00** (GPU training, OpenBCI dev kit, audio DACs, sound calibrator).
    - **Commercial Mass-Production BOM (per 1,000 units)**: **\$95.00 / unit** (Dry flex sensor, BLE 5.3 SoC, Li-Po battery, textile band, earphones).
    - **Retail Pricing**: **\$199.00** (52% gross margin vs. \$25k BioSemi or \$499 Cefaly).
    - **Revenue Model**: D2C Hardware + Freemium App (\$7.99/mo) + B2B Neurology Clinic SaaS (\$150/mo).
  - **Right: Washington Accord / BAETE Accreditation Mapping**:
    - **P1–P7 Complex Problem Solving**: Depth of Knowledge (WK1–WK8 mapped), Conflicting Requirements (Wearability vs. Accuracy), In-Depth Analysis (LUT inversion), Applicable Codes, Stakeholder Engagement.
    - **EA1–EA5 Complex Engineering Activities**: High-resource GPU computing, interdisciplinary interactions, technological innovation, and significant societal impact.

---

### Slide 15: Conclusion, Key Contributions & Future Roadmap
- **Slide Type**: Summary & Conclusion
- **Slide Title**: Conclusion, Key Contributions & Future Roadmap
- **Layout**: 3 Contribution Badges + 3 Future Milestones
  - **Summary of Project Contributions**:
    1. **Single-Channel Efficacy**: Demonstrated 93.75% interictal detection accuracy using only occipital Channel #80.
    2. **Breakthrough Mathematical Inversion**: Successfully reversed quantized RGB spectrograms into continuous physical PSD ($R^2 > 0.998$).
    3. **Automated Closed-Loop Audio**: Seamlessly translated detected neural deficits into anti-click personalized binaural beats.
  - **Future Engineering Roadmap**:
    - Physical hardware PCB fabrication of the single-channel dry-sensor textile headband.
    - Real-time mobile application deployment on iOS and Android via ONNX / CoreML.
    - Multi-center clinical trials evaluating migraine attack frequency reduction and cortical habituation recovery.
- **Closing**: *Thank you for your time and guidance. We welcome your questions.*

---

## Defense Slide Summary Table (Quick Lookup)

| Slide # | Slide Title | Core Content / Visual | Assigned Speaker |
| :---: | :--- | :--- | :---: |
| **1** | Title & Project Overview | Project Title, UIU Logo, Loop Diagram | Speaker 1 (Abu Hurayra) |
| **2** | Clinical Motivation & Neurophysiology | TCD, Alpha Deficit, Superior Olive, ASSR | Speaker 1 (Abu Hurayra) |
| **3** | Project Scope & Architecture | 5-Stage Closed-Loop Engineering Pipeline | Speaker 1 (Abu Hurayra) |
| **4** | State of the Art & Research Gaps | Comparative Matrix across 5 Literature Domains | Speaker 2 (Prince) |
| **5** | Dataset & Preprocessing Pipeline | CMU UHD-EEG, CAR, Butterworth 1–50 Hz, Notch | Speaker 2 (Prince) |
| **6** | Channel #80 & STFT Spectrogram | Oz/O1 Localization, Hamming Window, Viridis | Speaker 2 (Prince) |
| **7** | Deep Transfer Learning Benchmark | VGG16 vs. ResNet50 vs. EfficientNetB7 Setup | Speaker 3 (Anisa) |
| **8** | The 'Black-Box' Spectrogram Dilemma | Why Invert? Privacy vs. Raw PSD Recovery | Speaker 3 (Anisa) |
| **9** | Analytical Colormap Inversion Algorithm | 256-LUT, Euclidean Distance, Formulas, $R^2 > 0.998$ | Speaker 3 (Anisa) |
| **10** | Biomarker Extraction: IAF, Deficit, TAR | Peak Detection, Integral Formulas, M10 Curve | Speaker 4 (Jarin) |
| **11** | Closed-Loop Binaural Audio Synthesis | $f_c = 216$ Hz, $\Delta f = \text{IAF}$, 1.5s Fade Envelope | Speaker 4 (Jarin) |
| **12** | Experimental Results & M10 Case Study | 93.75% Benchmark Table, M10 Custom Track | Speaker 4 (Jarin) |
| **13** | Standards Compliance & Constraints | IFCN, WHO/OSHA, Safety, Privacy, Sustainability | Speaker 5 (Mashrafe) |
| **14** | Cost Analysis & Complex Engineering | \$1,200 vs. \$95 BOM, Revenue, P1–P7 & EA1–EA5 | Speaker 5 (Mashrafe) |
| **15** | Conclusion & Future Roadmap | 3 Contributions, Hardware/Clinical Next Steps | Speaker 5 (Mashrafe) |
