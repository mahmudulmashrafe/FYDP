import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, Wedge
from PIL import Image

os.makedirs('Images', exist_ok=True)

# Use clean, publication-ready font settings
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.edgecolor'] = '#cbd5e1'
plt.rcParams['axes.linewidth'] = 1.0

# ==============================================================================
# 1. HIGH-QUALITY DATASET PREPROCESSING DIAGRAM
# ==============================================================================
def generate_dataset_preprocess_diagram():
    fig = plt.figure(figsize=(16, 10.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')

    # Overall title
    plt.suptitle('UHD-EEG Acquisition, Artifact Removal & STFT Spectrogram Preprocessing Pipeline',
                 fontsize=15, fontweight='bold', color='#1e293b', y=0.98)

    # Subplot Grid: 2 rows x 2 columns
    # Panel A: 128-ch Head Montage (top-left)
    # Panel B: Signal Conditioning Before & After (top-right)
    # Panel C: Sliding Hann STFT Windowing (bottom-left)
    # Panel D: Real Calibrated Viridis Spectrogram & Partition (bottom-right)

    # -------------------------------------------------------------------------
    # PANEL A: Head Montage & Occipital Channel #80
    # -------------------------------------------------------------------------
    ax_a = fig.add_subplot(2, 2, 1)
    ax_a.set_title('A. 128-Channel Scalp Montage & Channel #80 Selection', fontsize=11, fontweight='bold', pad=10, color='#0f172a')
    ax_a.set_xlim(-1.4, 1.4)
    ax_a.set_ylim(-1.4, 1.4)
    ax_a.set_aspect('equal')
    ax_a.axis('off')

    # Draw head outline
    head_circle = Circle((0, 0), 1.0, facecolor='#f8fafc', edgecolor='#64748b', linewidth=2.5, zorder=1)
    ax_a.add_patch(head_circle)

    # Nose
    nose = Polygon([[-0.15, 0.98], [0.0, 1.22], [0.15, 0.98]], facecolor='#f8fafc', edgecolor='#64748b', linewidth=2.0, zorder=2)
    ax_a.add_patch(nose)

    # Left & Right Ears
    ear_l = patches.Ellipse((-1.05, 0.0), 0.15, 0.4, facecolor='#f8fafc', edgecolor='#64748b', linewidth=2.0, zorder=1)
    ear_r = patches.Ellipse((1.05, 0.0), 0.15, 0.4, facecolor='#f8fafc', edgecolor='#64748b', linewidth=2.0, zorder=1)
    ax_a.add_patch(ear_l)
    ax_a.add_patch(ear_r)

    # Generate 128 concentric electrode coordinates
    np.random.seed(42)
    radii = [0.22, 0.44, 0.65, 0.85]
    n_per_ring = [12, 24, 40, 52]
    all_x, all_y = [0], [0] # Cz
    for r, n in zip(radii, n_per_ring):
        angles = np.linspace(0, 2*np.pi, n, endpoint=False)
        all_x.extend(r * np.cos(angles))
        all_y.extend(r * np.sin(angles))

    # Plot all channels as subtle slate dots
    ax_a.scatter(all_x, all_y, s=18, color='#94a3b8', edgecolors='#64748b', linewidths=0.5, zorder=3, label='128 Scalp Electrodes')

    # Channel #80 (Medial Occipital / Oz boundary: posterior midline, near y = -0.75, x = 0.0)
    ch80_x, ch80_y = 0.0, -0.75
    ax_a.scatter([ch80_x], [ch80_y], s=140, color='#dc2626', edgecolors='#991b1b', linewidths=2.0, zorder=5)
    ax_a.scatter([ch80_x], [ch80_y], s=260, facecolors='none', edgecolors='#ef4444', linewidths=1.5, linestyle='--', zorder=4)

    # Annotation callout
    ax_a.annotate('Channel #80 (Oz/O1)\nMedial Occipital Locus\nVisual Hyperexcitability',
                  xy=(ch80_x, ch80_y), xytext=(0.45, -1.15),
                  arrowprops=dict(facecolor='#dc2626', edgecolor='#991b1b', shrink=0.08, width=1.5, headwidth=6),
                  fontsize=8.5, fontweight='bold', color='#991b1b', ha='left',
                  bbox=dict(boxstyle='round,pad=0.4', facecolor='#fef2f2', edgecolor='#fca5a5', lw=1))

    # Informational badges
    ax_a.text(0, 1.32, 'BioSemi ActiveTwo 128-ch Radial Layout', ha='center', fontsize=9, fontweight='bold', color='#1e3a8a')
    ax_a.text(-1.25, -1.25, '18 Migraineurs (12 Aura, 6 No-Aura)\n18 Matched Controls (Interictal)',
              fontsize=8, color='#334155', bbox=dict(boxstyle='round,pad=0.3', facecolor='#f1f5f9', edgecolor='#cbd5e1'))

    # -------------------------------------------------------------------------
    # PANEL B: Signal Conditioning (Raw vs Filtered EEG + Frequency Response)
    # -------------------------------------------------------------------------
    ax_b = fig.add_subplot(2, 2, 2)
    ax_b.set_title('B. Multichannel Signal Conditioning & Artifact Rejection', fontsize=11, fontweight='bold', pad=10, color='#0f172a')

    t = np.linspace(0, 2.0, 1000)
    # Synthetic clean physiological EEG (alpha + theta)
    clean_signal = 15.0 * np.sin(2 * np.pi * 10.0 * t) + 8.0 * np.sin(2 * np.pi * 6.0 * t) + 4.0 * np.sin(2 * np.pi * 22.0 * t)
    # Raw signal corrupted by 60 Hz line hum, DC drift, and random EMG noise
    dc_drift = 25.0 * np.sin(2 * np.pi * 0.3 * t) + 15.0
    line_hum = 18.0 * np.sin(2 * np.pi * 60.0 * t)
    emg_noise = np.random.normal(0, 6.0, len(t))
    raw_signal = clean_signal + dc_drift + line_hum + emg_noise

    ax_b.plot(t, raw_signal + 35, color='#94a3b8', linewidth=1.1, label='1. Raw EEG (Corrupted: 60Hz hum, DC drift, EMG noise)')
    ax_b.plot(t, clean_signal - 30, color='#0284c7', linewidth=1.4, label='2. Conditioned EEG (CAR + 1–50 Hz FIR + 60Hz Notch)')

    ax_b.set_xlabel('Time (seconds)', fontsize=9, fontweight='bold')
    ax_b.set_ylabel('Amplitude (μV)', fontsize=9, fontweight='bold')
    ax_b.set_ylim(-75, 95)
    ax_b.grid(True, linestyle=':', alpha=0.6)
    ax_b.legend(loc='upper right', fontsize=8, framealpha=0.9)

    # Inset card for filter parameters
    filter_box = (
        r"$\mathbf{Filtering\ Specifications:}$" + "\n"
        r"• $\mathrm{CAR:}\ v_i^{\mathrm{CAR}}(t) = v_i(t) - \frac{1}{128}\sum v_j(t)$" + "\n"
        r"• Zero-Phase FIR Bandpass: 1.0 – 50.0 Hz (Hamming sinc)" + "\n"
        r"• 60.0 Hz Notch Filter ($Q = 30$, suppresses AC powerline)"
    )
    ax_b.text(0.03, 0.06, filter_box, transform=ax_b.transAxes, fontsize=8,
              bbox=dict(boxstyle='round,pad=0.4', facecolor='#f0fdf4', edgecolor='#86efac', lw=1), color='#166534')

    # -------------------------------------------------------------------------
    # PANEL C: Sliding Hann STFT Windowing Mechanism
    # -------------------------------------------------------------------------
    ax_c = fig.add_subplot(2, 2, 3)
    ax_c.set_title('C. Short-Time Fourier Transform (STFT) Windowing Mechanism', fontsize=11, fontweight='bold', pad=10, color='#0f172a')

    t_stft = np.linspace(0, 4.0, 1000)
    eeg_trace = 12.0 * np.sin(2*np.pi*9.5*t_stft) + 8.0 * np.sin(2*np.pi*5.0*t_stft) + np.random.normal(0, 2.0, len(t_stft))
    ax_c.plot(t_stft, eeg_trace, color='#475569', linewidth=1.0, alpha=0.8, label='Channel #80 Signal $x[n]$')

    # Draw two overlapping Hann windows
    hann_w = np.hanning(250) * 22.0
    t_w1 = np.linspace(0.5, 2.5, 250)
    t_w2 = np.linspace(1.5, 3.5, 250)

    ax_c.plot(t_w1, hann_w, color='#ea580c', linewidth=2.0, label='Window $m$: Hann 2.0s ($L=500$)')
    ax_c.fill_between(t_w1, 0, hann_w, color='#ffedd5', alpha=0.5)

    ax_c.plot(t_w2, hann_w, color='#7c3aed', linewidth=2.0, linestyle='--', label='Window $m+1$: 50% Overlap ($R=250$)')
    ax_c.fill_between(t_w2, 0, hann_w, color='#ede9fe', alpha=0.4)

    ax_c.set_xlabel('Time (seconds)', fontsize=9, fontweight='bold')
    ax_c.set_ylabel('Amplitude (μV)', fontsize=9, fontweight='bold')
    ax_c.set_ylim(-20, 30)
    ax_c.grid(True, linestyle=':', alpha=0.6)
    ax_c.legend(loc='upper right', fontsize=8, framealpha=0.9)

    stft_eq = (
        r"$\mathbf{Discrete\ STFT\ Formulation:}$" + "\n"
        r"$X[m, k] = \sum_{n=0}^{L-1} x[mR+n] w[n] e^{-j \frac{2\pi kn}{N_{\mathrm{FFT}}}}$" + "\n"
        r"$S_{\mathrm{dB}}[m, k] = 10 \log_{10}\left(\frac{|X[m, k]|^2}{P_{\mathrm{norm}}}\right),\quad N_{\mathrm{FFT}}=1024$"
    )
    ax_c.text(0.03, 0.06, stft_eq, transform=ax_c.transAxes, fontsize=8.2,
              bbox=dict(boxstyle='round,pad=0.4', facecolor='#fffaf0', edgecolor='#fed7aa', lw=1), color='#9a3412')

    # -------------------------------------------------------------------------
    # PANEL D: Real Spectrogram Image & Dataset Split
    # -------------------------------------------------------------------------
    ax_d = fig.add_subplot(2, 2, 4)
    ax_d.set_title('D. Calibrated Viridis Spectrogram & Dataset Partitioning', fontsize=11, fontweight='bold', pad=10, color='#0f172a')

    spectrogram_path = 'spectrograms/spectrograms/Migraine/M10_Resting.png'
    if os.path.exists(spectrogram_path):
        img = Image.open(spectrogram_path)
        # Display image with extent: x in [0, 10] s, y in [1, 50] Hz
        im_plot = ax_d.imshow(img, aspect='auto', extent=[0, 10, 1, 50], origin='lower')
        cbar = plt.colorbar(plt.cm.ScalarMappable(norm=plt.Normalize(-10, 30), cmap='viridis'), ax=ax_d, fraction=0.046, pad=0.04)
        cbar.set_label('Power Spectral Density (dB)', fontsize=8.5, fontweight='bold')
        cbar.ax.tick_params(labelsize=8)
    else:
        # Fallback synthetic spectrogram if image not accessible
        dummy_spec = np.random.uniform(-10, 30, (50, 100))
        im_plot = ax_d.imshow(dummy_spec, aspect='auto', cmap='viridis', extent=[0, 10, 1, 50], origin='lower')
        cbar = plt.colorbar(im_plot, ax=ax_d)
        cbar.set_label('Power (dB)', fontsize=8.5)

    ax_d.set_xlabel('Time (seconds)', fontsize=9, fontweight='bold')
    ax_d.set_ylabel('Frequency (Hz)', fontsize=9, fontweight='bold')
    ax_d.set_ylim(1, 50)

    # Inset badge for dataset details
    dataset_info = (
        r"$\mathbf{Spectrogram\ Corpus\ (N=106):}$" + "\n"
        r"• 67 Control Spectrograms | 39 Migraine Spectrograms" + "\n"
        r"• Clamped Range: $[-10.0, +30.0]$ dB (Viridis Colormap)" + "\n"
        r"• Resolution: $224 \times 224 \times 3$ RGB (60% Train, 40% Eval)"
    )
    ax_d.text(0.03, 0.68, dataset_info, transform=ax_d.transAxes, fontsize=7.8,
              bbox=dict(boxstyle='round,pad=0.35', facecolor='#ffffff', edgecolor='#cbd5e1', lw=1, alpha=0.92), color='#1e293b')

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('Images/dataset_preprocess_diagram.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Successfully generated high-quality Images/dataset_preprocess_diagram.png")

# ==============================================================================
# 2. HIGH-QUALITY WHOLE METHODOLOGY DIAGRAM (END-TO-END SYSTEM)
# ==============================================================================
def generate_whole_methodology_diagram():
    fig = plt.figure(figsize=(16, 10.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')

    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10.5)
    ax.axis('off')

    # Top Header Banner
    banner = FancyBboxPatch((0.4, 9.5), 15.2, 0.75, boxstyle="round,pad=0.08,rounding_size=0.12",
                            fc='#0f172a', ec='#020617', lw=1.5)
    ax.add_patch(banner)
    ax.text(8.0, 9.87, 'End-to-End Closed-Loop Wearable EEG Architecture: Diagnostic & Targeted Neuromodulation',
            ha='center', va='center', color='#ffffff', fontsize=13.5, fontweight='bold')

    # -------------------------------------------------------------------------
    # STAGE 1: EEG Input & Preprocessing (Left column: x=0.5 to 4.2)
    # -------------------------------------------------------------------------
    box1 = FancyBboxPatch((0.5, 1.2), 3.8, 7.9, boxstyle="round,pad=0.08,rounding_size=0.12",
                          fc='#f8fafc', ec='#94a3b8', lw=1.5)
    ax.add_patch(box1)
    h1 = FancyBboxPatch((0.5, 8.3), 3.8, 0.8, boxstyle="round,pad=0.08,rounding_size=0.12",
                        fc='#1e3a8a', ec='#172554', lw=1)
    ax.add_patch(h1)
    ax.text(2.4, 8.7, '1. EEG Acquisition & Preprocessing', ha='center', va='center', color='#ffffff', fontsize=10, fontweight='bold')

    # Small schematic head inside box1
    c_head = Circle((2.4, 7.3), 0.65, facecolor='#ffffff', edgecolor='#3b82f6', linewidth=1.5)
    ax.add_patch(c_head)
    # Nose & Ch #80 marker
    ax.add_patch(Polygon([[2.3, 7.95], [2.4, 8.12], [2.5, 7.95]], facecolor='#ffffff', edgecolor='#3b82f6', lw=1))
    ax.scatter([2.4], [6.8], s=60, color='#dc2626', zorder=5)
    ax.text(2.4, 6.55, 'Channel #80 (Oz/O1)', ha='center', fontsize=7.5, fontweight='bold', color='#dc2626')

    # Text details for Stage 1
    t1 = (
        "Multichannel Acquisition:\n"
        "• 128-ch BioSemi ActiveTwo (144 total)\n"
        "• 18 Migraine (12 Aura) vs 18 Controls\n"
        "• Resting-State, SSAEP, and SSVEP\n\n"
        "Standardized Conditioning:\n"
        r"• Common Average Reference: $v_i^{\mathrm{CAR}}(t) = v_i(t) - \frac{1}{128}\sum v_j(t)$" + "\n"
        "• Zero-Phase FIR Bandpass: 1.0 – 50.0 Hz\n"
        "• 60.0 Hz Notch Filter (Q = 30)\n"
        "• Extraction of Medial Occipital Ch #80"
    )
    ax.text(0.7, 6.2, t1, ha='left', va='top', fontsize=8, color='#1e293b', linespacing=1.2)

    # -------------------------------------------------------------------------
    # STAGE 2: STFT Spectrogram Generation (Middle-Left: x=4.7 to 8.2, y=5.3 to 9.1)
    # -------------------------------------------------------------------------
    box2 = FancyBboxPatch((4.7, 5.2), 3.7, 3.9, boxstyle="round,pad=0.08,rounding_size=0.12",
                          fc='#fffaf0', ec='#ea580c', lw=1.5)
    ax.add_patch(box2)
    h2 = FancyBboxPatch((4.7, 8.3), 3.7, 0.8, boxstyle="round,pad=0.08,rounding_size=0.12",
                        fc='#c2410c', ec='#9a3412', lw=1)
    ax.add_patch(h2)
    ax.text(6.55, 8.7, '2. 2D STFT Spectrograms', ha='center', va='center', color='#ffffff', fontsize=10, fontweight='bold')

    # Embed real thumbnail of spectrogram
    spectrogram_path = 'spectrograms/spectrograms/Migraine/M10_Resting.png'
    if os.path.exists(spectrogram_path):
        thumb = Image.open(spectrogram_path).resize((180, 75))
        ax.imshow(thumb, extent=[5.1, 7.9, 6.7, 7.8], origin='lower', zorder=3)
        ax.text(6.55, 6.45, 'Calibrated Viridis Image (224 x 224 x 3)', ha='center', fontsize=7.5, fontweight='bold', color='#9a3412')

    t2 = (
        "• Sliding Hann Window (L=500, R=250)\n"
        r"• $S_{\mathrm{dB}}[m,k] = 10\log_{10}(|X|^2 / P_{\mathrm{norm}})$" + "\n"
        "• Fixed display range: [-10.0, +30.0] dB\n"
        "• 106 Images (67 Control, 39 Migraine)"
    )
    ax.text(4.9, 6.25, t2, ha='left', va='top', fontsize=7.8, color='#7c2d12', linespacing=1.2)

    # Connecting arrow 1 -> 2
    ax.annotate('', xy=(4.65, 7.15), xytext=(4.35, 7.15),
                arrowprops=dict(facecolor='#1e293b', edgecolor='#0f172a', width=1.5, headwidth=5))

    # -------------------------------------------------------------------------
    # STAGE 3: Deep Transfer Learning Branch (Top-Right: x=8.8 to 15.5, y=5.2 to 9.1)
    # -------------------------------------------------------------------------
    box3 = FancyBboxPatch((8.8, 5.2), 6.7, 3.9, boxstyle="round,pad=0.08,rounding_size=0.12",
                          fc='#fef2f2', ec='#ef4444', lw=1.5)
    ax.add_patch(box3)
    h3 = FancyBboxPatch((8.8, 8.3), 6.7, 0.8, boxstyle="round,pad=0.08,rounding_size=0.12",
                        fc='#b91c1c', ec='#991b1b', lw=1)
    ax.add_patch(h3)
    ax.text(12.15, 8.7, '3. Deep Transfer Learning Diagnostic Classification', ha='center', va='center', color='#ffffff', fontsize=10, fontweight='bold')

    t3 = (
        "Model Architectures & Empirical Benchmarks:\n"
        "• EfficientNetB7: 93.75% Acc | 94.71% Prec | 93.85% F1 | 0.8750 MCC (Best)\n"
        "• VGG16: 90.63% Acc | 90.99% Prec | 90.71% F1 | 0.7985 MCC\n"
        "• ResNet50: 87.50% Acc | 88.61% Prec | 87.71% F1 | 0.7410 MCC\n"
        "• Pretrained ImageNet backbones (frozen) + GAP + Dense(128, ReLU) + Softmax(2)"
    )
    ax.text(9.0, 8.0, t3, ha='left', va='top', fontsize=8, color='#7f1d1d', linespacing=1.2)

    # Decision Diamond
    diamond = Polygon([[12.15, 6.4], [13.1, 5.85], [12.15, 5.3], [11.2, 5.85]],
                      facecolor='#fef08a', edgecolor='#ca8a04', lw=1.5, zorder=4)
    ax.add_patch(diamond)
    ax.text(12.15, 5.85, 'Interictal\nMigraine?', ha='center', va='center', fontsize=8, fontweight='bold', color='#854d0e')

    # Arrow from CNN text to Diamond
    ax.annotate('', xy=(12.15, 6.45), xytext=(12.15, 6.75),
                arrowprops=dict(facecolor='#b91c1c', edgecolor='#991b1b', width=1.5, headwidth=4))

    # Decision paths
    # Control -> Right
    ax.annotate('NO (Control)', xy=(14.2, 5.85), xytext=(13.2, 5.85),
                arrowprops=dict(facecolor='#16a34a', edgecolor='#15803d', width=1.2, headwidth=4),
                fontsize=7.5, fontweight='bold', color='#15803d', va='bottom')
    badge_c = FancyBboxPatch((14.2, 5.55), 1.2, 0.6, boxstyle="round,pad=0.04,rounding_size=0.08", fc='#dcfce7', ec='#22c55e', lw=1)
    ax.add_patch(badge_c)
    ax.text(14.8, 5.85, 'Normal Baseline\nLogged', ha='center', va='center', fontsize=7, fontweight='bold', color='#166534')

    # Migraine -> Downwards into Neuromodulation
    ax.annotate('YES (Migraine Detected)', xy=(12.15, 4.8), xytext=(12.15, 5.25),
                arrowprops=dict(facecolor='#dc2626', edgecolor='#b91c1c', width=1.8, headwidth=5),
                fontsize=8, fontweight='bold', color='#b91c1c', ha='center', va='top')

    # Connecting arrow 2 -> 3
    ax.annotate('', xy=(8.75, 7.15), xytext=(8.45, 7.15),
                arrowprops=dict(facecolor='#1e293b', edgecolor='#0f172a', width=1.5, headwidth=5))

    # -------------------------------------------------------------------------
    # STAGE 4: Analytical Colormap Inversion & Biomarkers (Middle-Bottom: x=4.7 to 10.0, y=1.2 to 4.7)
    # -------------------------------------------------------------------------
    box4 = FancyBboxPatch((4.7, 1.2), 5.4, 3.5, boxstyle="round,pad=0.08,rounding_size=0.12",
                          fc='#f0fdf4', ec='#22c55e', lw=1.5)
    ax.add_patch(box4)
    h4 = FancyBboxPatch((4.7, 4.0), 5.4, 0.7, boxstyle="round,pad=0.08,rounding_size=0.12",
                        fc='#15803d', ec='#166534', lw=1)
    ax.add_patch(h4)
    ax.text(7.4, 4.35, '4. Analytical Colormap Inversion & Biomarkers', ha='center', va='center', color='#ffffff', fontsize=9.5, fontweight='bold')

    t4 = (
        "Minimum Euclidean LUT Reconstruction:\n"
        r"• $\hat{k}(y,t) = \arg\min_k ||\mathbf{p}(y,t) - \mathbf{LUT}_k||_2^2$ (256 sRGB entries)" + "\n"
        r"• Decibel & Linear PSD: $S_{\mathrm{dB}} = -10 + 40\hat{u} \rightarrow P = 10^{S_{\mathrm{dB}}/10}\ \mu\mathrm{V}^2/\mathrm{Hz}$" + "\n"
        r"• Frequency Mapping: $f(y) = 50.0 - y \cdot (49.0 / 399.0)$ across 400 rows" + "\n\n"
        "Biomarker Extraction (Exemplar Patient M10):\n"
        "• Individual Alpha Freq (IAF): 10.09 Hz (Peak in [8.0, 13.0] Hz)\n"
        "• Alpha Deficit: 7.88% (12.12% vs. 20% normative threshold)\n"
        "• Theta-to-Alpha Ratio (TAR): 1.64 (Impaired thalamocortical pacing)"
    )
    ax.text(4.9, 3.85, t4, ha='left', va='top', fontsize=7.6, color='#14532d', linespacing=1.2)

    # Arrow from Stage 2 (Spectrogram) directly down to Stage 4 (Inversion)
    ax.annotate('', xy=(6.55, 4.75), xytext=(6.55, 5.15),
                arrowprops=dict(facecolor='#15803d', edgecolor='#166534', width=1.5, headwidth=5))

    # -------------------------------------------------------------------------
    # STAGE 5: Personalized Binaural Beat Synthesis (Bottom-Right: x=10.5 to 15.5, y=1.2 to 4.7)
    # -------------------------------------------------------------------------
    box5 = FancyBboxPatch((10.5, 1.2), 5.0, 3.5, boxstyle="round,pad=0.08,rounding_size=0.12",
                          fc='#faf5ff', ec='#a855f7', lw=1.5)
    ax.add_patch(box5)
    h5 = FancyBboxPatch((10.5, 4.0), 5.0, 0.7, boxstyle="round,pad=0.08,rounding_size=0.12",
                        fc='#7e22ce', ec='#6b21a8', lw=1)
    ax.add_patch(h5)
    ax.text(13.0, 4.35, '5. Personalized Binaural Beat Synthesis', ha='center', va='center', color='#ffffff', fontsize=9.5, fontweight='bold')

    t5 = (
        "Dichotic Pure-Tone Synthesis:\n"
        "• Carrier Tone: fc = 216.0 Hz (Warm A3, max MSO phase-locking)\n"
        "• Resonant Beat Delta: f_beat = IAF = 10.09 Hz\n"
        "  - Left Ear: f_left = 216.0 - 5.045 = 210.96 Hz\n"
        "  - Right Ear: f_right = 216.0 + 5.045 = 221.05 Hz\n"
        "• Anti-Click Taper: 1.5s squared half-cosine envelope E[n]\n"
        "• CD Quality: 16-bit 44.1 kHz Stereo WAV (5-minute session)\n\n"
        "Neurological Mechanism:\n"
        "• Brainstem Superior Olivary Complex (SOC) detects IPD\n"
        "• Drives Thalamocortical Alpha Entrainment -> Restores Gating"
    )
    ax.text(10.7, 3.85, t5, ha='left', va='top', fontsize=7.6, color='#581c87', linespacing=1.2)

    # Connecting arrow 4 -> 5
    ax.annotate('', xy=(10.45, 2.8), xytext=(10.15, 2.8),
                arrowprops=dict(facecolor='#7e22ce', edgecolor='#6b21a8', width=1.5, headwidth=5))

    # Bottom Footer Summary
    foot = FancyBboxPatch((0.5, 0.2), 15.0, 0.7, boxstyle="round,pad=0.06,rounding_size=0.1",
                          fc='#f1f5f9', ec='#cbd5e1', lw=1)
    ax.add_patch(foot)
    ax.text(8.0, 0.55, 'Closed-Loop Operating Cycle: Automated diagnostic detection via EfficientNetB7 triggers analytical RGB spectrogram inversion to\nprecisely extract patient Individual Alpha Frequencies (IAF) and synthesize tailored 216 Hz dichotic audio to reverse thalamocortical alpha deficits.',
            ha='center', va='center', fontsize=8.5, color='#334155', style='italic', linespacing=1.25)

    plt.tight_layout()
    plt.savefig('Images/whole_methodology_diagram.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Successfully generated high-quality Images/whole_methodology_diagram.png")

# ==============================================================================
# 3. HIGH-QUALITY BINAURAL BEATS GENERATION & NEUROPHYSIOLOGY DIAGRAM
# ==============================================================================
def generate_binaural_beats_diagram():
    fig = plt.figure(figsize=(16, 10.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')

    plt.suptitle('Personalized Binaural Beat Audio Synthesis & Neurophysiological Entrainment Pathway',
                 fontsize=14.5, fontweight='bold', color='#1e293b', y=0.98)

    # 4 Panels:
    # Panel A: Patient Biomarker Input (top-left)
    # Panel B: Dichotic Waveforms & Beat Envelope (top-right)
    # Panel C: Anti-Click Fade Envelope & Spectrum (bottom-left)
    # Panel D: Ascending Neurophysiological Pathway (bottom-right)

    # -------------------------------------------------------------------------
    # PANEL A: Patient M10 Biomarkers & Band Powers
    # -------------------------------------------------------------------------
    ax_a = fig.add_subplot(2, 2, 1)
    ax_a.set_title('A. Patient Biomarker Extraction (Exemplar Patient M10)', fontsize=11, fontweight='bold', pad=10, color='#0f172a')

    bands = ['Delta\n(1-4Hz)', 'Theta\n(4-8Hz)', 'Alpha\n(8-13Hz)', 'Beta\n(13-30Hz)', 'Gamma\n(30-50Hz)']
    powers = [4.15, 19.88, 12.12, 38.64, 25.21]
    colors = ['#64748b', '#f97316', '#22c55e', '#3b82f6', '#a855f7']

    bars = ax_a.bar(bands, powers, color=colors, edgecolor='#334155', linewidth=1.0, width=0.55)
    ax_a.axhline(20.0, color='#ef4444', linestyle='--', linewidth=1.5, label='Normative Alpha Baseline (20%)')

    # Annotate deficit on Alpha bar
    ax_a.annotate('Alpha Deficit: 7.88%\n(Observed: 12.12%)', xy=(2, 12.12), xytext=(2, 24),
                  arrowprops=dict(facecolor='#ef4444', edgecolor='#dc2626', shrink=0.08, width=1.2, headwidth=4),
                  fontsize=8, fontweight='bold', color='#b91c1c', ha='center',
                  bbox=dict(boxstyle='round,pad=0.3', facecolor='#fef2f2', edgecolor='#fca5a5'))

    ax_a.set_ylabel('Relative Power (%)', fontsize=9, fontweight='bold')
    ax_a.set_ylim(0, 45)
    ax_a.grid(True, axis='y', linestyle=':', alpha=0.6)
    ax_a.legend(loc='upper right', fontsize=8)

    info_a = (
        "Extracted Biomarker Profile:\n"
        "• IAF_M10: 10.09 Hz (Sharp resonance peak)\n"
        "• TAR: 19.88% / 12.12% = 1.64 (Thalamic slowing)"
    )
    ax_a.text(0.04, 0.68, info_a, transform=ax_a.transAxes, fontsize=8,
              bbox=dict(boxstyle='round,pad=0.35', facecolor='#ffffff', edgecolor='#cbd5e1', lw=1), color='#0f172a')

    # -------------------------------------------------------------------------
    # PANEL B: Dichotic Waveforms & Beat Envelope
    # -------------------------------------------------------------------------
    ax_b = fig.add_subplot(2, 2, 2)
    ax_b.set_title('B. Dichotic Pure-Tone Waveforms & Acoustic Beat Envelope', fontsize=11, fontweight='bold', pad=10, color='#0f172a')

    t_ms = np.linspace(0, 50, 1000) # 50 ms view
    t_sec = t_ms / 1000.0
    fc = 216.0
    iaf = 10.09
    f_left = fc - iaf/2  # 210.955 Hz
    f_right = fc + iaf/2 # 221.045 Hz

    s_left = 0.75 * np.sin(2 * np.pi * f_left * t_sec)
    s_right = 0.75 * np.sin(2 * np.pi * f_right * t_sec)

    ax_b.plot(t_ms, s_left, color='#0284c7', linewidth=1.4, label=f'Left Ear: {f_left:.2f} Hz (Blue)')
    ax_b.plot(t_ms, s_right, color='#ef4444', linewidth=1.3, linestyle='--', label=f'Right Ear: {f_right:.2f} Hz (Red)')

    # Beat envelope over a wider window (200 ms to see beating clearly)
    t_wide = np.linspace(0, 50, 1000)
    envelope = 0.75 * np.abs(np.cos(np.pi * iaf * (t_wide / 1000.0)))
    ax_b.plot(t_wide, envelope, color='#0f172a', linewidth=1.8, linestyle=':', label='Perceived Beat Envelope (10.09 Hz)')

    ax_b.set_xlabel('Time (milliseconds)', fontsize=9, fontweight='bold')
    ax_b.set_ylabel('Normalized Amplitude', fontsize=9, fontweight='bold')
    ax_b.set_ylim(-0.95, 1.15)
    ax_b.grid(True, linestyle=':', alpha=0.6)
    ax_b.legend(loc='upper right', fontsize=7.8, ncol=2)

    # -------------------------------------------------------------------------
    # PANEL C: Anti-Click Fade Envelope & Acoustic Headroom
    # -------------------------------------------------------------------------
    ax_c = fig.add_subplot(2, 2, 3)
    ax_c.set_title('C. Anti-Click Squared Half-Cosine Fade Envelope ($E[n]$)', fontsize=11, fontweight='bold', pad=10, color='#0f172a')

    t_fade = np.linspace(0, 5.0, 1000)
    T_fade = 1.5
    T_total = 5.0
    env = np.ones_like(t_fade)
    # Fade in: sin^2(pi*t / (2*T_fade))
    idx_in = t_fade < T_fade
    env[idx_in] = np.sin(np.pi * t_fade[idx_in] / (2 * T_fade))**2
    # Fade out: cos^2(pi*(t - (T_total - T_fade)) / (2*T_fade))
    idx_out = t_fade > (T_total - T_fade)
    env[idx_out] = np.cos(np.pi * (t_fade[idx_out] - (T_total - T_fade)) / (2 * T_fade))**2

    ax_c.plot(t_fade, env, color='#16a34a', linewidth=2.2, label='1.5s Squared Half-Cosine Envelope E[n]')
    ax_c.fill_between(t_fade, 0, env, color='#dcfce7', alpha=0.5)

    ax_c.axvline(1.5, color='#94a3b8', linestyle=':', label='Onset Fade End (1.5s)')
    ax_c.axvline(3.5, color='#94a3b8', linestyle=':', label='Offset Fade Start (3.5s)')

    ax_c.set_xlabel('Prescription Duration (seconds)', fontsize=9, fontweight='bold')
    ax_c.set_ylabel('Amplitude Multiplier', fontsize=9, fontweight='bold')
    ax_c.set_ylim(0, 1.15)
    ax_c.grid(True, linestyle=':', alpha=0.6)
    ax_c.legend(loc='lower center', fontsize=8, ncol=3)

    fade_text = (
        "Anti-Click Windowing Rationale:\n"
        "• Sudden audio switching creates high-frequency spectral splatter (>500 Hz)\n"
        "• Triggers startle reflexes and pain in photophobic/phonophobic migraineurs\n"
        "• Smooth sin^2 taper provides gentle transition and preserves acoustic safety"
    )
    ax_c.text(0.04, 0.45, fade_text, transform=ax_c.transAxes, fontsize=8,
              bbox=dict(boxstyle='round,pad=0.35', facecolor='#ffffff', edgecolor='#cbd5e1', lw=1), color='#14532d')

    # -------------------------------------------------------------------------
    # PANEL D: Ascending Neurophysiological Pathway Diagram
    # -------------------------------------------------------------------------
    ax_d = fig.add_subplot(2, 2, 4)
    ax_d.set_title('D. Ascending Neurophysiological Auditory Entrainment Pathway', fontsize=11, fontweight='bold', pad=10, color='#0f172a')
    ax_d.set_xlim(0, 10)
    ax_d.set_ylim(0, 10)
    ax_d.axis('off')

    # Draw schematic vertical brainstem & cortical stages
    levels = [
        ('1. Dichotic Delivery', 'Stereo Headphones deliver pure tones:\nLeft: 210.96 Hz | Right: 221.05 Hz', 8.5, '#eff6ff', '#2563eb'),
        ('2. Cochlea & CN VIII', 'Cochleae transduce acoustics into\nauditory nerve action potentials', 6.6, '#f0fdf4', '#16a34a'),
        ('3. Superior Olivary Complex (MSO)', 'Medial Superior Olive in Pons detects\nInteraural Phase Disparity; fires at 10.09 Hz', 4.7, '#fff7ed', '#ea580c'),
        ('4. Inferior Colliculus & Thalamus', 'Brainstem pathway relays 10.09 Hz FFR\nto Medial Geniculate Body (Thalamus)', 2.8, '#fdf2f8', '#db2777'),
        ('5. Cortical Resonance & Recovery', 'Thalamocortical alpha pacing restored;\nSensory gating recovered; hyperexcitability mitigated', 0.9, '#faf5ff', '#9333ea')
    ]

    for title, desc, y_pos, bg_c, ec_c in levels:
        card = FancyBboxPatch((0.5, y_pos - 0.65), 9.0, 1.3, boxstyle="round,pad=0.06,rounding_size=0.1",
                              fc=bg_c, ec=ec_c, lw=1.5)
        ax_d.add_patch(card)
        ax_d.text(0.8, y_pos + 0.35, title, fontsize=8.5, fontweight='bold', color=ec_c, va='center')
        ax_d.text(0.8, y_pos - 0.15, desc, fontsize=7.8, color='#1e293b', va='center', linespacing=1.15)

    # Connecting arrows between levels
    for y_arrow in [7.75, 5.85, 3.95, 2.05]:
        ax_d.annotate('', xy=(5.0, y_arrow - 0.35), xytext=(5.0, y_arrow + 0.05),
                      arrowprops=dict(facecolor='#475569', edgecolor='#1e293b', width=1.2, headwidth=4))

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('Images/binaural_beats_diagram.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Successfully generated high-quality Images/binaural_beats_diagram.png")

if __name__ == '__main__':
    generate_dataset_preprocess_diagram()
    generate_whole_methodology_diagram()
    generate_binaural_beats_diagram()
