Speech Deepfake Detection in Real-Time Communication:Dataset, Analysis, and Phoneme-Guided Consistency Learning
====================

.. raw:: html

    <style>
    body {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        color: #000000;
        background-color: #ffffff;
        line-height: 1.6;
        margin: 0;
        padding: 0;
        text-align: center; 
    }
    
    .main-container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 40px 20px;
        text-align: left; 
        box-sizing: border-box;
    }
    
    .paper-title {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin: 0 0 10px 0;
        padding: 0;
    }
    
    .author-info {
        text-align: center;
        font-size: 16px;
        font-style: italic;
        margin: 0 0 30px 0;
        color: #555;
    }
    
    .dataset-title {
        font-size: 22px;
        font-weight: bold;
        margin: 30px 0 20px 0;
        padding: 0;
        text-align: left;
        color: #000;
    }
    
    .section-title {
        font-size: 20px;
        font-weight: bold;
        margin: 40px 0 20px 0;
        padding: 0 0 8px 0;
        text-align: left;
        color: #000;
    }
    
    .subsection-title {
        font-size: 18px;
        font-weight: bold;
        margin: 30px 0 15px 0;
        padding: 0;
        text-align: left;
        color: #444;
    }
    
    .table-title {
        font-size: 16px;
        font-weight: bold;
        margin: 25px 0 10px 0;
        padding: 0;
        text-align: left;
        color: #333;
    }
    
    .scrollable-container {
        width: 100%;
        overflow-x: auto;
        overflow-y: hidden;
        margin: 20px 0 40px 0;
        -webkit-overflow-scrolling: touch;
        border: none !important; 
    }
    
    .compact-table {
        width: auto;
        min-width: 100%;
        border-collapse: collapse;
        font-size: 14px;
        white-space: nowrap;
        margin-bottom: 20px;
        border: none !important;
    }
    
    .compact-table th {
        background-color: #f5f5f5;
        padding: 12px 10px;
        text-align: center;
        font-weight: bold;
        color: #000;
        vertical-align: middle;
        min-width: 120px;
        border: none !important; 
    }
    
    .compact-table td {
        padding: 10px 8px;
        text-align: center;
        vertical-align: top;
        color: #000;
        min-width: 120px;
        border: none !important; 
    }
    
    .compact-table .audio-cell {
        min-width: 200px;
        border: none !important;
    }
    
    .compact-table .spectrogram-cell {
        min-width: 280px;
        border: none !important;
    }
    
    .audio-player {
        margin: 8px 0;
    }
    
    .audio-player audio {
        width: 200px;
        height: 35px;
        border-radius: 4px;
    }
    
    .spectrogram-img {
        width: 280px;
        height: auto;
        max-height: 140px;
        margin: 8px 0;
        border: none !important; 
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    .lang-row {
        background-color: #fafafa;
    }
    
    .empty-cell {
        color: #999;
        font-style: italic;
        background-color: #f9f9f9;
    }
    
    .row-label {
        font-weight: bold;
        background-color: #f0f0f0;
        text-align: left;
        padding-left: 15px !important;
        border: none !important;
    }
    
    .compact-table tbody tr:nth-child(even) {
        background-color: #fafafa;
    }
    
    .compact-table tbody tr:hover {
        background-color: #f5f5f5;
    }
    
    .overview-text {
        font-size: 16px;
        line-height: 1.7;
        margin: 30px 0 50px 0;
        text-align: justify;
    }
    
    .section-divider {
        display: none !important;
    }
    </style>

    <div class="main-container">
    <p class="author-info">Anonymous ACL submission</p>
    
    <h2 class="dataset-title">Overview</h2>
    
    <div class="overview-text">
        The RTCFake dataset is a first-of-its-kind, large-scale speech deepfake collection specifically designed for real-time communication (RTC) scenarios, comprising approximately 600 hours of speech and covering 307 speakers. While existing research primarily relies on offline simulations, this dataset addresses that limitation by providing precisely paired "offline-online" samples transmitted through seven mainstream platforms, including QQ, Zoom, WeChat, etc. This dataset captures the complex, nonlinear distortions introduced by real-world "black-box" transmission, such as unknown noise suppression, echo cancellation and codec compression, providing a robust benchmark for evaluating detection models under realistic communication conditions.
    </div>
    
    <h2 class="section-title">Demos</h2>
    
    <h3 class="subsection-title">Offline Speech</h3>
    
    <h4 class="table-title">Training Subset</h4>
    
    <div class="scrollable-container">
        <table class="compact-table">
            <thead>
                <tr>
                    <th></th>
                    <th>Real</th>
                    <th>F5-TTS</th>
                    <th>OpenAudio-S1</th>
                    <th>VOXCPM</th>
                    <th>LLaSA</th>
                    <th>CosyVoice</th>
                    <th>SeedVC</th>
                </tr>
            </thead>
            <tbody>
                <!-- Chinese -->
                <tr class="lang-row">
                    <td class="row-label">Chinese</td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/train/CN/058_21_M_LY_177_real.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/train/CN/058_21_M_LY_177_F5-TTS.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/train/CN/058_21_M_LY_177_OpenAudio-S1-mini.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/train/CN/058_21_M_LY_177_VOXCPM.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/train/CN/058_21_M_LY_177_LLaSA.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="empty-cell">-</td>
                    <td class="empty-cell">-</td>
                </tr>
                <!-- English -->
                <tr class="lang-row">
                    <td class="row-label">English</td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/train/EN/100_F_02_baum_sea_fairi_48_real.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/train/EN/100_F_02_baum_sea_fairi_48_F5-TTS.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/train/EN/100_F_02_baum_sea_fairi_48_OpenAudio-S1-mini.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/train/EN/100_F_02_baum_sea_fairi_48_VOXCPM.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="empty-cell">-</td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/2_VC/train/EN/100_F_02_baum_sea_fairi_48_CosyVoice.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/2_VC/train/EN/100_F_02_baum_sea_fairi_48_SeedVC.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    
    <h4 class="table-title">Development Subset</h4>
    
    <div class="scrollable-container">
        <table class="compact-table">
            <thead>
                <tr>
                    <th></th>
                    <th>Real</th>
                    <th>F5-TTS</th>
                    <th>OpenAudio-S1</th>
                    <th>VOXCPM</th>
                    <th>LLaSA</th>
                    <th>CosyVoice</th>
                    <th>SeedVC</th>
                </tr>
            </thead>
            <tbody>
                <!-- Chinese -->
                <tr class="lang-row">
                    <td class="row-label">Chinese</td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/dev/CN/060_31_F_ZX_003_real.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/dev/CN/060_31_F_ZX_003_F5-TTS.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/dev/CN/060_31_F_ZX_003_OpenAudio-S1-mini.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/dev/CN/060_31_F_ZX_003_VOXCPM.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/dev/CN/060_31_F_ZX_003_LLaSA.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="empty-cell">-</td>
                    <td class="empty-cell">-</td>
                </tr>
                <!-- English -->
                <tr class="lang-row">
                    <td class="row-label">English</td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/dev/EN/3318_F_linco_353_willi_10_real.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/dev/EN/3318_F_linco_353_willi_10_F5-TTS.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/dev/EN/3318_F_linco_353_willi_10_OpenAudio-S1-mini.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/dev/EN/3318_F_linco_353_willi_10_VOXCPM.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="empty-cell">-</td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/2_VC/dev/EN/3318_F_linco_353_willi_10_CosyVoice.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/2_VC/dev/EN/3318_F_linco_353_willi_10_SeedVC.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    
    <h4 class="table-title">Evaluation Subset</h4>
    
    <div class="scrollable-container">
        <table class="compact-table">
            <thead>
                <tr>
                    <th></th>
                    <th>Real</th>
                    <th>F5-TTS</th>
                    <th>OpenAudio-S1</th>
                    <th>VOXCPM</th>
                    <th>LLaSA</th>
                    <th>IndexTTS2</th>
                    <th>Doubao</th>
                    <th>SparkTTS</th>
                    <th>CosyVoice</th>
                    <th>SeedVC</th>
                    <th>ChatterboxVC</th>
                </tr>
            </thead>
            <tbody>
                <!-- Chinese -->
                <tr class="lang-row">
                    <td class="row-label">Chinese</td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/test/CN/081_24_F_JKYS_070_real.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/test/CN/081_24_F_JKYS_070_F5-TTS.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/test/CN/081_24_F_JKYS_070_OpenAudio-S1-mini.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/test/CN/081_24_F_JKYS_070_VOXCPM.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/test/CN/081_24_F_JKYS_070_LLaSA.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/test/CN/081_24_F_JKYS_070_IndexTTS2.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="empty-cell">-</td>
                    <td class="empty-cell">-</td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/2_VC/test/CN/081_24_F_JKYS_070_CosyVoice.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/2_VC/test/CN/081_24_F_JKYS_070_SeedVC.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/2_VC/test/CN/081_24_F_JKYS_070_ChatterboxVC.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                </tr>
                <!-- English -->
                <tr class="lang-row">
                    <td class="row-label">English</td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/test/EN/2827_M_furth_04_defoe_62_real.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/test/EN/2827_M_furth_04_defoe_62_F5-TTS.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/test/EN/2827_M_furth_04_defoe_62_OpenAudio-S1-mini.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/test/EN/2827_M_furth_04_defoe_62_VOXCPM.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/test/EN/2827_M_furth_04_defoe_62_LLaSA.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/test/EN/2827_M_furth_04_defoe_62_IndexTTS2.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/test/EN/2827_M_furth_04_defoe_62_Doubao-Seed-TTS2.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/1_TTS/test/EN/2827_M_furth_04_defoe_62_SparkTTS.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/2_VC/test/EN/2827_M_furth_04_defoe_62_CosyVoice.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/2_VC/test/EN/2827_M_furth_04_defoe_62_SeedVC.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                    <td class="audio-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/offline/2_VC/test/EN/2827_M_furth_04_defoe_62_ChatterboxVC.wav" type="audio/wav">
                            </audio>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    
    <div class="section-divider"></div>
    
    <h3 class="subsection-title">Paired Offline-online Speech</h3>
    
    <h4 class="table-title">Comparison of Identical Real and Fake Utterances Across Multiple Transmission Platforms</h4>
    
    <div class="scrollable-container">
        <table class="compact-table">
            <thead>
                <tr>
                    <th></th>
                    <th>Offline</th>
                    <th>QQ</th>
                    <th>Zoom</th>
                    <th>DingTalk</th>
                    <th>Tencent<br>Meeting</th>
                    <th>Lark</th>
                    <th>WeChat</th>
                    <th>Telegram</th>
                </tr>
            </thead>
            <tbody>
                <!-- Real Row -->
                <tr>
                    <td class="row-label">Real</td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/1_real-fake/real/130_42_M_TY_252_real.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/1_real-fake/real/130_42_M_TY_252_real.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/1_real-fake/real/130_42_M_TY_252_real_qq.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/1_real-fake/real/130_42_M_TY_252_real_qq.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/1_real-fake/real/130_42_M_TY_252_real_zoom.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/1_real-fake/real/130_42_M_TY_252_real_zoom.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/1_real-fake/real/130_42_M_TY_252_real_dingding.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/1_real-fake/real/130_42_M_TY_252_real_dingding.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/1_real-fake/real/130_42_M_TY_252_real_txhy.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/1_real-fake/real/130_42_M_TY_252_real_txhy.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/1_real-fake/real/130_42_M_TY_252_real_feishu.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/1_real-fake/real/130_42_M_TY_252_real_feishu.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/1_real-fake/real/130_42_M_TY_252_real_wechat.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/1_real-fake/real/130_42_M_TY_252_real_wechat.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/1_real-fake/real/130_42_M_TY_252_real_telegram.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/1_real-fake/real/130_42_M_TY_252_real_telegram.png" alt="Spectrogram">
                    </td>
                </tr>
                <!-- Fake Row -->
                <tr>
                    <td class="row-label">Fake (IndexTTS2)</td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/1_real-fake/fake-IndexTTS2/130_42_M_TY_252_IndexTTS2.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/1_real-fake/fake-IndexTTS2/130_42_M_TY_252_IndexTTS2.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/1_real-fake/fake-IndexTTS2/130_42_M_TY_252_IndexTTS2_qq.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/1_real-fake/fake-IndexTTS2/130_42_M_TY_252_IndexTTS2_qq.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/1_real-fake/fake-IndexTTS2/130_42_M_TY_252_IndexTTS2_zoom.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/1_real-fake/fake-IndexTTS2/130_42_M_TY_252_IndexTTS2_zoom.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/1_real-fake/fake-IndexTTS2/130_42_M_TY_252_IndexTTS2_dingding.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/1_real-fake/fake-IndexTTS2/130_42_M_TY_252_IndexTTS2_dingding.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/1_real-fake/fake-IndexTTS2/130_42_M_TY_252_IndexTTS2_txhy.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/1_real-fake/fake-IndexTTS2/130_42_M_TY_252_IndexTTS2_txhy.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/1_real-fake/fake-IndexTTS2/130_42_M_TY_252_IndexTTS2_feishu.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/1_real-fake/fake-IndexTTS2/130_42_M_TY_252_IndexTTS2_feishu.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/1_real-fake/fake-IndexTTS2/130_42_M_TY_252_IndexTTS2_wechat.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/1_real-fake/fake-IndexTTS2/130_42_M_TY_252_IndexTTS2_wechat.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/1_real-fake/fake-IndexTTS2/130_42_M_TY_252_IndexTTS2_telegram.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/1_real-fake/fake-IndexTTS2/130_42_M_TY_252_IndexTTS2_telegram.png" alt="Spectrogram">
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    
    <h4 class="table-title">Comparison of Identical Clean and Noisy Utterances Across Multiple Transmission Platforms</h4>
    
    <div class="scrollable-container">
        <table class="compact-table">
            <thead>
                <tr>
                    <th></th>
                    <th>Offline</th>
                    <th>QQ</th>
                    <th>Zoom</th>
                    <th>DingTalk</th>
                    <th>Tencent<br>Meeting</th>
                    <th>Lark</th>
                    <th>WeChat</th>
                    <th>Telegram</th>
                </tr>
            </thead>
            <tbody>
                <!-- Clean Row -->
                <tr>
                    <td class="row-label">Clean</td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/2_clean-noisy/real_clean/3588_F_theam_07_anony_56_real.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/2_clean-noisy/real_clean/3588_F_theam_07_anony_56_real.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/2_clean-noisy/real_clean/3588_F_theam_07_anony_56_real_qq.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/2_clean-noisy/real_clean/3588_F_theam_07_anony_56_real_qq.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/2_clean-noisy/real_clean/3588_F_theam_07_anony_56_real_zoom.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/2_clean-noisy/real_clean/3588_F_theam_07_anony_56_real_zoom.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/2_clean-noisy/real_clean/3588_F_theam_07_anony_56_real_dingding.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/2_clean-noisy/real_clean/3588_F_theam_07_anony_56_real_dingding.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/2_clean-noisy/real_clean/3588_F_theam_07_anony_56_real_tencentmeeting.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/2_clean-noisy/real_clean/3588_F_theam_07_anony_56_real_tencentmeeting.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/2_clean-noisy/real_clean/3588_F_theam_07_anony_56_real_feishu.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/2_clean-noisy/real_clean/3588_F_theam_07_anony_56_real_feishu.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/2_clean-noisy/real_clean/3588_F_theam_07_anony_56_real_wechat.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/2_clean-noisy/real_clean/3588_F_theam_07_anony_56_real_wechat.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/2_clean-noisy/real_clean/3588_F_theam_07_anony_56_real_telegram.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/2_clean-noisy/real_clean/3588_F_theam_07_anony_56_real_telegram.png" alt="Spectrogram">
                    </td>
                </tr>
                <!-- Noisy Row -->
                <tr>
                    <td class="row-label">Noisy (Rain)</td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/2_clean-noisy/real_noisy/3588_F_theam_07_anony_56_real_rain.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/2_clean-noisy/real_noisy/3588_F_theam_07_anony_56_real_rain.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/2_clean-noisy/real_noisy/3588_F_theam_07_anony_56_real_rain_qq.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/2_clean-noisy/real_noisy/3588_F_theam_07_anony_56_real_rain_qq.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/2_clean-noisy/real_noisy/3588_F_theam_07_anony_56_real_rain_zoom.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/2_clean-noisy/real_noisy/3588_F_theam_07_anony_56_real_rain_zoom.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/2_clean-noisy/real_noisy/3588_F_theam_07_anony_56_real_rain_dingding.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/2_clean-noisy/real_noisy/3588_F_theam_07_anony_56_real_rain_dingding.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/2_clean-noisy/real_noisy/3588_F_theam_07_anony_56_real_rain_tencentmeeting.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/2_clean-noisy/real_noisy/3588_F_theam_07_anony_56_real_rain_tencentmeeting.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/2_clean-noisy/real_noisy/3588_F_theam_07_anony_56_real_rain_feishu.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/2_clean-noisy/real_noisy/3588_F_theam_07_anony_56_real_rain_feishu.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/2_clean-noisy/real_noisy/3588_F_theam_07_anony_56_real_rain_wechat.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/2_clean-noisy/real_noisy/3588_F_theam_07_anony_56_real_rain_wechat.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/2_clean-noisy/real_noisy/3588_F_theam_07_anony_56_real_rain_telegram.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/2_clean-noisy/real_noisy/3588_F_theam_07_anony_56_real_rain_telegram.png" alt="Spectrogram">
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    
    <h4 class="table-title">Utterances with Different Noises Transmitted through the Same Platform (Lark)</h4>
    
    <div class="scrollable-container">
        <table class="compact-table">
            <thead>
                <tr>
                    <th></th>
                    <th>Noise_keyboard</th>
                    <th>Noise_footsteps</th>
                    <th>Noise_rain</th>
                    <th>Noise_coffee</th>
                    <th>Noise_office</th>
                    <th>Echo</th>
                </tr>
            </thead>
            <tbody>
                <!-- Offline Row -->
                <tr>
                    <td class="row-label">Offline</td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/3_noisy_lark/noise_keyboard/2910_F_millo_32_eliot_39_IndexTTS2_keyboard.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/3_noisy_lark/noise_keyboard/2910_F_millo_32_eliot_39_IndexTTS2_keyboard.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/3_noisy_lark/noise_footsteps/204_M_lone_star_range_01_grey_58_real_footsteps.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/3_noisy_lark/noise_footsteps/204_M_lone_star_range_01_grey_58_real_footsteps.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/3_noisy_lark/noise_rain/2827_M_furth_01_defoe_82_LLaSA_rain.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/3_noisy_lark/noise_rain/2827_M_furth_01_defoe_82_LLaSA_rain.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/3_noisy_lark/noise_coffee/2039_M_outar_wilso_ae_120_real_coffee.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/3_noisy_lark/noise_coffee/2039_M_outar_wilso_ae_120_real_coffee.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/3_noisy_lark/noise_office/3657_M_camil_19_dumas_13_OpenAudio-S1-mini_office.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/3_noisy_lark/noise_office/3657_M_camil_19_dumas_13_OpenAudio-S1-mini_office.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/3_noisy_lark/echo/1867_F_warni_from_the_stars_cocki_rd_101_F5-TTS_echo.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/3_noisy_lark/echo/1867_F_warni_from_the_stars_cocki_rd_101_F5-TTS_echo.png" alt="Spectrogram">
                    </td>
                </tr>
                <!-- Online (Lark) Row -->
                <tr>
                    <td class="row-label">Online (Lark)</td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/3_noisy_lark/noise_keyboard/2910_F_millo_32_eliot_39_IndexTTS2_keyboard_feishu.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/3_noisy_lark/noise_keyboard/2910_F_millo_32_eliot_39_IndexTTS2_keyboard_feishu.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/3_noisy_lark/noise_footsteps/204_M_lone_star_range_01_grey_58_real_footsteps_feishu.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/3_noisy_lark/noise_footsteps/204_M_lone_star_range_01_grey_58_real_footsteps_feishu.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/3_noisy_lark/noise_rain/2827_M_furth_01_defoe_82_LLaSA_rain_feishu.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/3_noisy_lark/noise_rain/2827_M_furth_01_defoe_82_LLaSA_rain_feishu.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/3_noisy_lark/noise_coffee/2039_M_outar_wilso_ae_120_real_coffee_feishu.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/3_noisy_lark/noise_coffee/2039_M_outar_wilso_ae_120_real_coffee_feishu.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/3_noisy_lark/noise_office/3657_M_camil_19_dumas_13_OpenAudio-S1-mini_office_feishu.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/3_noisy_lark/noise_office/3657_M_camil_19_dumas_13_OpenAudio-S1-mini_office_feishu.png" alt="Spectrogram">
                    </td>
                    <td class="spectrogram-cell">
                        <div class="audio-player">
                            <audio controls preload="none">
                                <source src="_static/audio/wav_demo/online/3_noisy_lark/echo/1867_F_warni_from_the_stars_cocki_rd_101_F5-TTS_echo_feishu.wav" type="audio/wav">
                            </audio>
                        </div>
                        <img class="spectrogram-img" src="_static/spectrograms_color/online/3_noisy_lark/echo/1867_F_warni_from_the_stars_cocki_rd_101_F5-TTS_echo_feishu.png" alt="Spectrogram">
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    
    </div> <!-- End of main-container -->