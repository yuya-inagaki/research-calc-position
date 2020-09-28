# What's this code?
視覚的顕著性マップ作成のためのユーザー実験で得たユーザーの視線情報から位置情報を計算するプログラム

## About data
Tobii eyetrackerで取得したデータに関する重要項目

**[AH] Event Column**
| イベント内容 | イベント名 |
|---|---|
| レコーディング開始 | `RecordingStart` |
| レコーディング終了 | `RecordingEnd` |
| キャリブレーション開始 | `Eye tracker Calibration start` |
| キャリブレーション終了 | `Eye tracker Calibration end` |
| ウェブページ閲覧開始 | `ImageStimulusStart` |
| ウェブページ閲覧終了 | `ImageStimulusEnd` |
|---|---|
| マウスイベント発生 | `MouseEvent` |

**[AI] Event value**
| イベント内容 | イベント名 |
|---|---|
| 黒背景閲覧 | `black` |
| ウェブページ閲覧（サイト名） | `C01-01-PASMO etc.` |
| マウスイベント | `Down, Left, Up, Right` |

**[BP] Presented Stimulus name**
| イベント内容 | イベント名 |
|---|---|
| キャリブレーション | `Eyetracker Calibration` |
| 黒背景閲覧 | `black` |
| ウェブページ閲覧（サイト名） | `C01-01-PASMO etc.` |

**[BQ] Presented Media name**
| イベント内容 | イベント名 |
|---|---|
| 黒背景ファイル名 | `black.jpg` |
| ウェブページファイル名 | `C01-01-PASMO.png etc.` |


**Fixation point**
| カラム数 | カラム名 | イベント名 |
|---|---|---|
| CA | Fixation point X | X座標の視線座標 |
| CB | Fixation point Y | Y座標の視線座標 |