import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ArrowStyle, FancyArrowPatch
from PIL import Image

os.makedirs('Images', exist_ok=True)

# Set high-quality font defaults
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']

# ==============================================================================
# DIAGRAM 1: DATASET PREPROCESSING DIAGRAM
# ==============================================================================
def create_dataset_preprocess_diagram():
    fig, ax = plt.subplots(figsize=(15, 8.5), dpi=300)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    # Background canvas
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    # Title header banner
    title_box = FancyBboxPatch((0.4, 7.6), 14.2, 0.75, boxstyle="round,pad=0.08,rounding_size=0.15",
                               fc='#1a365d', ec='#0f233d', lw=1.5)
    ax.add_patch(title_box)
    ax.text(7.5, 7.97, 'UHD-EEG Acquisition, Artifact Removal & STFT Spectrogram Preprocessing Pipeline',
            ha='center', va='center', color='#ffffff', fontsize=14, fontweight='bold')

    # 4 Main Stages across columns
    # Col 1: Raw UHD-EEG (x=0.5 to 3.6)
    # Col 2: Signal Conditioning (x=4.1 to 7.2)
    # Col 3: STFT Time-Frequency (x=7.7 to 10.8)
    # Col 4: Viridis Image & Partition (x=11.3 to 14.4)

    col_w = 3.2
    col_h = 6.4
    y_col = 0.9

    stages = [
        {
            'x': 0.5,
            'title': 'Stage 1: Raw UHD-EEG Data',
            'sub': 'CMU Neuro-Engineering Repository',
            'header_c': '#2b6cb0',
            'bg_c': '#ebf8ff',
            'border_c': '#3182ce',
            'items': [
                ('Recording Modality', '128-ch BioSemi ActiveTwo (144 total)'),
                ('Cohort Breakdown', '18 Migraine (12 Aura, 6 No-Aura)\n18 Matched Controls (+4 Supp)'),
                ('Sampling & Dynamics', 'fs = 1000 Hz / 250 Hz, 24-bit BDF'),
                ('Clinical Paradigms', '• Resting State (Eyes Open / Closed)\n• Auditory SSAEP (4 Hz, 6 Hz tones)\n• Visual SSVEP (4 Hz, 6 Hz gratings)'),
                ('Patient State', 'Strictly Interictal (≥72h attack-free)')
            ]
        },
        {
            'x': 4.1,
            'title': 'Stage 2: Signal Conditioning',
            'sub': 'MNE-Python Biomedical Pipeline',
            'header_c': '#276749',
            'bg_c': '#f0fff4',
            'border_c': '#38a169',
            'items': [
                ('Montage Filtering', 'Extract 128 scalp electrodes;\nStrip ocular & external references'),
                ('Common Average Ref (CAR)', r'$v_i^{\mathrm{CAR}}(t) = v_i(t) - \frac{1}{128}\sum_{j=1}^{128} v_j(t)$'),
                ('Bandpass FIR Filter', '1.0 Hz – 50.0 Hz (Zero-Phase Hamming sinc)\nRemoves slow DC drift & EMG noise'),
                ('Powerline Notch', '60.0 Hz Notch Filter (Quality Q = 30)'),
                ('Channel Selection', 'Occipital Ch #80 (Oz/O1 boundary)\nPrime locus of migraine hyperexcitability')
            ]
        },
        {
            'x': 7.7,
            'title': 'Stage 3: Time-Frequency STFT',
            'sub': 'Spectro-Temporal Harmonic Extraction',
            'header_c': '#c05621',
            'bg_c': '#fffaf0',
            'border_c': '#dd6b20',
            'items': [
                ('Temporal Windowing', 'Sliding Hann Window: L = 500 samples (2.0s)\n50% Temporal Overlap (R = 250 samples)'),
                ('Discrete STFT Form', r'$X[m, k] = \sum_{n=0}^{L-1} x[mR+n] w[n] e^{-j\frac{2\pi kn}{N_{\mathrm{FFT}}}}$'),
                ('FFT Resolution', r'$N_{\mathrm{FFT}} = 1024$ frequency interpolation bins'),
                ('Logarithmic Power (dB)', r'$S_{\mathrm{dB}}[m,k] = 10\log_{10}\left(\frac{|X[m,k]|^2}{P_{\mathrm{norm}}}\right)$'),
                ('Frequency Boundaries', 'Constrained strictly to 1.0 Hz – 50.0 Hz')
            ]
        },
        {
            'x': 11.3,
            'title': 'Stage 4: Image & Partition',
            'sub': 'Photometric Calibration & Dataset Split',
            'header_c': '#6b46c1',
            'bg_c': '#faf5ff',
            'border_c': '#805ad5',
            'items': [
                ('Colormap Mapping', 'Perceptually Uniform Viridis LUT (256-color)\nClamped dynamic range: [-10, +30] dB'),
                ('Resolution & Format', 'Standardized 224 × 224 × 3 RGB PNGs\nPreserves spectral power gradients'),
                ('Cohort Corpus Size', '106 High-Resolution Spectrograms\n• 67 Healthy Control Images\n• 39 Interictal Migraine Images'),
                ('Dataset Partitioning', '60% Train Split (64 images)\n40% Evaluation Split (42 images)'),
                ('Target Utility', 'Computer Vision & Inverse LUT Reconstruction')
            ]
        }
    ]

    for st in stages:
        x = st['x']
        # Card container
        card = FancyBboxPatch((x, y_col), col_w, col_h, boxstyle="round,pad=0.08,rounding_size=0.12",
                              fc=st['bg_c'], ec=st['border_c'], lw=1.5)
        ax.add_patch(card)

        # Header bar
        header = FancyBboxPatch((x, y_col + col_h - 0.9), col_w, 0.9, boxstyle="round,pad=0.08,rounding_size=0.12",
                                fc=st['header_c'], ec=st['border_c'], lw=1)
        ax.add_patch(header)
        ax.text(x + col_w/2, y_col + col_h - 0.35, st['title'], ha='center', va='center',
                color='#ffffff', fontsize=10.5, fontweight='bold')
        ax.text(x + col_w/2, y_col + col_h - 0.65, st['sub'], ha='center', va='center',
                color='#e2e8f0', fontsize=8, style='italic')

        # Items
        cur_y = y_col + col_h - 1.2
        for label, val in st['items']:
            # Small pill for label
            pill = FancyBboxPatch((x + 0.15, cur_y - 0.22), col_w - 0.3, 0.26, boxstyle="round,pad=0.04,rounding_size=0.06",
                                  fc='#ffffff', ec=st['border_c'], lw=0.8)
            ax.add_patch(pill)
            ax.text(x + 0.25, cur_y - 0.09, label, ha='left', va='center',
                    color=st['header_c'], fontsize=8.5, fontweight='bold')
            
            cur_y -= 0.35
            # Value text
            ax.text(x + 0.25, cur_y, val, ha='left', va='top',
                    color='#2d3748', fontsize=8, linespacing=1.2)
            # Adjust spacing based on line count
            lines = val.count('\n') + 1
            cur_y -= (lines * 0.25 + 0.15)

    # Connecting arrows between stages
    arrow_props = dict(boxstyle="circle,pad=0.1", fc="#4a5568", ec="none")
    for i in range(3):
        x_start = stages[i]['x'] + col_w
        x_end = stages[i+1]['x']
        y_arrow = y_col + col_h / 2
        arrow = FancyArrowPatch((x_start + 0.05, y_arrow), (x_end - 0.05, y_arrow),
                                arrowstyle="-|>,head_width=4,head_length=6",
                                color="#2d3748", lw=2, mutation_scale=15)
        ax.add_patch(arrow)

    # Bottom summary footnote box
    foot_box = FancyBboxPatch((0.5, 0.15), 14.0, 0.55, boxstyle="round,pad=0.06,rounding_size=0.1",
                              fc='#edf2f7', ec='#cbd5e0', lw=1)
    ax.add_patch(foot_box)
    ax.text(7.5, 0.42, 'Summary: 128-channel UHD-EEG is conditioned, referenced to CAR, bandpassed to 1–50 Hz, and channel #80 is extracted.\nSTFT generates calibrated time-frequency power matrices rendered as 106 standardized Viridis RGB spectrograms for CNN input and PSD inversion.',
            ha='center', va='center', color='#4a5568', fontsize=8.5, style='italic', linespacing=1.2)

    plt.tight_layout()
    plt.savefig('Images/dataset_preprocess_diagram.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated Images/dataset_preprocess_diagram.png successfully.")

# ==============================================================================
# DIAGRAM 2: WHOLE METHODOLOGY DIAGRAM (END-TO-END CLOSED-LOOP ARCHITECTURE)
# ==============================================================================
def create_whole_methodology_diagram():
    fig, ax = plt.subplots(figsize=(16, 9.5), dpi=300)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9.5)
    ax.axis('off')

    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    # Title header banner
    title_box = FancyBboxPatch((0.5, 8.6), 15.0, 0.75, boxstyle="round,pad=0.08,rounding_size=0.15",
                               fc='#1e3a8a', ec='#172554', lw=1.5)
    ax.add_patch(title_box)
    ax.text(8.0, 8.97, 'End-to-End Closed-Loop Wearable EEG Architecture: Diagnostic & Personalized Therapeutic Entrainment',
            ha='center', va='center', color='#ffffff', fontsize=14, fontweight='bold')

    # Left Section: Data Acquisition & Time-Frequency Transformation (x=0.5 to 4.2)
    card1 = FancyBboxPatch((0.5, 1.2), 3.8, 7.1, boxstyle="round,pad=0.08,rounding_size=0.12",
                           fc='#f8fafc', ec='#94a3b8', lw=1.5)
    ax.add_patch(card1)
    h1 = FancyBboxPatch((0.5, 7.5), 3.8, 0.8, boxstyle="round,pad=0.08,rounding_size=0.12",
                        fc='#334155', ec='#1e293b', lw=1)
    ax.add_patch(h1)
    ax.text(2.4, 7.9, '1. EEG Acquisition & Preprocessing', ha='center', va='center', color='#ffffff', fontsize=10.5, fontweight='bold')

    steps1 = [
        ('128-ch BioSemi ActiveTwo', '18 Migraineurs + 18 Healthy Controls\nResting-State, Auditory SSAEP, Visual SSVEP'),
        ('Signal Conditioning', 'Common Average Reference (CAR)\n1.0 – 50.0 Hz Zero-Phase Bandpass\n60 Hz Notch Filter (Q = 30)'),
        ('Occipital Channel #80', 'Selected over visual cortex (Oz/O1)\nLocus of cortical hyperexcitability'),
        ('STFT Time-Frequency', 'Hann window (L=500, 50% overlap)\nLog power: -10 dB to +30 dB'),
        ('2D Viridis Spectrogram', '224 × 224 × 3 RGB Images\n106 total images (67 Control, 39 Migraine)')
    ]
    y_pos = 7.1
    for title, desc in steps1:
        pill = FancyBboxPatch((0.7, y_pos - 0.25), 3.4, 0.28, boxstyle="round,pad=0.04,rounding_size=0.06",
                              fc='#e2e8f0', ec='#cbd5e1', lw=0.8)
        ax.add_patch(pill)
        ax.text(0.8, y_pos - 0.11, title, ha='left', va='center', color='#1e293b', fontsize=8.5, fontweight='bold')
        y_pos -= 0.4
        ax.text(0.8, y_pos, desc, ha='left', va='top', color='#475569', fontsize=8, linespacing=1.2)
        y_pos -= (desc.count('\n') * 0.25 + 0.35)

    # Center-Top: Deep Transfer Learning Branch (x=4.8 to 10.4, y=4.9 to 8.3)
    card2 = FancyBboxPatch((4.8, 4.9), 5.8, 3.4, boxstyle="round,pad=0.08,rounding_size=0.12",
                           fc='#fef2f2', ec='#ef4444', lw=1.5)
    ax.add_patch(card2)
    h2 = FancyBboxPatch((4.8, 7.5), 5.8, 0.8, boxstyle="round,pad=0.08,rounding_size=0.12",
                        fc='#b91c1c', ec='#991b1b', lw=1)
    ax.add_patch(h2)
    ax.text(7.7, 7.9, '2. Deep Transfer Learning Diagnostic Classifier', ha='center', va='center', color='#ffffff', fontsize=10.5, fontweight='bold')

    cnn_txt = (
        '• Pre-Trained Backbones: VGG16 (14.7M) | ResNet50 (25.6M) | EfficientNetB7 (66M)\n'
        '• Custom Head: GlobalAveragePooling2D → Dense(128, ReLU) → Dropout(0.2) → Softmax(2)\n'
        '• Optimization: Adam (η = 1e-4), Sparse Categorical Cross-Entropy Loss\n'
        '• Benchmark Performance:\n'
        '   - EfficientNetB7: 93.75% Accuracy | 94.71% Precision | 93.85% F1 | 0.8750 MCC (Best)\n'
        '   - VGG16: 90.63% Accuracy | 90.99% Precision | 90.71% F1 | 0.7985 MCC\n'
        '   - ResNet50: 87.50% Accuracy | 88.61% Precision | 87.71% F1 | 0.7410 MCC'
    )
    ax.text(5.0, 7.2, cnn_txt, ha='left', va='top', color='#7f1d1d', fontsize=8, linespacing=1.25)

    # Decision Diamond (x=11.1, y=6.2)
    diamond = patches.Polygon([[11.1, 6.6], [12.1, 7.4], [13.1, 6.6], [12.1, 5.8]],
                              fc='#fef08a', ec='#ca8a04', lw=2)
    ax.add_patch(diamond)
    ax.text(12.1, 6.75, 'Interictal\nMigraine?', ha='center', va='center', color='#854d0e', fontsize=9, fontweight='bold')

    # Arrow from CNN to Decision Diamond
    ax.add_patch(FancyArrowPatch((10.6, 6.6), (11.05, 6.6), arrowstyle="-|>,head_width=4,head_length=6", color='#991b1b', lw=2))

    # Control outcome (No -> Normal state)
    ax.add_patch(FancyArrowPatch((12.1, 7.4), (12.1, 8.2), arrowstyle="-|>,head_width=3,head_length=5", color='#16a34a', lw=1.8))
    ax.text(12.25, 7.8, 'NO (Control)', color='#16a34a', fontsize=8, fontweight='bold')
    ctrl_box = FancyBboxPatch((13.4, 7.8), 2.2, 0.6, boxstyle="round,pad=0.05,rounding_size=0.08", fc='#dcfce7', ec='#22c55e', lw=1)
    ax.add_patch(ctrl_box)
    ax.text(14.5, 8.1, 'Healthy Baseline Logged\nNo Entrainment Required', ha='center', va='center', color='#15803d', fontsize=7.5, fontweight='bold')
    ax.add_patch(FancyArrowPatch((12.6, 8.1), (13.35, 8.1), arrowstyle="-|>,head_width=3,head_length=5", color='#16a34a', lw=1.5))

    # Migraine outcome (Yes -> Triggers Neuromodulation Branch)
    ax.add_patch(FancyArrowPatch((12.1, 5.8), (12.1, 4.7), arrowstyle="-|>,head_width=4,head_length=6", color='#dc2626', lw=2.2))
    ax.text(12.25, 5.25, 'YES (Migraine Detected)', color='#b91c1c', fontsize=8.5, fontweight='bold')

    # Center-Bottom: Analytical Inversion & Biomarker Extraction (x=4.8 to 10.4, y=1.2 to 4.5)
    card3 = FancyBboxPatch((4.8, 1.2), 5.8, 3.3, boxstyle="round,pad=0.08,rounding_size=0.12",
                           fc='#f0fdf4', ec='#22c55e', lw=1.5)
    ax.add_patch(card3)
    h3 = FancyBboxPatch((4.8, 3.7), 5.8, 0.8, boxstyle="round,pad=0.08,rounding_size=0.12",
                        fc='#15803d', ec='#166534', lw=1)
    ax.add_patch(h3)
    ax.text(7.7, 4.1, '3. Spectrogram Inversion & Biomarker Extraction', ha='center', va='center', color='#ffffff', fontsize=10.5, fontweight='bold')

    inv_txt = (
        '• Viridis Colormap Look-Up Table (LUT): 256-color precomputed sRGB matrix\n'
        r'• Minimum Euclidean Inversion: $\hat{k}(y,t) = \arg\min_k ||\mathbf{p}(y,t) - \mathrm{LUT}_k||_2$' + '\n'
        r'• Calibrated Decibel & PSD: $S_{\mathrm{dB}} = -10 + 40\hat{u}\ \mathrm{dB} \rightarrow P(y,t) = 10^{S_{\mathrm{dB}}/10}\ \mu\mathrm{V}^2/\mathrm{Hz}$' + '\n'
        r'• Frequency Mapping: $f(y) = 50.0 - y \cdot (49.0 / 399.0)$ across 400 rows' + '\n'
        '• Biomarker Localization:\n'
        r'   - Individual Alpha Frequency (IAF): Peak frequency within [8.0, 13.0] Hz' + '\n'
        r'   - Relative Power & Deficit: $\tilde{P}(\alpha)$ vs. 20% normative; $\Delta_\alpha = \max(0, 0.20 - \tilde{P}(\alpha))$' + '\n'
        r'   - Theta-to-Alpha Ratio (TAR): $\tilde{P}(\mathrm{Theta}) / \tilde{P}(\mathrm{Alpha})$ (Elevated in migraine: 1.64 vs 1.15)'
    )
    ax.text(5.0, 3.45, inv_txt, ha='left', va='top', color='#14532d', fontsize=8, linespacing=1.22)

    # Connecting Arrow from Spectrogram (Card 1) to Inversion (Card 3) and CNN (Card 2)
    ax.add_patch(FancyArrowPatch((4.3, 6.6), (4.75, 6.6), arrowstyle="-|>,head_width=4,head_length=6", color='#1e293b', lw=2))
    ax.add_patch(FancyArrowPatch((4.3, 2.8), (4.75, 2.8), arrowstyle="-|>,head_width=4,head_length=6", color='#1e293b', lw=2))

    # Right-Bottom: Personalized Binaural Beat Audio Synthesis (x=11.0 to 15.5, y=1.2 to 4.5)
    card4 = FancyBboxPatch((11.0, 1.2), 4.6, 3.3, boxstyle="round,pad=0.08,rounding_size=0.12",
                           fc='#faf5ff', ec='#a855f7', lw=1.5)
    ax.add_patch(card4)
    h4 = FancyBboxPatch((11.0, 3.7), 4.6, 0.8, boxstyle="round,pad=0.08,rounding_size=0.12",
                        fc='#7e22ce', ec='#6b21a8', lw=1)
    ax.add_patch(h4)
    ax.text(13.3, 4.1, '4. Targeted Binaural Beat Synthesis', ha='center', va='center', color='#ffffff', fontsize=10.5, fontweight='bold')

    audio_txt = (
        r'• Resonant Tuning: $f_{\mathrm{beat}} = \mathrm{IAF}$ (e.g. 10.09 Hz for M10)' + '\n'
        r'• Carrier Frequency: $f_c = 216.0$ Hz (Max brainstem phase locking)' + '\n'
        '• Dichotic Pure-Tone Frequency Allocation:\n'
        r'   - Left Ear: $f_{\mathrm{left}} = f_c - \mathrm{IAF}/2 = 210.96$ Hz' + '\n'
        r'   - Right Ear: $f_{\mathrm{right}} = f_c + \mathrm{IAF}/2 = 221.05$ Hz' + '\n'
        r'• Anti-Click Taper: 1.5s squared half-cosine envelope $E[n]$' + '\n'
        '• Digital Output: 16-bit 44.1 kHz Stereo WAV\n'
        '• Neuro-Mechanism: Superior Olivary Complex (SOC)\n'
        '   phase locking → Thalamocortical entrainment'
    )
    ax.text(11.2, 3.45, audio_txt, ha='left', va='top', color='#581c87', fontsize=8, linespacing=1.22)

    # Connecting Arrow from Inversion (Card 3) to Audio (Card 4)
    ax.add_patch(FancyArrowPatch((10.6, 2.8), (10.95, 2.8), arrowstyle="-|>,head_width=4,head_length=6", color='#7e22ce', lw=2.2))

    # Bottom summary box
    foot_box = FancyBboxPatch((0.5, 0.15), 15.1, 0.65, boxstyle="round,pad=0.06,rounding_size=0.1",
                              fc='#f1f5f9', ec='#cbd5e1', lw=1)
    ax.add_patch(foot_box)
    ax.text(8.0, 0.47, 'Closed-Loop Feedback: Dual-branch architecture executes automated diagnostic screening via EfficientNetB7 (93.75% accuracy) and\nanalytical Viridis LUT spectrogram inversion to extract patient IAF and synthesize personalized 216 Hz dichotic binaural beats.',
            ha='center', va='center', color='#334155', fontsize=8.5, style='italic', linespacing=1.2)

    plt.tight_layout()
    plt.savefig('Images/whole_methodology_diagram.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated Images/whole_methodology_diagram.png successfully.")

# ==============================================================================
# DIAGRAM 3: BINAURAL BEATS GENERATION DIAGRAM (SYNTHESIS & NEUROPHYSIOLOGY)
# ==============================================================================
def create_binaural_beats_diagram():
    fig, ax = plt.subplots(figsize=(15.5, 9.0), dpi=300)
    ax.set_xlim(0, 15.5)
    ax.set_ylim(0, 9.0)
    ax.axis('off')

    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    # Title header banner
    title_box = FancyBboxPatch((0.5, 8.1), 14.5, 0.75, boxstyle="round,pad=0.08,rounding_size=0.15",
                               fc='#4a044e', ec='#2e0854', lw=1.5)
    ax.add_patch(title_box)
    ax.text(7.75, 8.47, 'Personalized Binaural Beat Audio Synthesis & Neurophysiological Entrainment Pathway',
            ha='center', va='center', color='#ffffff', fontsize=13.5, fontweight='bold')

    # 4 Sequential Blocks (Left-to-Right layout)
    # Block 1: Patient Biomarker Input (x=0.5 to 3.8)
    # Block 2: Digital Audio Synthesis Engine (x=4.2 to 7.8)
    # Block 3: Anti-Click Envelope & Export (x=8.2 to 11.5)
    # Block 4: Ascending Auditory Pathway & Cortical Entrainment (x=11.9 to 15.1)

    y_bot = 1.1
    b_h = 6.6

    # Panel 1: Biomarker Input
    p1 = FancyBboxPatch((0.5, y_bot), 3.4, b_h, boxstyle="round,pad=0.08,rounding_size=0.12",
                        fc='#faf5ff', ec='#9333ea', lw=1.5)
    ax.add_patch(p1)
    hp1 = FancyBboxPatch((0.5, y_bot + b_h - 0.8), 3.4, 0.8, boxstyle="round,pad=0.08,rounding_size=0.12",
                         fc='#7e22ce', ec='#6b21a8', lw=1)
    ax.add_patch(hp1)
    ax.text(2.2, y_bot + b_h - 0.4, '1. Patient Biomarkers', ha='center', va='center', color='#ffffff', fontsize=10, fontweight='bold')

    b1_items = [
        ('Reconstructed PSD', 'Extracted via Viridis LUT inversion\nof occipital channel #80 spectrogram'),
        ('Individual Alpha Freq (IAF)', r'$\mathrm{IAF} = \arg\max_{f \in [8, 13]} \overline{P}(f)$' + '\nExemplar M10: IAF = 10.09 Hz'),
        ('Alpha Power Deficit', r'$\Delta_\alpha = \max(0, 0.20 - \tilde{P}(\alpha))$' + '\nPatient M10: 7.88% Deficit\n(Normalized Alpha = 12.12%)'),
        ('Theta-to-Alpha Ratio', r'$\mathrm{TAR} = \tilde{P}(\theta) / \tilde{P}(\alpha) = 1.64$' + '\nMarker of thalamocortical slowing'),
        ('Target Beat Frequency', r'$f_{\mathrm{beat}} = \mathrm{IAF} = 10.09$ Hz' + '\nTuned precisely to patient resonance')
    ]
    cur_y = y_bot + b_h - 1.1
    for title, desc in b1_items:
        pill = FancyBboxPatch((0.65, cur_y - 0.22), 3.1, 0.26, boxstyle="round,pad=0.04,rounding_size=0.06",
                              fc='#f3e8ff', ec='#d8b4fe', lw=0.8)
        ax.add_patch(pill)
        ax.text(0.75, cur_y - 0.09, title, ha='left', va='center', color='#6b21a8', fontsize=8, fontweight='bold')
        cur_y -= 0.35
        ax.text(0.75, cur_y, desc, ha='left', va='top', color='#3b0764', fontsize=7.8, linespacing=1.2)
        cur_y -= (desc.count('\n') * 0.22 + 0.3)

    # Panel 2: Audio Synthesis Engine
    p2 = FancyBboxPatch((4.2, y_bot), 3.6, b_h, boxstyle="round,pad=0.08,rounding_size=0.12",
                        fc='#eff6ff', ec='#2563eb', lw=1.5)
    ax.add_patch(p2)
    hp2 = FancyBboxPatch((4.2, y_bot + b_h - 0.8), 3.6, 0.8, boxstyle="round,pad=0.08,rounding_size=0.12",
                         fc='#1d4ed8', ec='#1e40af', lw=1)
    ax.add_patch(hp2)
    ax.text(6.0, y_bot + b_h - 0.4, '2. Dichotic Wave Synthesis', ha='center', va='center', color='#ffffff', fontsize=10, fontweight='bold')

    b2_items = [
        ('Carrier Frequency (fc)', r'$f_c = 216.0$ Hz (Warm pitch A3)' + '\nOptimal for superior olivary phase-locking;\nHarmless to photophobic/phonophobic brain'),
        ('Dichotic Pure Tones', r'Left: $f_L = f_c - \frac{\mathrm{IAF}}{2} = 210.96$ Hz' + '\n' +
                                r'Right: $f_R = f_c + \frac{\mathrm{IAF}}{2} = 221.05$ Hz'),
        ('Sinusoidal Generators', r'$s_L(t) = A \cdot \sin(2\pi f_L t)$' + '\n' +
                                  r'$s_R(t) = A \cdot \sin(2\pi f_R t)$' + '\nPeak amplitude A = 0.75 (-2.5 dBFS)'),
        ('Headroom & Dynamic Range', 'Guarantees ≥2.5 dB DAC headroom;\nCompletely eliminates inter-sample clipping'),
        ('Sampling Specifications', 'Sampling rate: fs = 44,100 Hz (CD quality)\nDuration: 300s (5.0 min prescription)')
    ]
    cur_y = y_bot + b_h - 1.1
    for title, desc in b2_items:
        pill = FancyBboxPatch((4.35, cur_y - 0.22), 3.3, 0.26, boxstyle="round,pad=0.04,rounding_size=0.06",
                              fc='#dbeafe', ec='#93c5fd', lw=0.8)
        ax.add_patch(pill)
        ax.text(4.45, cur_y - 0.09, title, ha='left', va='center', color='#1d4ed8', fontsize=8, fontweight='bold')
        cur_y -= 0.35
        ax.text(4.45, cur_y, desc, ha='left', va='top', color='#1e3a8a', fontsize=7.8, linespacing=1.2)
        cur_y -= (desc.count('\n') * 0.22 + 0.3)

    # Panel 3: Anti-Click Envelope & Export
    p3 = FancyBboxPatch((8.1, y_bot), 3.4, b_h, boxstyle="round,pad=0.08,rounding_size=0.12",
                        fc='#f0fdf4', ec='#16a34a', lw=1.5)
    ax.add_patch(p3)
    hp3 = FancyBboxPatch((8.1, y_bot + b_h - 0.8), 3.4, 0.8, boxstyle="round,pad=0.08,rounding_size=0.12",
                         fc='#15803d', ec='#166534', lw=1)
    ax.add_patch(hp3)
    ax.text(9.8, y_bot + b_h - 0.4, '3. Anti-Click Shaping & Export', ha='center', va='center', color='#ffffff', fontsize=10, fontweight='bold')

    b3_items = [
        ('Acoustic Click Prevention', 'Instantaneous tone onset creates high-freq\nspectral splatter that triggers headache.\nTaper envelope eliminates switching clicks.'),
        ('Squared Half-Cosine Fade', r'Fade-In: $E(t) = \sin^2\left(\frac{\pi t}{2 T_{\mathrm{fade}}}\right)$' + '\n' +
                                     r'Fade-Out: $E(t) = \cos^2\left(\frac{\pi (t - t_0)}{2 T_{\mathrm{fade}}}\right)$' + '\n' + r'Duration: $T_{\mathrm{fade}} = 1.5$ seconds'),
        ('16-bit PCM Quantization', r'$s[n] = \lfloor 32767 \cdot E[n] \cdot s(t) \rfloor$' + '\nQuantized into signed 16-bit integers\nRange: [-32768, +32767]'),
        ('Audio Export Format', 'Uncompressed Stereo WAV (44.1 kHz)\nLossless acoustic fidelity\nCompatible with clinical headphones')
    ]
    cur_y = y_bot + b_h - 1.1
    for title, desc in b3_items:
        pill = FancyBboxPatch((8.25, cur_y - 0.22), 3.1, 0.26, boxstyle="round,pad=0.04,rounding_size=0.06",
                              fc='#dcfce7', ec='#86efac', lw=0.8)
        ax.add_patch(pill)
        ax.text(8.35, cur_y - 0.09, title, ha='left', va='center', color='#15803d', fontsize=8, fontweight='bold')
        cur_y -= 0.35
        ax.text(8.35, cur_y, desc, ha='left', va='top', color='#14532d', fontsize=7.8, linespacing=1.2)
        cur_y -= (desc.count('\n') * 0.22 + 0.3)

    # Panel 4: Ascending Neurophysiological Entrainment Pathway
    p4 = FancyBboxPatch((11.8, y_bot), 3.3, b_h, boxstyle="round,pad=0.08,rounding_size=0.12",
                        fc='#fff7ed', ec='#ea580c', lw=1.5)
    ax.add_patch(p4)
    hp4 = FancyBboxPatch((11.8, y_bot + b_h - 0.8), 3.3, 0.8, boxstyle="round,pad=0.08,rounding_size=0.12",
                         fc='#c2410c', ec='#9a3412', lw=1)
    ax.add_patch(hp4)
    ax.text(13.45, y_bot + b_h - 0.4, '4. Auditory Pathway & FFR', ha='center', va='center', color='#ffffff', fontsize=10, fontweight='bold')

    b4_items = [
        ('Dichotic Auditory Input', 'Calibrated stereo headphones deliver\n210.96 Hz (left) and 221.05 Hz (right)\ninto separate ears simultaneously'),
        ('Superior Olivary Complex', 'Medial Superior Olive (MSO) in pons\ncomputes Interaural Phase Difference (IPD)\nNeurons fire at beat delta: 10.09 Hz'),
        ('Ascending Brainstem Path', 'Inferior Colliculus (IC) →\nMedial Geniculate Nucleus (Thalamus) →\nPrimary Auditory Cortex (A1)'),
        ('Thalamocortical Entrainment', 'Drives Frequency Following Response (FFR)\nRestores sensory gating & habituation\nSuppresses cortical hyperexcitability'),
        ('Clinical Mitigation Outcome', 'Replaces toxic pharmacotherapy with\npersonalized, non-invasive digital acoustic\nneuromodulation')
    ]
    cur_y = y_bot + b_h - 1.1
    for title, desc in b4_items:
        pill = FancyBboxPatch((11.95, cur_y - 0.22), 3.0, 0.26, boxstyle="round,pad=0.04,rounding_size=0.06",
                              fc='#ffedd5', ec='#fdba74', lw=0.8)
        ax.add_patch(pill)
        ax.text(12.05, cur_y - 0.09, title, ha='left', va='center', color='#c2410c', fontsize=8, fontweight='bold')
        cur_y -= 0.35
        ax.text(12.05, cur_y, desc, ha='left', va='top', color='#7c2d12', fontsize=7.8, linespacing=1.2)
        cur_y -= (desc.count('\n') * 0.22 + 0.3)

    # Connecting arrows
    for x_conn in [3.9, 7.8, 11.5]:
        ax.add_patch(FancyArrowPatch((x_conn + 0.05, y_bot + b_h/2), (x_conn + 0.25, y_bot + b_h/2),
                                     arrowstyle="-|>,head_width=4,head_length=6", color='#374151', lw=2))

    # Bottom summary footnote
    foot_box = FancyBboxPatch((0.5, 0.15), 14.6, 0.65, boxstyle="round,pad=0.06,rounding_size=0.1",
                              fc='#f8fafc', ec='#cbd5e1', lw=1)
    ax.add_patch(foot_box)
    ax.text(7.75, 0.47, 'Biomedical Entrainment Mechanism: Patient-specific IAF (10.09 Hz for M10) modulates dichotic pure tones around a 216 Hz carrier.\nThe brainstem Superior Olivary Complex detects interaural phase disparities, driving cortical frequency-following resonance to reverse alpha deficits.',
            ha='center', va='center', color='#334155', fontsize=8.5, style='italic', linespacing=1.2)

    plt.tight_layout()
    plt.savefig('Images/binaural_beats_diagram.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated Images/binaural_beats_diagram.png successfully.")

if __name__ == '__main__':
    create_dataset_preprocess_diagram()
    create_whole_methodology_diagram()
    create_binaural_beats_diagram()
