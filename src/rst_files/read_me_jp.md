## はじめに
このpythonパッケージはハミルトニアンがPauli行列積の線型結合で
表現できる場合に量子回路上で再現する手法、Block-Encoding法を
実行するものである。\
このプログラムでは量子コンピュータ向け量子化学計算パッケージである[Openfermion](https://github.com/quantumlib/OpenFermion)や量子コンピュータシミュレータの[Qulacs](https://github.com/qulacs/qulacs)（推奨）または[Qiskit](https://github.com/Qiskit/qiskit)の利用を前提としているので利用する際には
これらのパッケージのダウンロードを強く推奨する。\
本プログラムの一部の作成にはXANADA社の開発した[PennyLane](https://github.com/PennyLaneAI/pennylane)というライブラリの実行結果を参考にした。

## 利用方法
~~利用方法はdocsファイルをダウンロードしてもらいindex.htmlを開いて欲しい。
詳しくはそこに記載してある。注意点としてこのライブラリ内からアクセスできる
github pageは同様のことが記載されているが、
現在筆者の想定した通りの表示ができていない。
今後の修正度合いに応じて新しい発表を行うので今はアクセスしないことを強く勧める~~
本パッケージはフォルダ`PItBE`ごと、あるいはフォルダ`src`内のフォルダ`pitbe`のみをgithubを介して手持ちの端末にリポジトリを複製して利用することを推奨する。\
Block-Encoding法の理論及び`pitbe`に含まれている関数についての説明は本パッケージの[Github pages](https://b-reo.github.io/PItBE/)に記述してあるため、一読することを推奨する。`pitbe`に含まれている関数についてはフォルダ`src/rst_files`に存在する関数名と同じ名前のjupyter notebookでも参照可能。\
実際の利用方法の見本として[github pages](https://b-reo.github.io/PItBE/)に`Demo Play`という章を用意してあるので、そちらも一読することを推奨する。\
なお本ページに含まれているフォルダのうち`pitbe`及び`src`以外のファイルについては実行上無視してもらっても構わない。

## 最後に
本プログラムはまだまだ荒削りであり、利用者にとって扱いやすいものであるとは
到底言える状態ではない。しかしそれは更なる発展が見込まれることを
同時に示唆している。今後のアップデートに期待してほしい。

## 更新情報
### 2025/06/20 更新
関数"mat_maker"を実装。同時にgithub pageにおける関数"mat_make"についての記述を関数"mat_maker"に変更。\
関数"mat_make"で生じていたユニタリ行列が正しく生成されない問題を解決。\
今後は"mat_make"を使用せず、"mat_maker"を使用することを強く推奨する。\
関数"read_general"を実装。\
関数"read_jw"では対応できなかったOpenfermionによるBravyi変換結果にも対応できるように改良。\
"read_jw"の完全上位互換版であるので"read_general"への移行を強く推奨。\
関数"qiskit_circ_make"を実装。\
QiskitにおいてもPItBEを用いたBlock-Encodingを実行可能になった。\
ただ製作者の環境ではQulacsの方が実行時間は短かった。\
github pagesの不具合のうち大部分を解消、再度公開。\
ただし、"circ_make"及び"qiskit_circ_make"のページにおいて画像が読み込まれないことは未だ解消されていない。\
これらのページについては"src/rst_files"中に存在する"circ_make.ipynb"または"qiskit_circ_make.ipynb"を参考にしてほしい。

### 2025/06/25 更新
READMEの内容のうち利用方法の部分を更新。

### 2025/06/26　　更新
[github pages](https://b-reo.github.io/PItBE/)に利用方法を説明するページ`Demo Play`を掲載。

### 2025/06/30 更新
[github pages](https://b-reo.github.io/PItBE/)にBlock-Encoding法及びPItBEを説明するページ`What is Block-Encoding and PItBE`にてBlock-Encoding法の理論的背景を解説するページの日本語版を公開。\
`PItBE`についての説明及び英語版は今後の更新で公開予定。

### 2025/07/01　更新
`PItBE`についての説明を行うページの公開。