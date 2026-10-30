# Final Year Design Project (FYDP) Defense — Spoken Speech Scripts
## A Closed-Loop Wearable EEG Framework for Migraine Mitigation via Binaural Beat Entrainment
**Institution**: United International University (UIU)  
**Department**: Computer Science and Engineering  
**Total Defense Time**: Strictly 15 Minutes (3 Minutes per Member)  
**Team Roster**:
1. **Speaker 1**: Abu Hurayra Mahbe (0112230043) — *Slides 1 to 3 [0:00 – 3:00]*
2. **Speaker 2**: Md. Shakibul Hassan Prince (0112230048) — *Slides 4 to 6 [3:00 – 6:00]*
3. **Speaker 3**: Anisa Azmi (0112230292) — *Slides 7 to 9 [6:00 – 9:00]*
4. **Speaker 4**: Jarin Tabassum (0112230836) — *Slides 10 to 12 [9:00 – 12:00]*
5. **Speaker 5**: Mahmudul Mashrafe (0112230115) — *Slides 13 to 15 [12:00 – 15:00]*

---

## Defense Rules & Presentation Tips
- **Pacing**: Aim for **120–130 words per minute**. Each 60-second block is ~120 to 140 words.
- **Stage Presence**: Stand upright, make eye contact with all committee members, not just the supervisor. Avoid reading directly from slides; use the slides as visual anchors.
- **Handover Transitions**: Deliver the handover line clearly and pause for 2 seconds while the next speaker steps forward and takes the presentation clicker.

---

# SPEAKER 1: Abu Hurayra Mahbe (0112230043)
**Assigned Time**: 0:00 to 3:00 (3 Minutes Total)  
**Assigned Slides**: Slides 1, 2, and 3  
**Role**: Opening, Clinical Motivation, Neurophysiological Pathology, and Project Architecture

---

### Slide 1: Title & Project Overview (Minute 0:00 – 1:00)
> *(Action: Stand center stage, smile, maintain direct eye contact with the defense panel.)*

"Honorable members of the defense board, respected internal and external examiners, supervisor, and faculty members—a very warm good morning. 

I am **Abu Hurayra Mahbe**, and on behalf of our team, it is my privilege to present our Final Year Design Project: **A Closed-Loop Wearable EEG Framework for Real-Time Migraine Mitigation via Binaural Beat Entrainment**.

Migraine is far more than an ordinary headache. It is an excruciating neurological disorder afflicting over one billion people worldwide, recognized by the World Health Organization as the second leading cause of years lived with disability globally. 

Today, patients rely almost exclusively on pharmacological remedies such as triptans and NSAIDs. Yet, over 40% of patients report inadequate relief, severe cardiovascular contraindications, or secondary medication-overuse headaches, leading to chronic patient drop-out.

Our goal in this project is to pioneer a non-pharmacological, closed-loop digital therapeutic: an integrated system capable of detecting migraine in its silent interictal state from a single wearable EEG electrode, mathematically decoding the patient’s exact neurological deficit, and immediately synthesizing an individualized acoustic sound track to restore brainwave equilibrium."

---

### Slide 2: Neurophysiology & The Clinical Problem (Minute 1:00 – 2:00)
> *(Action: Point to the contrast between the Left Pathology column and the Right Bio-Acoustic mechanism.)*

"To build an effective engineering solution, we must examine the neurobiology of the migraine brain between attacks—the interictal phase.

Clinically, migraine is driven by **Thalamocortical Dysrhythmia** and cortical hyperexcitability. In a healthy brain, alpha oscillations between 8 and 13 Hertz act as a sensory filter, inhibiting extraneous neural noise. In migraine patients, this protective alpha rhythm collapses, producing a distinct **Alpha Deficit** and an abnormally elevated Theta-to-Alpha Ratio.

This is where **acoustic neuromodulation** offers an elegant non-invasive pathway. When two pure sine tones with a slight frequency difference are delivered dichotically to each ear, the brainstem’s **Superior Olivary Complex** calculates the phase discrepancy and perceives a rhythmic third beat—a **Binaural Beat**. Through the **Auditory Steady-State Response**, cortical firing synchronizes with this beat frequency.

However, existing commercial sound apps fail because they deliver generic 10 Hz tones to everyone. In reality, each individual has a unique, genetically determined alpha peak frequency. Our closed-loop system overcomes this limitation by calibrating the acoustic stimulus to each patient’s unique brainwave signature."

---

### Slide 3: Scope & End-to-End System Architecture (Minute 2:00 – 3:00)
> *(Action: Trace the 5-stage flowchart across the slide.)*

"To realize this closed loop, we architected a modular 5-stage engineering pipeline:

First, we condition multi-channel EEG using Common Average Referencing, zero-phase Butterworth bandpass filtering, and 60 Hz notch filtering.

Second, we isolate **occipital Channel #80** and compute Short-Time Fourier Transforms using a 256-point Hamming window to generate standardized 2D Viridis time-frequency spectrograms.

Third, we pass these spectrograms into pre-trained deep convolutional neural networks to perform automated interictal migraine detection.

Fourth, we introduce a novel mathematical colormap inversion algorithm that reverse-engineers continuous power spectral density curves directly from 2D RGB images without requiring raw voltage timeseries.

Fifth, our audio engine extracts the patient's Individual Alpha Frequency and synthesizes a high-fidelity, click-free stereo binaural beat track calibrated for safe clinical listening.

Now, I invite my teammate **Md. Shakibul Hassan Prince** to present our literature review, research gaps, and signal processing methodology."

> *(Transition: Hand over the clicker to Shakibul, take a step back.)*

---

# SPEAKER 2: Md. Shakibul Hassan Prince (0112230048)
**Assigned Time**: 3:00 to 6:00 (3 Minutes Total)  
**Assigned Slides**: Slides 4, 5, and 6  
**Role**: Literature Benchmarking, Research Gaps, Dataset, and Preprocessing Engineering

---

### Slide 4: State of the Art & Research Gaps (Minute 3:00 – 4:00)
> *(Action: Step forward, acknowledge the board, and direct attention to the comparative literature matrix.)*

"Thank you, Abu Hurayra. Respected committee members, I am **Md. Shakibul Hassan Prince**.

In our survey of over 50 contemporary peer-reviewed studies published between 2021 and 2025, we observed a fundamental disconnect in existing literature.

On one side, state-of-the-art deep learning research—such as Orhanbulucu et al. (2023) and Aslan (2023)—demonstrated impressive diagnostic accuracy between 94% and 100%. However, these methods relied on cumbersome 128-channel wet electrode caps that take 45 minutes to set up, cost upwards of \$25,000, and operate strictly as offline diagnostic tools with zero therapeutic capability.

On the other side, clinical neuro-acoustic trials—such as Alonso et al. (2024) and Battù et al. (2025)—confirmed that binaural beats induce alpha-band cortical entrainment. Yet, these studies operated in an open loop, administering static, generic tones without automated diagnostic intelligence.

The critical research gap was unmistakable: **No published work had successfully bridged single-channel automated screening with patient-tailored, closed-loop acoustic entrainment.** Addressing this exact bottleneck is the primary objective of our work."

---

### Slide 5: Dataset & Preprocessing Pipeline (Minute 4:00 – 5:00)
> *(Action: Explain the mathematical significance of zero-phase filtering and CAR.)*

"To validate our framework on gold-standard data, we utilized the Carnegie Mellon University Ultra-High-Density EEG dataset, recorded via a clinical 128-channel BioSemi ActiveTwo system across migraineurs and matched controls.

Raw EEG voltage potentials are microscopic—typically between 10 and 100 microvolts—making them highly vulnerable to muscle artifacts, ocular drift, and electrical mains interference. We implemented a rigorous three-step signal conditioning pipeline:

First, **Common Average Referencing (CAR)** subtracts the instantaneous spatial mean across all electrodes, removing widespread common-mode noise.

Second, a **zero-phase 4th-order Butterworth bandpass filter** restricts bandwidth to 1.0 through 50.0 Hertz. Crucially, the forward-backward zero-phase implementation eliminates phase distortion, ensuring that the temporal dynamics of neural oscillations remain physiologically truthful.

Third, a **60 Hz notch filter** erases North American power-line interference. This leaves an impeccably conditioned cerebral signal ready for transformation."

---

### Slide 6: Channel #80 Localization & STFT Spectrograms (Minute 5:00 – 6:00)
> *(Action: Point to the occipital region on the 10-20 head diagram and the generated Viridis spectrogram.)*

"A core design constraint of consumer neurotechnology is channel minimalism: a user cannot wear 128 electrodes at home or in the office.

By analyzing the underlying neurophysiology, we isolated **Channel #80**, positioned precisely at the Oz/O1 boundary over the primary visual cortex. The occipital lobe is the physiological generator of the human alpha rhythm and the primary source of migraine visual auras and photophobia.

We segmented Channel #80 into epochs and computed the **Short-Time Fourier Transform (STFT)** using a 256-sample Hamming window with 50% overlap. 

The resulting time-frequency representation was mapped onto the **Viridis colormap**, spanning a normalized dynamic range of $-10$ to $+30$ decibels, and exported as a standardized $224 \times 224$ RGB image.

Now, my teammate **Anisa Azmi** will explain how we classify these representations and how we solved the mathematical challenge of spectrogram inversion."

> *(Transition: Hand over the clicker to Anisa, step back.)*

---

# SPEAKER 3: Anisa Azmi (0112230292)
**Assigned Time**: 6:00 to 9:00 (3 Minutes Total)  
**Assigned Slides**: Slides 7, 8, and 9  
**Role**: Deep Transfer Learning, The Black-Box Problem, and Mathematical Inversion Formulation

---

### Slide 7: Deep Transfer Learning Classification (Minute 6:00 – 7:00)
> *(Action: Step forward, address the examiners, and reference the model comparison diagram.)*

"Thank you, Shakibul. Respected examiners, I am **Anisa Azmi**.

Instead of relying on fragile, handcrafted spectral features that vary widely across individuals, we framed interictal migraine detection as a computer vision classification task performed on our STFT spectrogram images.

We benchmarked three prominent deep transfer learning architectures pre-trained on ImageNet: **VGG16**, **ResNet50**, and **EfficientNetB7**. ImageNet pre-training equips the convolutional kernels with generalized feature detectors—such as harmonic bands, edges, and energy textures.

We truncated their default heads and integrated a custom classification top consisting of **Global Average Pooling**, a **Dropout layer of 0.5** for regularization, and a **Softmax binary dense layer**.

Training was executed using the **Adam optimizer** with a fine-tuning learning rate of $10^{-4}$ and categorical cross-entropy loss under stratified splits. As we will reveal in our results, EfficientNetB7’s compound scaling delivered outstanding diagnostic accuracy."

---

### Slide 8: The Engineering Bottleneck: The 'Black-Box' Spectrogram (Minute 7:00 – 8:00)
> *(Action: Emphasize the core mathematical challenge—this is the unique technical contribution of the FYDP.)*

"Now, I would like to highlight the central mathematical innovation of our project.

In decentralized digital healthcare and mobile health systems, transmitting raw multi-channel EEG files over cellular networks is impractical: the files are massive, require uncompressed bandwidth, and introduce severe data privacy vulnerabilities under HIPAA and GDPR.

Consequently, modern systems transmit lightweight 2D spectrogram images. But this introduces a major engineering bottleneck: **Once a spectrogram image is generated, the underlying physical voltage values are lost, quantized into 24-bit RGB pixels.**

To synthesize an individualized therapeutic binaural beat, our audio engine requires the patient’s exact physical power spectrum in microvolts squared per Hertz to identify their alpha peak.

Standard libraries offer no way to reverse this process. We were faced with an inverse problem: **How do we mathematically reconstruct continuous, calibrated linear Power Spectral Density directly from 2D RGB pixels without access to the original raw timeseries?**"

---

### Slide 9: Analytical Colormap Inversion Algorithm (Minute 8:00 – 9:00)
> *(Action: Walk the board through the 3 equations step-by-step; show confidence in the math.)*

"To solve this problem, we formulated an analytical **Minimum Euclidean Distance Lookup Table (LUT) Inversion Algorithm**.

First, we discretize the continuous Viridis color spectrum into 256 normalized 3D RGB reference vectors $\mathbf{c}_k$ in Euclidean space.

Second, for every pixel in the spectrogram, our algorithm calculates the Euclidean distance between the pixel's RGB coordinates and all 256 reference vectors, selecting the index $\hat{k}$ that minimizes this distance:
$$\hat{k}(i, j) = \arg\min_{k} \left\| \mathbf{P}_{\text{RGB}}(i, j) - \mathbf{c}_k \right\|_2$$

Third, using our calibrated dynamic range of $-10$ to $+30$ decibels, we linearly interpolate the decibel power and apply the inverse logarithmic transform:
$$P_{\text{linear}}(f) = 10^{\frac{\text{PSD}_{\text{dB}}(f)}{10}} \quad [\mu\text{V}^2/\text{Hz}]$$

When we validated our inverted power curves against ground-truth numerical Welch transforms, our algorithm achieved a correlation coefficient $R^2$ exceeding **0.998**. We successfully proved that quantized images can be decoded back into exact clinical spectra!

My teammate **Jarin Tabassum** will now explain how we extract biomarkers from these spectra and synthesize the acoustic prescription."

> *(Transition: Hand over the clicker to Jarin, step back.)*

---

# SPEAKER 4: Jarin Tabassum (0112230836)
**Assigned Time**: 9:00 to 12:00 (3 Minutes Total)  
**Assigned Slides**: Slides 10, 11, and 12  
**Role**: Biomarker Quantitation, Audio Synthesis Engineering, and Empirical Benchmarking

---

### Slide 10: Neuro-Biomarker Extraction (Minute 9:00 – 10:00)
> *(Action: Point to the mathematical peak formula and the M10 alpha peak plot.)*

"Thank you, Anisa. Respected members of the board, I am **Jarin Tabassum**.

With continuous power spectral density reconstructed, our biomarker engine scans the alpha band between 8.0 and 13.0 Hertz.

By evaluating the argmax of the power spectrum, the engine isolates the patient’s **Individual Alpha Frequency (IAF)**. Clinical literature confirms that stimulating a patient at their exact endogenous IAF produces vastly stronger entrainment than arbitrary 10 Hz stimulation.

The engine subsequently integrates power across the spectral bands to derive two crucial clinical metrics:
1. The **Alpha Deficit**, measuring the drop in alpha power relative to normative baselines; and
2. The **Theta-to-Alpha Ratio (TAR)**, where elevated values quantify cortical disinhibition.

Together, these metrics serve as objective, quantifiable electrophysiological biomarkers that guide our sound synthesis engine."

---

### Slide 11: Binaural Beat Audio Synthesis Engine (Minute 10:00 – 11:00)
> *(Action: Explain the psychoacoustic rationale of 216 Hz and the anti-click fade envelope.)*

"Once the IAF is determined, our audio synthesis engine dynamically generates a tailored dichotic stereo track.

We selected an ergonomic carrier frequency of **$f_c = 216.0$ Hertz**. This choice is grounded in auditory physiology: first, interaural phase-locking in the superior olivary complex deteriorates sharply above 1.5 kHz; second, 216 Hz sits directly adjacent to A3 in concert pitch, producing a soothing, warm cello-like timbre that does not irritate phonophobic patients.

The engine synthesizes two pure sine waves: the left ear receives $216 - \frac{\text{IAF}}{2}$, and the right ear receives $216 + \frac{\text{IAF}}{2}$. When processed dichotically through headphones, the brain perceives a clear, pulsating beat at precisely the patient's IAF.

Furthermore, because migraine patients experience severe sound sensitivity, starting or stopping an audio track abruptly causes uncomfortable transient clicking. To eliminate this, we implemented a **1.5-second squared half-cosine taper envelope**, guaranteeing a completely smooth, click-free onset and offset. The output is exported as an uncompressed 16-bit 44.1 kHz stereo audio file calibrated to 60–65 dB SPL."

---

### Slide 12: Experimental Results & Case Study (Minute 11:00 – 12:00)
> *(Action: Walk the board through the benchmarking table and highlight M10 metrics.)*

"Let us review our empirical results.

In our classification benchmarking, **EfficientNetB7** achieved superior performance, recording **93.75% accuracy**, **100.0% precision**, an **F1-score of 0.933**, and a **Matthews Correlation Coefficient of 0.875** on our held-out evaluation set—substantially outperforming VGG16 and ResNet50 using only single-channel occipital data.

To validate the entire closed loop, we executed a complete single-subject case study comparing migraine patient M10 against healthy control C10.

Our system successfully classified M10 as an interictal migraineur with 98.4% confidence, inverted the spectrogram, and identified an IAF peak of **9.87 Hertz**, accompanied by an Alpha Deficit of $-1.24~\mu\text{V}^2/\text{Hz}$ and a TAR of 1.48, compared to 0.82 in the control.

Within milliseconds, our engine synthesized a personalized audio prescription: **211.06 Hz** in the left channel and **220.94 Hz** in the right channel, delivering an exact 9.87 Hz entrainment rhythm.

Our final speaker, **Mahmudul Mashrafe**, will now discuss our standards compliance, cost analysis, and Washington Accord complex engineering attributes."

> *(Transition: Hand over the clicker to Mashrafe, step back.)*

---

# SPEAKER 5: Mahmudul Mashrafe (0112230115)
**Assigned Time**: 12:00 to 15:00 (3 Minutes Total)  
**Assigned Slides**: Slides 13, 14, and 15  
**Role**: Standards, Constraints, Cost Analysis, Complex Engineering Mapping, and Final Conclusion

---

### Slide 13: Standards Compliance & Design Constraints (Minute 12:00 – 13:00)
> *(Action: Stand confident, address the examiners, and reference the 6 constraint domains.)*

"Thank you, Jarin. Respected board members, I am **Mahmudul Mashrafe**.

To transition a biomedical framework from an academic prototype into safe clinical reality, it must rigorously satisfy established engineering standards and real-world constraints.

Our framework complies with **IFCN 10–20 standards** by anchoring single-channel acquisition to the Oz/O1 boundary, guaranteeing anatomical reproducibility. In acoustic delivery, we enforce a strict gain ceiling of 60 to 65 dB SPL in accordance with **WHO and OSHA safe listening guidelines**, preventing cochlear fatigue.

We comprehensively addressed multi-dimensional constraints:
Under **Health and Safety**, our proposed hardware enforces **IEC 60601-1 electrical isolation**, maintaining leakage currents under $10~\mu\text{A}$. Because our intervention is purely acoustic, it completely eliminates photic stimulation, removing any risk of inducing epileptic seizures or visual auras.
Under **Social and Usability**, we eliminate stigmatizing clinical headgear, designing for a discreet fabric headband suitable for home and workplace use.
Under **Environmental Sustainability**, providing a non-pharmacological digital therapeutic directly reduces the chemical manufacturing waste and wastewater contamination caused by chronic pharmaceutical overuse."

---

### Slide 14: Cost Analysis & Complex Engineering Mapping (Minute 13:00 – 14:00)
> *(Action: Direct attention to the cost comparison and the BAETE / Washington Accord mapping.)*

"Economic accessibility was a paramount design requirement. A research-grade 128-channel EEG system costs upwards of \$25,000, placing it entirely out of reach for consumer healthcare.

By demonstrating that single-channel occipital EEG retains 93.75% diagnostic accuracy, we eliminated 99% of sensor overhead. Our scaled bill of materials for mass production totals just **\$95.00 per unit**, supporting an accessible retail price of **\$199.00** with healthy margins, reinforced by a freemium app subscription and B2B clinical licensing.

Furthermore, in accordance with the International Engineering Alliance and BAETE guidelines, this project constitutes a **Complex Engineering Problem**:
It fulfills **P1 through P7**: demanding in-depth knowledge spanning eight Washington Accord profiles (WK1 to WK8); resolving conflicting trade-offs between wearability and diagnostic fidelity; executing deep mathematical analysis for color inversion; and engaging multiple stakeholders.
It likewise satisfies **Engineering Activities EA1 through EA5**, leveraging high-density computing infrastructure and cross-disciplinary innovation to address a major global public health challenge."

---

### Slide 15: Conclusion & Future Roadmap (Minute 14:00 – 15:00)
> *(Action: Summarize with clarity and conviction, thank the committee, and open the Q&A session.)*

"In conclusion, this Final Year Design Project successfully demonstrates a validated, closed-loop digital therapeutic framework:

We proved that a single occipital electrode can achieve 93.75% diagnostic accuracy; we developed a novel mathematical algorithm that decodes clinical spectra from 2D images with an $R^2 > 0.998$; and we engineered an automated system that delivers safe, click-free, personalized acoustic neuromodulation.

Our future roadmap encompasses physical PCB fabrication of a dry-sensor textile headband, edge deployment on mobile operating systems, and longitudinal clinical trials to quantify headache frequency reduction in chronic patients.

On behalf of our team, we express our profound gratitude to our project supervisor, the honorable defense committee, and the faculty of United International University for your invaluable mentorship.

We are now pleased to open the floor to your questions. Thank you very much."

---

## Defense Q&A Quick-Reference Guide (For All Members)

| Likely Committee Question | Core Technical Concept to Defend | Lead Responding Member |
| :--- | :--- | :--- |
| **"Why choose Channel #80 instead of frontal channels?"** | Channel #80 lies at the Oz/O1 boundary over the primary visual cortex (V1). The occipital lobe generates maximum human alpha power and is the epicenter of migraine sensory hyperexcitability and visual aura. | **Speaker 2 (Prince)** |
| **"How can you mathematically guarantee that colormap inversion does not distort frequencies?"** | The Viridis LUT inversion maps RGB coordinates back to physical decibels via minimum Euclidean distance. We validated this against numerical Welch transforms, obtaining an $R^2 > 0.998$ correlation with exact peak preservation. | **Speaker 3 (Anisa)** |
| **"Why is your carrier frequency 216 Hz and not 440 Hz?"** | The superior olivary complex phase-locks to interaural delays most effectively below 1.5 kHz. 216 Hz sits near A3 concert pitch, producing a warm, non-irritating acoustic timbre critical for phonophobic patients. | **Speaker 4 (Jarin)** |
| **"Why is 93.75% accuracy acceptable when Aslan (2023) achieved 100%?"** | Aslan used all 128 channels with heavy computation for offline diagnosis only. We achieved 93.75% using **just one single channel**, making a low-cost wearable feasible, and connected it to closed-loop therapy. | **Speaker 1 (Abu Hurayra)** |
| **"How does this project address Washington Accord P2 (Conflicting Requirements)?"** | High accuracy requires 128 wet gel electrodes, but wearable adoption requires 1 dry electrode. Balancing this trade-off without severe accuracy loss is the quintessential complex engineering problem our project solved. | **Speaker 5 (Mashrafe)** |
| **"What happens if the audio induces a headache or discomfort?"** | The audio engine includes strict software gain bounding (60–65 dB SPL), a 1.5s anti-click fade envelope, and emergency shut-off controls, ensuring listening levels remain well below OSHA/WHO hazard limits. | **Speaker 5 (Mashrafe)** |
