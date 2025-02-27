"""
FreakQuest 分析ツール

予期せぬ周波数パターンの中に隠された謎を探求する実験プロジェクトです。
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_signal(duration=1.0, sampling_rate=44100):
    """
    ランダムな正弦波2つで構成された信号を生成します。
    """
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    freq1 = np.random.uniform(50, 2000) 
    freq2 = np.random.uniform(50, 2000)
    signal = np.sin(2 * np.pi * freq1 * t) + 0.5 * np.sin(2 * np.pi * freq2 * t)
    return t, signal, freq1, freq2

def analyze_signal(signal, sampling_rate=44100):
    """
    高速フーリエ変換を使って信号を解析します。
    """
    fft_result = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), 1/sampling_rate)
    power = np.abs(fft_result)**2
    return freqs, power

def plot_spectrum(freqs, power, freq1, freq2):
    """
    信号のパワースペクトルをプロットします。
    """
    plt.figure(figsize=(10, 6))
    half = len(freqs) // 2  
    plt.plot(freqs[:half], power[:half], color='purple')
    plt.title("FreakQuest 周波数スペクトル")
    plt.xlabel("周波数 (Hz)")
    plt.ylabel("パワー")
    plt.axvline(x=freq1, color='red', linestyle='--', label=f'周波数1: {freq1:.2f} Hz')
    plt.axvline(x=freq2, color='green', linestyle='--', label=f'周波数2: {freq2:.2f} Hz')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("FreakQuest 分析ツールへようこそ。")
    print("ここで何をしているのか？探求してみてください…")
    
    t, signal, freq1, freq2 = generate_signal()
    print(f"信号が生成されました: 周波数1 = {freq1:.2f} Hz, 周波数2 = {freq2:.2f} Hz")
    
    freqs, power = analyze_signal(signal)
    plot_spectrum(freqs, power, freq1, freq2)
    
    print("分析完了。君は何を見つける？")

if __name__ == "__main__":
    main()
