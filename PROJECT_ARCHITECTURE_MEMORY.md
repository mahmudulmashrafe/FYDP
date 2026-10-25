# Project Memory: Closed-Loop Wearable EEG & Spectrogram-Driven Binaural Beat Neuromodulation for Migraine

## 1. Project Identity & Context
- **Title**: A Closed-Loop Wearable EEG Framework for Real-Time Migraine Mitigation via Binaural Beat Entrainment
- **Academic Context**: Final Year Design Project (FYDP-III), Department of Computer Science and Engineering, United International University (UIU).
- **Date**: Academic Year 2025–2026 (Graduation / Submission June 11, 2026).
- **Authors**:
  - Abu Hurayra Mahbe (0112230043)
  - Md. Shakibul Hassan Prince (0112230048)
  - Jarin Tabassum (0112230836)
  - Anisa Azmi (0112230292)
  - Mahmudul Mashrafe (0112230115)
- **Supervision**: Dr. Jannatun Noor Mukta (Supervisor), RA Md Abu Obaida Zishan (Class Teacher / Lab), Dr. Hasan Sarwar (Department Head / Advisor).

---

## 2. Research Problem & Clinical Motivation
- **Clinical Condition**: Migraine is a major neurovascular disorder affecting ~15% of the global population, ranked among the leading global causes of years lived with disability (YLD). Current pharmacological treatments suffer from side effects, medication overuse headaches (MOH), and incomplete efficacy.
- **Electrophysiological Underpinnings**:
  - **Thalamocortical Dysrhythmia (TCD)**: Interictal dysregulation between the thalamus and cortex leading to altered low-frequency (theta) burst firing and pervasive suppression of posterior alpha rhythms (8–13 Hz).
  - **Cortical Hyperexcitability & Sensory Gating**: Lack of habituation to sensory stimuli, hypersensitivity in visual and auditory cortices.
- **The Core Clinical Hypothesis**:
  1. *Detection*: Time-frequency spectrogram images derived from scalp EEG (specifically occipital/visual cortex Channel #80) capture distinct signatures of interictal cortical hyperexcitability and can be reliably classified into Migraine vs. Healthy Control using deep convolutional neural networks.
  2. *Mitigation*: Migraineurs exhibit an **Individual Alpha Frequency (IAF)** deficit and elevated Theta-to-Alpha Ratio (TAR). Delivering non-invasive, patient-tailored **binaural beats** tuned precisely to the patient's extracted IAF (within 8–13 Hz) at a carrier frequency of 216 Hz promotes auditory brainwave entrainment, restoring alpha power and mitigating cortical hyperexcitability.

---

## 3. Core Data Architecture: Carnegie Mellon University (CMU) Repository
- **Reference**: Chamanzar, Haigh, Grover, Behrmann (2021), *Brain Communications*, doi:10.1093/braincomms/fcab061.
- **Acquisition Hardware**: BioSemi ActiveTwo 128-channel ultra-high-density cap + external electrodes (144 total recorded channels in `.bdf` format) sampled at 512 Hz or 2048 Hz (downsampled for processing).
- **Cohort Composition**:
  - **Migraine Patients (M)**: 18 recorded (M1–M18); 12 females, 5 males; mean age ~27.2 years (range 19–54); 12 with aura, 6 without aura.
  - **Healthy Controls (C)**: 18 matched controls (C1, C3–C5, C7–C11, C13–C21) + 4 additional (C2, C6, C12, P15); matched for age and gender.
- **Experimental Conditions**:
  1. **Resting State (`*Resting*.bdf`)**: Eyes open/closed spontaneous baseline EEG.
  2. **Steady-State Auditory Evoked Potentials (`*SSAEP*.bdf`)**: 4 Hz and 6 Hz modulated tone stimuli assessing auditory sensory processing.
  3. **Steady-State Visual Evoked Potentials (`*SSVEP*.bdf`)**: 4 Hz and 6 Hz vertical grating patterns testing visual cortical excitability.
- **Generated Spectrogram Repository**:
  - Total: **106 high-resolution PNG spectrogram images** (6000 x 2400 pixels original, Viridis colormap, 1.0–50.0 Hz).
  - 67 Control images, 39 Migraine images across Resting, SSAEP, and SSVEP.

---

## 4. End-to-End Pipeline & Notebook Map

```
Raw BioSemi .bdf Files (144 channels)
       │
       ▼ [1_EEG_CMU.ipynb]
MNE Signal Preprocessing:
  - Select 128 scalp channels
  - Common Average Reference (CAR)
  - Bandpass Filter (1.0–50.0 Hz)
  - Notch Filter (60.0 Hz line noise)
  - Select Occipital/Visual Channel #80
  - Short-Time Fourier Transform (STFT)
       │
       ▼
Rendered STFT Spectrograms (Viridis Colormap, [-10, +30] dB)
       │
       ├─────────────────────────────────────────┐
       ▼ [Notebooks 2, 3, 4]                     ▼ [Notebook 5]
CNN Transfer Learning Classification:      Spectrogram Inversion & Audio Neuromodulation:
  - VGG16 (Accuracy: 90.63%, MCC: 0.798)     - 256-color Viridis LUT minimum Euclidean distance
  - ResNet50 (Accuracy: 87.50%, MCC: 0.741)  - Reconstruct calibrated decibels [-10, +30] dB
  - EfficientNetB7 (Accuracy: 93.75%, MCC: 0.875) - Convert to linear power (uV^2/Hz)
                                             - Integrate PSD profile across 1.0–50.0 Hz
                                             - Localize Individual Alpha Frequency (IAF)
                                             - Quantify Alpha Deficit & TAR (Theta-to-Alpha)
                                             - Synthesize dichotic pure-tone binaural beats:
                                               * Left: fc - f_beat/2
                                               * Right: fc + f_beat/2 (fc = 216 Hz)
                                               * Squared half-cosine anti-click fade envelope
                                               * 16-bit 44.1 kHz stereo PCM WAV export
```

---

## 5. Machine Learning Benchmarks (Notebooks 2–4)
- **Input Dimensions**: Resized to 224x224x3 (or 256x256x3) with `[0, 1]` rescaling.
- **Training Strategy**: Transfer learning from ImageNet pre-trained backbones with frozen base layers, average pooling, Dense(128, ReLU), Dropout, and Dense(2, Softmax).
- **Optimization**: Adam optimizer ($\text{lr} = 10^{-4}$), Sparse Categorical Crossentropy, ModelCheckpoint callback.
- **Empirical Results**:
  | Model Architecture | Accuracy | Weighted Precision | Weighted Recall | Weighted F1 | Matthews Corr. Coeff. (MCC) |
  | :--- | :---: | :---: | :---: | :---: | :---: |
  | **VGG16** | 90.63% | 0.9099 | 0.9063 | 0.9071 | 0.7985 |
  | **ResNet50** | 87.50% | 0.8861 | 0.8750 | 0.8771 | 0.7410 |
  | **EfficientNetB7** | **93.75%** | **0.9471** | **0.9375** | **0.9385** | **0.8750** |

---

## 6. Spectrogram Inversion & Audio Prescription Engine (Notebook 5)
- **Colormap Lookup Table (LUT)**: 256-entry RGB Viridis array.
- **Pixel Inversion**:
  $$\hat{i}(y, t) = \frac{1}{255} \arg\min_{k \in \{0, \dots, 255\}} \| p(y, t) - \text{LUT}_{\text{viridis}}(k) \|_2^2$$
  $$S_{\text{dB}}(y, t) = P_{\min} + \hat{i}(y, t) \cdot (P_{\max} - P_{\min}) = -10 + 40 \cdot \hat{i}(y, t)$$
  $$P(y, t) = 10^{S_{\text{dB}}(y, t) / 10}$$
- **Time-Averaged Power Spectral Density (PSD)**:
  $$\overline{P}(y) = \frac{1}{T} \sum_{t=1}^T P(y, t)$$
- **Canonical Bands**:
  - Delta: 1.0–4.0 Hz
  - Theta: 4.0–8.0 Hz
  - Alpha: 8.0–13.0 Hz
  - Beta: 13.0–30.0 Hz
  - Gamma: 30.0–50.0 Hz
- **Individual Alpha Frequency (IAF)**:
  $$\text{IAF} = \arg\max_{f \in [8, 13]} \overline{P}(f)$$
- **Theta-to-Alpha Ratio (TAR)**:
  $$\text{TAR} = \frac{P_{\text{Theta}}}{P_{\text{Alpha}}}$$
- **Alpha Deficit**:
  $$\Delta_{\text{Alpha}} = \max\left(0, 0.20 - \frac{P_{\text{Alpha}}}{P_{\text{Total}}}\right)$$
- **Cohort Analytics (Resting State)**:
  - **Migraine Cohort ($n=12$)**: Mean IAF = $9.12 \pm 0.80$ Hz; Alpha Power = $9.41 \pm 5.03\%$; TAR = $1.64 \pm 0.38$; Theta Power = $15.47 \pm 8.48\%$.
  - **Control Cohort ($n=22$)**: Mean IAF = $8.86 \pm 1.18$ Hz; Alpha Power = $7.60 \pm 3.32\%$; TAR = $1.77 \pm 0.35$; Theta Power = $13.17 \pm 5.93\%$.
  - **Exemplar Patient M10**: IAF = 10.09 Hz, Alpha Power = 12.12%, Alpha Deficit = 7.88%, TAR = 1.64. Synthesized prescription: $f_{\text{left}} = 210.955$ Hz, $f_{\text{right}} = 221.045$ Hz ($f_c = 216.0$ Hz), 16-bit 44.1 kHz stereo WAV.

---

## 7. Comprehensive Literature Grounding (2023–2026)
- **Direct CMU Dataset Baselines**:
  - *Chamanzar et al. (2021)*: Original CMU ultra-high-density study identifying altered phase-locking and coherence abnormalities.
  - *Orhanbulucu, Latifoglu & Baydemir (2023)*: Diagnostics; STFT and CWT time-frequency images classified with AlexNet, ResNet50, and SqueezeNet (94.7% accuracy).
  - *Aslan (2023)*: Circuits, Systems, and Signal Processing; CWT scalograms + CNN with Grad-CAM interpretability (100% on CMU).
- **Clinical Migraine Neuromarkers & DL**:
  - *Alsabea et al. (2024)*: IEEE ICEET; PSD features with CNN/DNN (97% accuracy).
  - *Sebastianelli et al. (2025)*: J. Headache & Pain; Somatosensory evoked potentials with ANN.
  - *Hsiao et al. (2024)*: J. Headache & Pain; Somatosensory evoked EEG with SVM connectivity.
  - *Van den Hoek et al. (2024)*: Brain Sciences; Preictal alterations in theta/alpha power and connectivity.
  - *Kim et al. (2023)*: QEEG biomarkers in 720 migraineurs.
- **Binaural Beat Entrainment & Neuromodulation**:
  - *Oster (1973)*: Foundational biophysical theory of auditory beats and superior olivary complex processing.
  - *Wahbeh et al. (2007)*: Binaural beat technology in EEG entrainment and anxiety.
  - *Melnichuk et al. (2025)*: CPT EEG entrainment with beta and gamma beats.
  - *Kahathuduwa et al. (2025)*: Physiologia; Real-time EEG-guided binaural beat audio for relaxation and cognition.
  - *Shamsi et al. (2024)*: Systematic review of binaural beats in clinical pain management.
  - *Hamid et al. (2025)*: AIMS Neuroscience; Distinct neural mechanisms of alpha binaural beats vs white noise.
- **Wearable BCI & Digital Phenotyping**:
  - *Petrušić (2025)*: Cephalalgia; Digital phenotyping for migraine.
  - *He et al. (2023)*: State-of-the-art wearable and wireless EEG systems survey.
  - *Muhammad et al. (2023)*: Low-cost wearable EEG headsets.
  - *Danelakis et al. (2025)*: Narrative review of AI and wearables in headache disorders.

---

## 8. Engineering Standards & Realistic Constraints
- **Electrode Montages**: International 10–20, 10–10, and 10–5 systems; BioSemi 128-channel radial coordinates.
- **Acoustic Safety**: OSHA (85 dBA 8-hr TWA), NIOSH (85 dBA recommended exposure limit), WHO guidelines on safe listening devices.
- **Data & Clinical Formats**: Brain Imaging Data Structure (BIDS), EDF/BDF standard specifications, HIPAA / GDPR data privacy principles.
