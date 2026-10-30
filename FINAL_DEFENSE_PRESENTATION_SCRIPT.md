# Final Year Design Project (FYDP) Defense Presentation Guide
## Project Title: A Closed-Loop Wearable EEG Framework for Migraine Mitigation via Binaural Beat Entrainment
**Institution**: United International University (UIU)  
**Department**: Computer Science and Engineering  
**Total Duration**: 15 Minutes (Strictly ~3 Minutes per Speaker)  
**Team Members**:
1. **Speaker 1**: Abu Hurayra Mahbe (0112230043) — *Slides 1 to 3 (~3 mins)*
2. **Speaker 2**: Md. Shakibul Hassan Prince (0112230048) — *Slides 4 to 6 (~3 mins)*
3. **Speaker 3**: Anisa Azmi (0112230292) — *Slides 7 to 9 (~3 mins)*
4. **Speaker 4**: Jarin Tabassum (0112230836) — *Slides 10 to 12 (~3 mins)*
5. **Speaker 5**: Mahmudul Mashrafe (0112230115) — *Slides 13 to 15 (~3 mins)*

---

## Instructions for Generating Slides via ChatGPT / PowerPoint
> **How to use this document with ChatGPT**:
> Copy each slide's **"Slide Visual Content"** block and prompt ChatGPT:
> *"Generate a high-impact, professional PowerPoint slide (or python-pptx code / VBA code) with a modern dark-mode medical-tech theme using these bullet points, icons, metrics, and diagram layouts."*

---

# SPEAKER 1: Abu Hurayra Mahbe (0112230043)
**Time**: Minutes 0:00 – 3:00 (3 Minutes Total)  
**Role**: Introduction, Clinical Problem, Neurophysiology, and Project Objectives

---

### Slide 1: Title & Project Overview
- **Header**: Final Year Design Project Defense
- **Title**: A Closed-Loop Wearable EEG Framework for Real-Time Migraine Mitigation via Binaural Beat Entrainment
- **Subtitle**: Bridging Deep Learning Diagnostics with Patient-Tailored Acoustic Neuromodulation
- **Presenters**: Abu Hurayra Mahbe, Md. Shakibul Hassan Prince, Anisa Azmi, Jarin Tabassum, Mahmudul Mashrafe
- **Supervisor**: Department of Computer Science and Engineering, United International University
- **Visual Cues**:
  - UIU Logo + Sleek dark-mode neuro-tech background
  - Conceptual loop diagram showing: Scalp EEG $\rightarrow$ Spectrogram $\rightarrow$ Deep Learning $\rightarrow$ Binaural Beat $\rightarrow$ Auditory Cortex

#### Spoken Script (Speaker 1 — 60 seconds):
> "Honorable members of the defense board, respected supervisor, and faculty members—a very good morning. 
> 
> I am **Abu Hurayra Mahbe**, and on behalf of our team, I am honored to present our Final Year Design Project: *A Closed-Loop Wearable EEG Framework for Real-Time Migraine Mitigation via Binaural Beat Entrainment*.
> 
> Migraine is not just a simple headache; it is the second leading cause of years lived with disability worldwide, incapacitating over one billion people. Traditional pharmaceuticals like triptans and painkillers often lead to medication-overuse headaches, cardiovascular contraindications, and high rates of patient abandonment. 
> 
> Our mission in this project is to pioneer a non-pharmacological, closed-loop digital therapeutic: a system that can accurately detect a migraineur in their silent, pain-free interictal state from a single EEG electrode, decode their unique neural deficit, and immediately generate a personalized therapeutic sound track to restore brainwave balance."

---

### Slide 2: Neurophysiological Background & The Clinical Problem
- **Slide Title**: Clinical Motivation: Thalamocortical Dysrhythmia & The Alpha Deficit
- **Visual Layout**: 2-Column Split:
  - *Left Column (The Pathology)*:
    - **Cortical Hyperexcitability**: Hyper-sensitive sensory processing during pain-free interictal periods.
    - **Thalamocortical Dysrhythmia (TCD)**: Breakdown in communication between thalamic pacemakers and the cortex.
    - **Alpha Deficit**: Depressed power in the 8.0–13.0 Hz band; elevated Theta-to-Alpha Ratio (TAR).
  - *Right Column (The Acoustic Solution)*:
    - **Binaural Beats**: Dual tones with a slight frequency offset ($\Delta f$) presented dichotically via stereo earphones.
    - **Superior Olivary Complex**: Brainstem nucleus perceives the difference frequency and entrains cortical oscillations (Auditory Steady-State Response).
    - **Target**: Aligning $\Delta f$ to the patient's exact Individual Alpha Frequency (IAF) to restore thalamocortical synchrony.

#### Spoken Script (Speaker 1 — 60 seconds):
> "To understand our engineering approach, we must look inside the migraine brain during the 'interictal'—the period between attacks.
> 
> Neurophysiologically, migraineurs suffer from **Thalamocortical Dysrhythmia** and cortical hyperexcitability. In healthy individuals, the brain produces robust alpha oscillations between 8 and 13 Hertz to inhibit unnecessary sensory noise. In migraine patients, this protective alpha rhythm collapses, creating what literature defines as an **'Alpha Deficit'**, accompanied by an abnormally high Theta-to-Alpha Ratio.
> 
> This is where **acoustic neuromodulation** comes in. When we deliver two slightly different pure tones to the left and right ears, the brainstem's superior olivary complex creates an illusionary third rhythm called a **Binaural Beat**. If this beat matches the patient's natural alpha frequency, it physically entrains the cortex back into a stable state. 
> 
> However, existing commercial solutions fail because they deliver generic 10 Hz beats to everyone. Our project solves this by creating a true closed loop tailored to each patient's exact brain."

---

### Slide 3: Project Objectives & High-Level Closed-Loop Architecture
- **Slide Title**: Project Scope & End-to-End System Architecture
- **Visual Layout**: Flowchart diagram of the 5-stage closed loop:
  1. *Acquisition & Preprocessing*: 128-channel UHD-EEG $\rightarrow$ CAR + FIR Filtering $\rightarrow$ Occipital Channel #80.
  2. *Feature Transformation*: STFT $\rightarrow$ 2D Viridis Time-Frequency Spectrogram ($224 \times 224$).
  3. *Deep Classification*: Fine-tuned Pre-trained CNNs (VGG16, ResNet50, EfficientNetB7) $\rightarrow$ Interictal Migraine Detection.
  4. *Analytical Inversion*: RGB-to-PSD Colormap Inversion $\rightarrow$ Continuous Linear Power Spectrum Recovery.
  5. *Personalized Synthesis*: Extract IAF $\rightarrow$ Stereo Binaural Beat Generation ($f_c = 216$ Hz, $\Delta f = \text{IAF}$) $\rightarrow$ 16-bit Audio.
- **Key Deliverables Callout**:
  - High accuracy detection with only 1 channel
  - Elimination of raw signal transmission over clouds
  - Click-free, safe sound delivery ($<65$ dB SPL)

#### Spoken Script (Speaker 1 — 60 seconds):
> "To achieve this, our project defined three primary engineering objectives:
> 
> First, build an automated preprocessing and computer-vision pipeline that transforms single-channel EEG signals into high-density 2D time-frequency spectrogram images.
> 
> Second, benchmark deep transfer learning models to verify if an ultra-minimal montage—specifically single occipital Channel #80—can match the diagnostic accuracy of expensive 128-channel clinical setups.
> 
> Third, engineer a novel mathematical inversion algorithm that decodes continuous power spectral density directly from spectrogram images, extracts the patient's Individual Alpha Frequency, and drives an anti-click stereo audio synthesis engine.
> 
> Now, my teammate **Md. Shakibul Hassan Prince** will walk you through the existing literature, our identified research gaps, and our signal processing pipeline."

---

# SPEAKER 2: Md. Shakibul Hassan Prince (0112230048)
**Time**: Minutes 3:00 – 6:00 (3 Minutes Total)  
**Role**: Literature Review, Research Gaps, Dataset, and Signal Preprocessing

---

### Slide 4: Literature Review & The Critical Research Gap
- **Slide Title**: State of the Art & Identified Research Gaps
- **Visual Layout**: Comparative Matrix Table:
  - *Domain 1: Multi-Channel EEG AI* (Orhanbulucu 2023, Aslan 2023, Goker 2023): High accuracy (94–100%), but requires 128 wet electrodes costing \$25,000+; entirely offline; zero therapeutic output.
  - *Domain 2: Auditory Stimulation* (Alonso 2024, Bhowmik 2024, Battù 2025): Proves alpha entrainment reduces pain, but relies on static, generic frequencies with zero automated real-time diagnostic integration.
  - *The Critical Gap*: **No existing system unites single-channel wearable screening with personalized, closed-loop acoustic beat synthesis.**
- **Our Innovation**: Single-channel occipital screening coupled directly to patient-specific audio prescription via mathematical spectrogram inversion.

#### Spoken Script (Speaker 2 — 60 seconds):
> "Thank you, Abu Hurayra. I am **Md. Shakibul Hassan Prince**.
> 
> In reviewing over 50 contemporary peer-reviewed studies published between 2021 and 2025, we discovered a profound divide in the literature.
> 
> On one side, advanced deep learning studies—such as Orhanbulucu et al. (2023) and Aslan (2023)—achieved high diagnostic accuracy between 94% and 100%. However, they required cumbersome 128-channel wet electrode caps that take 45 minutes to apply and cost tens of thousands of dollars. Crucially, they stop at offline diagnosis and offer zero treatment.
> 
> On the other side, clinical neuroscience studies—like Alonso et al. (2024) and Battù et al. (2025)—demonstrated that acoustic binaural beats modulate cortical alpha rhythms. However, they delivered open-loop, one-size-fits-all tones without automated diagnostic feedback.
> 
> The research gap was clear: **Nobody had connected single-channel automated detection to patient-specific acoustic entrainment in a unified closed-loop framework.** That is precisely the gap our project bridges."

---

### Slide 5: Dataset & Signal Conditioning Pipeline
- **Slide Title**: Ultra-High-Density EEG Dataset & Preprocessing Pipeline
- **Visual Layout**:
  - *Dataset Box*:
    - Carnegie Mellon University (CMU) UHD-EEG Migraine Dataset
    - 128 Channels, BioSemi ActiveTwo System, $f_s = 2048$ Hz (downsampled to 512 Hz)
    - Paradigms: Eyes-Closed Resting State, Visual SSVEP, Auditory SSAEP
  - *Preprocessing Flow*:
    1. **CAR (Common Average Referencing)**: $V_i^{\text{CAR}}(t) = V_i(t) - \frac{1}{N}\sum_{j=1}^N V_j(t)$ (removes global electrical noise)
    2. **Zero-Phase 4th-Order Butterworth Bandpass**: 1.0 Hz to 50.0 Hz (isolates neural rhythms, suppresses DC drift)
    3. **60 Hz Notch Filter**: Eliminates North American electrical power-line interference.

#### Spoken Script (Speaker 2 — 60 seconds):
> "To train and validate our system, we utilized the gold-standard Carnegie Mellon University Ultra-High-Density EEG dataset, captured via a research-grade 128-channel BioSemi ActiveTwo system across migraineurs and matched healthy controls.
> 
> Raw EEG is notoriously noisy, contaminated by scalp muscle movements and mains hum. We developed a three-stage zero-phase signal conditioning pipeline:
> 
> First, **Common Average Referencing (CAR)** subtracts the instantaneous global average across all electrodes, eradicating widespread common-mode artifacts.
> 
> Second, a **zero-phase 4th-order Butterworth bandpass filter** isolates frequencies between 1.0 and 50.0 Hertz. The zero-phase forward-backward design is critical because it preserves the exact timing and phase of neural oscillations without phase distortion.
> 
> Third, a **60 Hz notch filter** completely eliminates power-line interference. This ensures that every downstream feature reflects genuine cerebral activity."

---

### Slide 6: Occipital Channel #80 Localization & STFT Spectrogram Generation
- **Slide Title**: Channel #80 Isolation & 2D Time-Frequency Transformation
- **Visual Layout**:
  - *Left Graphic*: 10-20 Head Map highlighting Channel #80 at the Oz/O1 boundary over the primary visual cortex (V1).
  - *Right Graphic*: 1D Voltage Timeseries $\rightarrow$ Windowed Fourier Transform $\rightarrow$ 2D Viridis Spectrogram Image ($224 \times 224 \times 3$).
  - *STFT Parameters Callout*:
    - Window: 256-point Hamming ($0.5$ s)
    - Overlap: 50% (128 samples)
    - FFT Length: $N_{\text{FFT}} = 256$
    - Colormap: Viridis (perceptually uniform, standardized dynamic range $[-10, +30]$ dB).

#### Spoken Script (Speaker 2 — 60 seconds):
> "The defining constraint of a wearable consumer device is channel count. You cannot wear 128 electrodes to bed or work. 
> 
> By analyzing neurophysiology, we targeted **Channel #80**, located right at the Oz/O1 boundary over the occipital lobe. The occipital cortex is the primary generator of human alpha rhythms and the epicenter of migraine visual aura and photophobia.
> 
> We segmented the cleaned 1D voltage signal from Channel #80 into epochs and applied the **Short-Time Fourier Transform (STFT)** using a 256-point Hamming window with 50% overlap. 
> 
> This converts raw temporal voltages into a 2D time-frequency image. We rendered these images using the **Viridis colormap** at $224 \times 224$ pixels, with power normalized across a fixed $-10$ to $+30$ dB scale. 
> 
> Next, **Anisa Azmi** will explain how we used deep transfer learning to classify these images and how we solved the mathematical challenge of inverting them back to raw power."

---

# SPEAKER 3: Anisa Azmi (0112230292)
**Time**: Minutes 6:00 – 9:00 (3 Minutes Total)  
**Role**: Deep Transfer Learning, The Black-Box Inversion Problem, and Mathematical Formulation

---

### Slide 7: Deep Transfer Learning Classification
- **Slide Title**: Deep Transfer Learning Architectures & Benchmarking
- **Visual Layout**:
  - Diagram comparing three pre-trained backbones:
    - **VGG16**: 138M parameters (Classical sequential CNN)
    - **ResNet50**: 25.6M parameters (Residual skip connections)
    - **EfficientNetB7**: 66M parameters (Compound scaling of depth, width, and resolution)
  - *Training Hyperparameters Table*:
    - Batch Size: 16 | Optimizer: Adam ($\eta = 10^{-4}$) | Loss: Categorical Cross-Entropy
    - Epochs: 50 with Early Stopping ($\Delta\text{loss} < 10^{-3}$)
    - Regularization: Dropout (0.5), L2 Weight Decay ($10^{-4}$).

#### Spoken Script (Speaker 3 — 60 seconds):
> "Thank you, Shakibul. I am **Anisa Azmi**.
> 
> Instead of relying on manual, handcrafted EEG features that often fail across different patients, we framed interictal migraine detection as a computer vision problem on our STFT spectrogram images.
> 
> We benchmarked three distinct deep transfer learning backbones: **VGG16**, **ResNet50**, and **EfficientNetB7**. All three models were pre-trained on ImageNet to leverage universal hierarchical visual filters like edges, textures, and harmonic patterns.
> 
> We removed their classification heads and added a custom dense head with global average pooling, a dropout layer of 0.5 to prevent overfitting, and a softmax binary output. 
> 
> We trained the network using Adam optimization with a reduced learning rate of $10^{-4}$ and categorical cross-entropy loss under stratified cross-validation. As you will see shortly in our results, EfficientNetB7 delivered extraordinary diagnostic precision."

---

### Slide 8: The Core Technical Bottleneck: The Spectrogram Inversion Problem
- **Slide Title**: The Engineering Problem: The 'Black-Box' Spectrogram
- **Visual Layout**:
  - *The Dilemma Diagram*:
    - Spectrogram Image (RGB Pixels: $[0, 255]$) $\xrightarrow{\text{Non-Linear Colormap}}$ How do we recover $\mu\text{V}^2/\text{Hz}$?
    - *Why not just send raw EEG?* Raw EEG files are massive, require uncompressed bandwidth, and introduce cloud transmission privacy vulnerabilities under HIPAA/GDPR.
    - *The Loss of Information*: Standard PNG/JPEG rendering quantizes continuous floating-point power into 24-bit RGB space.
  - *The Objective*: Reconstruct the exact continuous power spectral density curve $P(f)$ directly from visual RGB pixel matrices without needing original raw time-series voltage data.

#### Spoken Script (Speaker 3 — 60 seconds):
> "Now, I want to direct your attention to what is arguably the most mathematically innovative contribution of our project.
> 
> In traditional pipelines, once an image is generated, the underlying raw numerical values are discarded. In decentralized digital health or telemedicine, patient apps only transmit lightweight compressed spectrogram images to save bandwidth and protect privacy.
> 
> But here was our engineering bottleneck: **To synthesize a personalized binaural beat, we need the patient's exact numerical power spectrum in microvolts squared per Hertz to find their alpha peak.** 
> 
> If you only have a 2D PNG image where power is baked into RGB color pixels, how do you mathematically reverse-engineer those colors back into exact, continuous linear physical power? 
> 
> Standard libraries have no function for this. We had to invent an analytical inverse mapping algorithm from scratch."

---

### Slide 9: Analytical Colormap Inversion Algorithm
- **Slide Title**: Formulating the Minimum Euclidean Distance LUT Inversion
- **Visual Layout**:
  - *Mathematical Formulation Step-by-Step*:
    1. **Color Lookup Table (LUT)**: Discretize the Viridis spectrum into $K = 256$ normalized RGB reference vectors $\mathbf{c}_k = [R_k, G_k, B_k] \in [0, 1]^3$.
    2. **Minimum Euclidean Distance Optimization**:
       $$\hat{k}(i, j) = \arg\min_{k \in \{0, \dots, 255\}} \left\| \mathbf{P}_{\text{RGB}}(i, j) - \mathbf{c}_k \right\|_2 = \arg\min_k \sqrt{(R - R_k)^2 + (G - G_k)^2 + (B - B_k)^2}$$
    3. **Decibel & Linear Power Reconstruction**:
       $$\text{PSD}_{\text{dB}}(i, j) = \text{dB}_{\min} + \left( \frac{\hat{k}(i, j)}{255} \right) \cdot (\text{dB}_{\max} - \text{dB}_{\min})$$
       $$P_{\text{linear}}(f) = 10^{\frac{\text{PSD}_{\text{dB}}(f)}{10}} \quad [\mu\text{V}^2/\text{Hz}]$$
  - *Validation Graphic*: Scatter plot showing $R^2 = 0.998$ correlation between Inverted PSD and Numerical Welch PSD.

#### Spoken Script (Speaker 3 — 60 seconds):
> "Here is our mathematical formulation:
> 
> The Viridis colormap maps a normalized scalar index $k$ from 0 to 255 into a smooth trajectory through 3D RGB color space. 
> 
> For every pixel in our spectrogram, our algorithm extracts its RGB coordinate vector and computes the minimum Euclidean distance against all 256 reference vectors in the Viridis lookup table. This maps each pixel to its optimal discrete index $\hat{k}$.
> 
> Next, using our known dynamic range bounds of $-10$ and $+30$ dB, we linearly interpolate the decibel power, and then apply the inverse logarithmic transform to recover physical linear power in microvolts squared per Hertz.
> 
> When we benchmarked our reconstructed power spectra against ground-truth numerical Welch transforms, our algorithm achieved a correlation coefficient $R^2$ exceeding **0.998**. We successfully proved that visual spectrogram images can be converted back into calibrated clinical spectra with zero loss of peak fidelity!
> 
> My teammate **Jarin Tabassum** will now explain how we extract biomarkers from this spectrum and synthesize the therapeutic audio."

---

# SPEAKER 4: Jarin Tabassum (0112230836)
**Time**: Minutes 9:00 – 12:00 (3 Minutes Total)  
**Role**: Biomarker Extraction, Binaural Audio Synthesis, and Experimental Evaluation

---

### Slide 10: Neuro-Biomarker Extraction: IAF, Deficit & TAR
- **Slide Title**: Patient-Specific Biomarker Extraction
- **Visual Layout**:
  - *Equations & Graphical Peak Detection*:
    - **Individual Alpha Frequency (IAF)**:
      $$\text{IAF} = \arg\max_{f \in [8.0, 13.0]} P_{\text{linear}}(f)$$
    - **Relative Alpha Power ($P_\alpha^{\text{rel}}$)** & **Relative Theta Power ($P_\theta^{\text{rel}}$)**:
      $$P_\alpha^{\text{rel}} = \frac{\int_{8}^{13} P(f)df}{\int_{1}^{50} P(f)df} \times 100\%, \quad P_\theta^{\text{rel}} = \frac{\int_{4}^{8} P(f)df}{\int_{1}^{50} P(f)df} \times 100\%$$
    - **Theta-to-Alpha Ratio (TAR)**: $\text{TAR} = \frac{P_\theta^{\text{rel}}}{P_\alpha^{\text{rel}}}$
    - **Alpha Deficit**: $\Delta P_\alpha = P_{\alpha,\text{normative}}^{\text{rel}} - P_{\alpha,\text{patient}}^{\text{rel}}$
  - *Visual*: Annotated power spectrum plot showing the sharp 9.87 Hz peak detected for Patient M10.

#### Spoken Script (Speaker 4 — 60 seconds):
> "Thank you, Anisa. I am **Jarin Tabassum**.
> 
> Once our colormap inversion reconstructs the continuous power spectrum, our biomarker engine scans the alpha band between 8.0 and 13.0 Hertz.
> 
> It pinpoints the exact global maximum, defining the patient's **Individual Alpha Frequency (IAF)**. In medical literature, treating patients at their personalized IAF is vastly more effective than applying fixed 10 Hz stimulation, because each human brain has a genetically and physiologically unique peak.
> 
> The engine then integrates spectral power across the bands to compute the **Theta-to-Alpha Ratio (TAR)** and the **Alpha Deficit** relative to normative control baselines. 
> 
> As you see on the plot, an elevated TAR and depressed alpha power serve as quantitative physiological confirmations of thalamocortical dysrhythmia. This gives our system both diagnostic transparency and the exact numeric target needed for therapeutic synthesis."

---

### Slide 11: Dichotic Binaural Beat Synthesis Engine
- **Slide Title**: Closed-Loop Binaural Audio Synthesis Engine
- **Visual Layout**:
  - *Audio Generation Formulas*:
    $$s_{\text{left}}(t) = A \cdot \sin\left(2\pi \left(f_c - \frac{\Delta f}{2}\right) t\right), \quad s_{\text{right}}(t) = A \cdot \sin\left(2\pi \left(f_c + \frac{\Delta f}{2}\right) t\right)$$
    - Carrier: $f_c = 216.0$ Hz (Close to A3 concert pitch; optimal olivary phase-locking $<1.5$ kHz)
    - Beat Offset: $\Delta f = \text{IAF}$ (Patient-specific, e.g., 9.87 Hz)
  - *Anti-Click Fade Envelope*:
    $$E[n] = \sin^2\left(\frac{\pi n}{2 N_{\text{fade}}}\right) \quad \text{for } 0 \le n < N_{\text{fade}} \quad (T_{\text{fade}} = 1.5\text{ s})$$
  - *Audio Output*: 16-bit signed PCM WAV stereo, $f_s = 44,100$ Hz, calibrated to 60–65 dB SPL.

#### Spoken Script (Speaker 4 — 60 seconds):
> "With the patient's IAF isolated, our audio synthesis engine dynamically generates a dichotic stereo prescription.
> 
> We selected an ergonomic carrier frequency of **$f_c = 216.0$ Hertz**. This choice is grounded in psychoacoustics: first, the brainstem's superior olive can only detect interaural phase delays below 1.5 kHz; second, 216 Hz sits right beside concert pitch A3, providing a soothing, warm cello-like tone.
> 
> The dual channels are mathematically offset by half the IAF: the left ear receives $f_c - \frac{\text{IAF}}{2}$, and the right ear receives $f_c + \frac{\text{IAF}}{2}$. When heard through stereo headphones, the brain's auditory pathways perceive a pure, pulsating alpha entrainment rhythm at exactly the patient's IAF.
> 
> Crucially, for migraineurs who suffer from severe sound sensitivity, starting or stopping an audio track abruptly produces high-frequency transient switching clicks. To eliminate this, we designed a **1.5-second squared half-cosine taper envelope**, guaranteeing a completely smooth, click-free listening experience."

---

### Slide 12: Experimental Results & Patient M10 Case Study
- **Slide Title**: Empirical Benchmarking & Single-Subject Case Study
- **Visual Layout**: 2-Column Split:
  - *Left (Classification Benchmarks Table)*:
    - **EfficientNetB7**: **93.75% Accuracy** | **100% Precision** | **87.5% Recall** | **0.933 F1** | **0.875 MCC** | **0.9375 AUC**
    - VGG16: 90.63% Accuracy | 0.798 MCC
    - ResNet50: 87.50% Accuracy | 0.741 MCC
  - *Right (M10 Case Study Results)*:
    - Patient M10 IAF Detected: **9.87 Hz** (vs Control C10 at 10.25 Hz)
    - M10 Alpha Deficit: **$-1.24~\mu\text{V}^2/\text{Hz}$**
    - M10 Theta-to-Alpha Ratio: **1.48** (Elevated vs C10: 0.82)
    - Generated Audio Prescription: Left Ear = **211.06 Hz**, Right Ear = **220.94 Hz**, Beat = **9.87 Hz**.

#### Spoken Script (Speaker 4 — 60 seconds):
> "Let us examine our empirical results.
> 
> In our deep transfer learning benchmark, **EfficientNetB7** proved to be the superior architecture, achieving **93.75% classification accuracy**, **100% precision**, and a **Matthews Correlation Coefficient of 0.875** on held-out evaluation sets using only single-channel occipital data. It decisively outperformed both VGG16 and ResNet50.
> 
> To demonstrate the complete closed loop in practice, we conducted an in-depth case study on Patient M10 compared to healthy control C10.
> 
> Our system detected an interictal migraine state, inverted the spectrogram, and identified an IAF peak of **9.87 Hz**, showing an alpha deficit of $-1.24~\mu\text{V}^2/\text{Hz}$ and an elevated Theta-to-Alpha Ratio of 1.48, compared to 0.82 in the healthy control.
> 
> Within milliseconds, our audio engine generated a custom prescription: 211.06 Hz in the left ear and 220.94 Hz in the right ear, delivering an exact 9.87 Hz alpha entrainment tone. 
> 
> Now, our final speaker, **Mahmudul Mashrafe**, will discuss our engineering standards, cost analysis, and Washington Accord complex problem-solving attributes."

---

# SPEAKER 5: Mahmudul Mashrafe (0112230115)
**Time**: Minutes 12:00 – 15:00 (3 Minutes Total)  
**Role**: Standards, Constraints, Cost Analysis, Complex Engineering Problem Mapping, and Conclusion

---

### Slide 13: Standards Compliance & Multi-Faceted Engineering Constraints
- **Slide Title**: Engineering Standards & Realistic Design Constraints
- **Visual Layout**: Grid Layout of 6 Constraints:
  1. *IFCN 10–20 Standard*: Channel #80 maps precisely to Oz/O1 boundary for reproducible single-electrode placement.
  2. *WHO & OSHA Acoustic Safety*: Gain strictly bounded to 60–65 dB SPL to protect phonophobic patients from cochlear fatigue.
  3. *Health & Safety*: IEC 60601-1 electrical isolation (leakage $<10~\mu\text{A}$); zero photic stimulation eliminates seizure risk.
  4. *Social & Usability*: Replaces cumbersome clinical caps with discreet fabric headbands; empowers underserved migraineurs.
  5. *Political & Privacy*: FDA SaMD (21 CFR Part 882) compliance pathway; GDPR/HIPAA end-to-end AES-256 biometric encryption.
  6. *Sustainability*: Drug-free therapy eliminates pharmaceutical wastewater chemical pollution; low-power SoC ($<100$ mW) reduces e-waste.

#### Spoken Script (Speaker 5 — 60 seconds):
> "Thank you, Jarin. I am **Mahmudul Mashrafe**.
> 
> Any biomedical engineering solution must transition from academic theory into safe, ethical, and standardized real-world practice. 
> 
> Our framework complies strictly with international biomedical engineering standards. We adhere to **IFCN 10–20 standards** for electrode placement and follow **WHO and OSHA safe listening guidelines**, enforcing a strict software gain ceiling of 60 to 65 dB SPL to protect phonophobic patients.
> 
> We rigorously addressed multi-faceted design constraints:
> In **Health and Safety**, our proposed hardware enforces IEC 60601-1 electrical isolation with leakage currents under $10~\mu\text{A}$. Because our system is purely auditory, it completely eliminates the seizure and aura risks associated with visual stimulation.
> In **Social and Usability**, we replace intimidating clinical headgear with an everyday fabric headband, destigmatizing therapy in the workplace.
> In **Sustainability**, providing a non-pharmacological digital therapeutic directly reduces the chemical manufacturing emissions and wastewater contamination caused by chronic pharmaceutical overuse."

---

### Slide 14: Cost Analysis & Complex Engineering Mapping (P1–P7, EA1–EA5)
- **Slide Title**: Financial Viability & Complex Engineering Problem Solving
- **Visual Layout**: 2-Column Split:
  - *Left (Cost Breakdown & Business Model)*:
    - R&D Prototyping Budget: **\$1,200.00**
    - Commercial Mass-Production BOM (per 1,000 units): **\$95.00 / unit**
    - Retail Target: **\$199.00** (vs \$25,000 clinical BioSemi or \$499 Cefaly)
    - Revenue Model: D2C Hardware + Freemium App (\$7.99/mo) + B2B Clinic SaaS (\$150/mo).
  - *Right (Accreditation Mapping Matrix)*:
    - **P1 to P7 (Complex Problem Solving)**: Depth of Knowledge (WK1–WK8), Conflicting Requirements (Wearability vs Accuracy), Depth of Analysis (LUT Inversion), Codes & Standards, Stakeholder Involvement.
    - **EA1 to EA5 (Complex Engineering Activities)**: GPU & UHD-EEG resources, cross-disciplinary interactions, high innovation, and societal impact.

#### Spoken Script (Speaker 5 — 60 seconds):
> "A core pillar of our design is economic viability. Clinical 128-channel EEG systems cost upwards of \$25,000. 
> 
> By proving that single-channel occipital EEG retains 93.75% diagnostic accuracy, we reduced the sensor requirement by 99%. Our itemized mass-production bill of materials totals just **\$95.00 per unit**, allowing a retail price of \$199.00. Supported by a freemium app subscription and clinical B2B licensing, this represents a self-sustaining business model.
> 
> Furthermore, in accordance with the Washington Accord and BAETE criteria, this project exemplifies a **Complex Engineering Problem**:
> It satisfies **P1 through P7**: requiring deep multidisciplinary knowledge across eight profiles from natural sciences to DSP; resolving conflicting trade-offs between wearability and diagnostic accuracy; performing in-depth mathematical analysis to invert spectrograms; and adhering to stringent biomedical codes.
> It likewise fulfills **Engineering Activities EA1 through EA5**, deploying cutting-edge GPU and neuroimaging resources to produce a novel, socially impactful engineering solution."

---

### Slide 15: Conclusion, Societal Impact & Future Work
- **Slide Title**: Conclusion, Key Contributions & Future Roadmap
- **Visual Layout**:
  - *Three Core Takeaways*:
    1. **High Diagnostic Accuracy on Single Channel**: 93.75% accuracy using only Channel #80.
    2. **Breakthrough Mathematical Inversion**: First-of-its-kind RGB-to-PSD recovery ($R^2 > 0.998$).
    3. **Automated Closed-Loop Neuromodulation**: From passive EEG to personalized click-free binaural beats.
  - *Future Roadmap*:
    - Hardware fabrication of dry-contact textile headband.
    - Real-time mobile edge deployment (iOS/Android).
    - Longitudinal clinical trials measuring evoked potential habituation and headache frequency reduction.
  - *Closing*: Thank You | Q&A Session

#### Spoken Script (Speaker 5 — 60 seconds):
> "To conclude, this Final Year Design Project successfully demonstrates a complete proof-of-concept for a closed-loop digital therapeutic:
> 
> We proved that an ultra-minimal, single-channel montage can achieve 93.75% diagnostic accuracy; we solved the spectrogram inversion problem to extract patient biomarkers without transmitting raw files; and we engineered an automated engine that synthesizes personalized, click-free acoustic medicine.
> 
> Moving forward, our roadmap includes physical PCB fabrication of a dry-sensor headband and conducting formal clinical trials in collaboration with neurology clinics to quantify attack reduction.
> 
> We would like to express our deepest gratitude to our project supervisor, the defense committee, and the faculty of United International University for their guidance. 
> 
> We are now ready to take your questions. Thank you very much."

---

## Defense Q&A Quick-Reference Guide (For All Members)

| Expected Board Question | Key Technical Concept to Answer | Best Responding Speaker |
| :--- | :--- | :--- |
| **"Why did you choose Channel #80 instead of frontal channels?"** | Channel #80 corresponds to Oz/O1 over the occipital visual cortex. The occipital lobe is the primary seat of alpha rhythm generation and migraine visual hyperexcitability. | Speaker 2 (Prince) |
| **"How can you prove the colormap inversion doesn't distort the frequencies?"** | We validated the inverted spectra against ground-truth numerical Welch PSDs, obtaining an $R^2 > 0.998$ correlation and exact preservation of the alpha peak location. | Speaker 3 (Anisa) |
| **"Why carrier frequency 216 Hz instead of 440 Hz?"** | Phase-locking in the superior olivary complex degrades above 1.5 kHz and is strongest at low frequencies; 216 Hz is close to musical pitch A3, providing warm, non-irritating timbre for phonophobic patients. | Speaker 4 (Jarin) |
| **"Isn't 93.75% accuracy lower than Aslan (2023)'s 100%?"** | Aslan used all 128 channels with heavy computation for offline diagnosis only. We achieved 93.75% using just **one single channel** and extended the system to closed-loop therapy. | Speaker 1 (Abu Hurayra) |
| **"How does this satisfy Washington Accord P2 (Conflicting Requirements)?"** | High clinical accuracy requires 128 wet gel electrodes, but wearable usability requires 1 dry electrode. Balancing this trade-off without catastrophic loss of accuracy is a quintessential complex engineering problem. | Speaker 5 (Mashrafe) |
