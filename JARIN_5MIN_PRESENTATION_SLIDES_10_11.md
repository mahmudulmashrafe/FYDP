# Final Defense Presentation Guide & Spoken Script (5-Minute Extended)
## Slides 10 & 11: Patient-Specific Biomarker Extraction & Binaural Audio Synthesis
**Speaker**: Jarin Tabassum (0112230836)  
**Total Allocated Duration**: Exactly 5 Minutes (~600–650 Words at a Steady, Confident 120–130 WPM)  
**Assigned Slides**: 
- **Slide 10**: Patient-Specific Neuro-Biomarker Extraction (IAF, Alpha Deficit, TAR) — *[0:00 – 2:30]*
- **Slide 11**: Closed-Loop Dichotic Binaural Beat Audio Synthesis Engine — *[2:30 – 5:00]*

---

## Strategic Presentation Architecture (5-Minute Breakdown)
```
[Minute 0:00 - 0:30] Introduction & Bridge: Connecting Anisa's Inversion to Clinical Biomarkers
[Minute 0:30 - 1:30] Slide 10: Deep Dive into IAF Peak Mathematical Detection & The "Why"
[Minute 1:30 - 2:30] Slide 10: Alpha Deficit, Relative Power Integrals & Elevated TAR (TCD Confirmation)
[Minute 2:30 - 3:30] Slide 11: Dichotic Stereo Synthesis Math & Psychoacoustics of the 216 Hz Carrier
[Minute 3:30 - 4:30] Slide 11: Anti-Click Fade Envelope Engineering (1.5s Squared Half-Cosine) & SPL Safety
[Minute 4:30 - 5:00] Summary & Transition to Speaker 5 (Mashrafe / Results & Standards)
```

---

# PART 1: SLIDE CONTENT (For PowerPoint / Visual Presentation)

### Slide 10: Patient-Specific Neuro-Biomarker Extraction
- **Slide Title**: Patient-Specific Neuro-Biomarker Extraction & Quantitation
- **Subtitle**: Decoding Thalamocortical Dysrhythmia via Continuous Spectral Inversion
- **Visual Layout (3 Cards + Spectral Curve)**:
  - **Card 1: Individual Alpha Frequency (IAF)**:
    $$\text{IAF} = \arg\max_{f \in [8.0, 13.0]} P_{\text{linear}}(f)$$
    - Scans narrow-band linear power $P(f)$ ($\mu\text{V}^2/\text{Hz}$) across 8.0–13.0 Hz.
    - Captures the patient's biological resonant frequency (e.g., M10 = **9.87 Hz**).
  - **Card 2: Relative Alpha Power & Alpha Deficit**:
    $$P_{\alpha}^{\text{rel}} = \frac{\int_{8}^{13} P(f)df}{\int_{1}^{50} P(f)df} \times 100\%, \quad \Delta P_\alpha = P_{\alpha,\text{normative}}^{\text{rel}} - P_{\alpha,\text{patient}}^{\text{rel}}$$
    - Directly quantifies the loss of inhibitory alpha oscillations.
  - **Card 3: Theta-to-Alpha Ratio (TAR)**:
    $$\text{TAR} = \frac{P_\theta^{\text{rel}}}{P_\alpha^{\text{rel}}} = \frac{\int_{4}^{8} P(f)df}{\int_{8}^{13} P(f)df}$$
    - Diagnostic Threshold: $\text{TAR} > 1.2$ confirms cortical hyperexcitability and TCD.
- **Center Graphic**: Annotated power spectrum plot showing patient M10's prominent 9.87 Hz alpha peak versus depressed broadband power.

---

### Slide 11: Closed-Loop Binaural Audio Synthesis Engine
- **Slide Title**: Closed-Loop Binaural Audio Synthesis & Psychoacoustic Engineering
- **Subtitle**: Click-Free Dichotic Entrainment Modulated to Patient-Specific IAF
- **Visual Layout (2 Column Split + Waveform Display)**:
  - **Column 1: Dichotic Waveform Generation**:
    $$s_{\text{left}}(t) = A \cdot \sin\left(2\pi \left(f_c - \frac{\text{IAF}}{2}\right) t\right), \quad s_{\text{right}}(t) = A \cdot \sin\left(2\pi \left(f_c + \frac{\text{IAF}}{2}\right) t\right)$$
    - **Carrier Frequency ($f_c = 216.0$ Hz)**:
      - Optimal phase-locking in Medial Superior Olive ($<1.5$ kHz).
      - Proximity to concert pitch A3 (220 Hz) yields soothing, warm cello timbre.
    - **Interaural Beat Differential**: $\Delta f = |f_{\text{right}} - f_{\text{left}}| = \text{IAF}$ (Exact biological tuning).
  - **Column 2: Anti-Click Fade Envelope & Calibrated Export**:
    $$E[n] = \sin^2\left(\frac{\pi n}{2 N_{\text{fade}}}\right) \quad \text{for } 0 \le n < N_{\text{fade}} \quad (T_{\text{fade}} = 1.5\text{ s})$$
    - Eliminates high-frequency transient switching clicks for phonophobic patients.
    - **Audio Format**: 16-bit signed PCM uncompressed stereo WAV ($f_s = 44,100$ Hz).
    - **Acoustic Bounding**: Calibrated strictly to 60–65 dB SPL (well below WHO/OSHA 85 dBA limits).

---

# PART 2: WORD-FOR-WORD 5-MINUTE SPOKEN DEFENSE SCRIPT

> *(Stage Directions: Stand upright, face the examination committee with confidence. Smile, take the clicker from Anisa, take a two-second pause to settle the room, and begin in a clear, resonant voice.)*

---

### Minute 0:00 – 1:00 | The Transition & Individual Alpha Frequency (IAF)
"Thank you, Anisa. 

Honorable members of the defense board, respected supervisor, and faculty members—I am **Jarin Tabassum**. 

Up to this point, my teammates have demonstrated how we clean raw single-channel EEG, classify interictal migraine states with 93.75% accuracy, and mathematically invert 2D spectrogram images back into continuous linear power spectral densities. 

Now, we arrive at the pivotal clinical bridge of our project: **How do we turn those mathematical power curves into actionable neurological biomarkers, and how do we translate those biomarkers into personalized acoustic medicine?**

Please direct your attention to **Slide 10**. 

Once our colormap inversion reconstructs the continuous power spectrum $P(f)$ in microvolts squared per Hertz, our biomarker engine immediately interrogates the alpha band between **8.0 and 13.0 Hertz**. 

As shown in our first formulation, the engine computes:
$$\text{IAF} = \arg\max_{f \in [8.0, 13.0]} P_{\text{linear}}(f)$$

This identifies the patient’s **Individual Alpha Frequency**, or **IAF**. 

Why is this step so critical? In traditional commercial relaxation apps or older clinical studies, researchers delivered a generic, fixed 10 Hertz binaural beat to every patient. But in clinical neuroscience, we know that every human brain has a genetically and structurally unique alpha peak—some patients resonate at 9.2 Hertz, others at 10.1, and others at 11.0. 

If you stimulate a patient even 0.5 Hertz away from their natural peak, you cause destructive phase cancellation instead of therapeutic entrainment. By isolating the exact mathematical argmax, our system guarantees that the incoming therapeutic stimulus will match the patient’s endogenous thalamocortical resonance with surgical precision."

---

### Minute 1:00 – 2:30 | Relative Power, Alpha Deficit & Theta-to-Alpha Ratio (TAR)
"Next, our engine performs numerical integration across the 1.0 to 50.0 Hertz spectrum to compute relative band powers and quantify the patient's pathological state. 

Under normal physiological conditions, the human visual cortex at rest produces a dominant alpha rhythm that inhibits irrelevant sensory noise. In migraineurs, however, low-threshold T-type calcium channels de-inactivate, causing thalamic neurons to fire irregularly in the slower theta range (4.0 to 8.0 Hertz). 

This phenomenon produces two key biomarkers:
First, the **Alpha Deficit**, calculated as:
$$\Delta P_\alpha = P_{\alpha,\text{normative}}^{\text{rel}} - P_{\alpha,\text{patient}}^{\text{rel}}$$
This metric directly quantifies how much protective alpha power the patient has lost compared to healthy baseline controls.

Second, we formulate the **Theta-to-Alpha Ratio**, or **TAR**:
$$\text{TAR} = \frac{P_\theta^{\text{rel}}}{P_\alpha^{\text{rel}}} = \frac{\int_{4}^{8} P(f)df}{\int_{8}^{13} P(f)df}$$

In healthy controls, alpha power heavily dominates over theta, maintaining a low TAR—typically between 0.7 and 0.9. But in migraineurs during the interictal state, as cortical hyperexcitability takes over, theta power rises and alpha collapses, driving the TAR well above 1.2. 

In our single-subject validation of patient **M10**, for example, our engine detected an IAF peak of **9.87 Hertz**, an Alpha Deficit of **$-1.24\,\mu\text{V}^2/\text{Hz}$**, and an abnormally elevated TAR of **1.48**. 

This gives our framework complete diagnostic transparency: we are not just handing down an AI prediction; we are presenting verifiable, physical electrophysiological biomarkers that explain *why* the patient is suffering from thalamocortical dysrhythmia."

---

> *(Action: Press the clicker to advance to Slide 11. Point to the dichotic synthesis equations and waveform.)*

---

### Minute 2:30 – 3:45 | Closed-Loop Dichotic Synthesis & The 216 Hz Carrier
"Now, let us examine **Slide 11**, which details our **Closed-Loop Binaural Audio Synthesis Engine**. 

Once the patient’s IAF is extracted, our system does not rely on pre-recorded audio files. Instead, it dynamically synthesizes a brand-new, customized dichotic stereo prescription from pure mathematical sine waves in real time.

As shown in our synthesis equations:
$$s_{\text{left}}(t) = A \cdot \sin\left(2\pi \left(f_c - \frac{\text{IAF}}{2}\right) t\right), \quad s_{\text{right}}(t) = A \cdot \sin\left(2\pi \left(f_c + \frac{\text{IAF}}{2}\right) t\right)$$

Notice our carrier frequency: **$f_c = 216.0$ Hertz**. 
The selection of 216 Hertz is one of the most deliberate psychoacoustic engineering decisions in our project, founded upon two physiological principles:

1. **Superior Olivary Phase-Locking:** The brainstem nucleus responsible for detecting interaural phase differences—the Medial Superior Olive—can only phase-lock to acoustic timing cues at low carrier frequencies, specifically below 1.5 kilohertz. If you use a carrier frequency above 1 kilohertz, the brain cannot resolve the phase delay, and the perception of a binaural beat completely vanishes.
2. **Timbre and Phonophobia Tolerance:** Migraine patients suffer from acute sound sensitivity, known as phonophobia. Conventional high-pitched test frequencies, like 440 Hertz or 1000 Hertz, sound piercing and trigger severe auditory discomfort. By contrast, 216 Hertz sits just below concert pitch A3 (220 Hertz), producing a deep, warm, soothing cello-like drone that is pleasant and therapeutic to listen to.

By splitting the beat symmetrically—subtracting half the IAF from the left ear and adding half the IAF to the right ear—the auditory pathways perceive an illusionary third rhythm pulsing at precisely $\Delta f = \text{IAF}$."

---

### Minute 3:45 – 4:40 | The Anti-Click Fade Envelope & Calibrated Acoustic Safety
"However, synthesizing pure sine waves introduces a severe real-world engineering challenge: **Acoustic Switching Transients**.

When a digital pure tone begins or terminates abruptly, the instantaneous step discontinuity in the speaker diaphragm produces high-frequency harmonic splatter—a sharp, mechanical 'click' or 'pop'. To an individual in a fragile, pre-headache state, such a click can trigger an acoustic startle reflex, causing immediate muscle tensing and worsening the headache.

To eliminate this artifact entirely, we engineered an **Anti-Click Fade Envelope** $E[n]$ using a squared half-cosine taper over a duration of $T_{\text{fade}} = 1.5$ seconds:
$$E[n] = \sin^2\left(\frac{\pi n}{2 N_{\text{fade}}}\right) \quad \text{for } 0 \le n < N_{\text{fade}}$$

The first derivative of the $\sin^2$ function is zero at $t = 0$. This guarantees that both the amplitude and the rate of change of amplitude rise from zero with absolute smoothness, completely eradicating transient clicks.

Finally, the synthesized audio is exported as an uncompressed, **16-bit linear PCM stereo WAV file at 44.1 kilohertz**. We specifically avoid MP3 or AAC compression because lossy psychoacoustic compression algorithms discard subtle interaural phase differences. Furthermore, in strict compliance with World Health Organization (WHO) and OSHA safe listening guidelines, our software gain ceiling limits playback volume to **60 to 65 decibels SPL**, protecting patients from cochlear fatigue."

---

### Minute 4:40 – 5:00 | Conclusion of Technical Core & Handover
"In summary, Slides 10 and 11 represent the complete technological realization of our closed loop: we take a passive mathematical spectrogram, extract the patient’s biological alpha peak and dysrhythmia ratio, and immediately synthesize a safe, click-free, personalized acoustic prescription tailored to their brain.

Now, I hand over the presentation to **Mahmudul Mashrafe**, who will present our experimental benchmarking, engineering standards compliance, cost analysis, and Washington Accord complex problem-solving mapping. 

Thank you."

> *(Stage Directions: Smile, nod to the committee, and hand the clicker to Mashrafe.)*

---

# PART 3: VIVA / DEFENSE COMMITTEE Q&A PREPARATION FOR JARIN

If the defense committee or external examiners ask you questions about Slides 10 and 11, here are your **exact, authoritative technical answers**:

### Question 1: "Why do you use the argmax in the 8–13 Hz band? What if there are multiple peaks?"
> **Your Answer**: 
> *"Respected examiner, in healthy and interictal EEG, the alpha rhythm is characterized by a dominant spectral peak reflecting the thalamocortical pacing frequency. In cases where multiple sub-peaks or broadband plateauing occur, taking the global argmax over the filtered 8.0 to 13.0 Hz band isolates the frequency carrying the highest power density. Furthermore, in our full pipeline, we inspect relative alpha power and TAR to ensure that the detected peak is physiologically prominent before generating the audio."*

### Question 2: "Why did you choose 216 Hz for the carrier frequency instead of 100 Hz or 440 Hz?"
> **Your Answer**: 
> *"There are two reasons, sir. First, physiologically, the Medial Superior Olive (MSO) performs interaural phase delay processing only below 1.5 kHz, and literature (such as Battù et al., 2025 and Wahbeh et al., 2007) shows that beat perception diminishes as the carrier approaches 1 kHz. Second, psychoacoustically, very low carriers like 100 Hz require high acoustic power to be perceived and can cause rumbling, while 440 Hz is shrill and irritating for phonophobic migraineurs. 216 Hz sits right beside musical concert pitch A3 (220 Hz), giving a soothing, cello-like acoustic timbre that promotes relaxation and compliance."*

### Question 3: "Why is the fade envelope 1.5 seconds, and why squared half-cosine ($\sin^2$) instead of a simple linear ramp?"
> **Your Answer**: 
> *"A linear ramp has a non-zero slope at sample zero, which causes a sharp corner in the waveform, still generating high-frequency spectral leakage. The squared half-cosine ($\sin^2$) function has a first derivative of zero at both onset ($t=0$) and full amplitude ($t=1.5\text{s}$). This guarantees continuous first-order smoothness ($C^1$ continuity), completely suppressing switching clicks. We chose 1.5 seconds because psychoacoustic studies show that migraineurs require a gradual sensory adaptation period to prevent startle responses."*

### Question 4: "Why export as WAV instead of MP3?"
> **Your Answer**: 
> *"Binaural beats rely entirely on the brain detecting microsecond phase differences between the left and right ear. Lossy compression formats like MP3 use perceptual coding that discards phase information and high-frequency resolution to save file size, which can degrade or destroy the interaural phase cue. An uncompressed 16-bit 44.1 kHz PCM WAV file preserves 100% of the mathematical phase relationships."*
