日本語版
=====================================

本モジュール'PItBE'はBE法の実行用モジュールであり、本モジュールを用いることで
簡単にBE法を実行することができる。また本モジュールはBE法の更なる普及を目指し、
BE法の理論的背景を解説したテキストを付属する。
日本語でBE法を解説したものはまだまだ数少ないので、付属テキストを用いて
BE法についての見識を深めることを期待する。

本テキストは以下の章によって構成されている。

1. Read me：日本語版Readme、本パッケージの日本語版更新情報はここに掲載
2. Block-Encoding法について：Block-Encoding法についての理論的解説を行う
3. PItBEについて：本モジュールの概説及び実行上の推奨環境
4. 関数について：本モジュールに含まれている関数についての個別ページ
5. デモプレイ：本モジュールを用いたBlock-Encoding法の実践

なお、本テキストについては量子コンピュータについての基礎的な知識や、
古典コンピュータ上で実行可能な量子コンピュータシミュレータが
実行可能であることを前提としている。これらの知識が不十分である場合
`このサイト <https://dojo.qulacs.org/ja/latest/index.html>`_
で知識を身につけることを推奨する。
量子コンピュータの基礎知識からシミュレータの実行方法に至るまで、
丁寧に解説されているので初学者に適している。

.. toctree::
   :maxdepth: 1
   :caption: Read me:

   ../read_me_jp

.. toctree::
   :maxdepth: 1
   :caption: Block-Encoding法について:

   ../ipynb/jpn/describe_be.ipynb

.. toctree::
   :maxdepth: 1
   :caption: PItBEについて:

   ../ipynb/jpn/describe_pitbe.ipynb

.. toctree::
   :maxdepth: 1
   :caption: 関数について

   ../ipynb/jpn/circ_make.ipynb
   ../ipynb/jpn/coeff_make.ipynb
   ../ipynb/jpn/cont_order.ipynb
   ../ipynb/jpn/mat_maker.ipynb
   ../ipynb/jpn/normalize.ipynb
   ../ipynb/jpn/qiskit_circ_make.ipynb
   ../ipynb/jpn/read_general.ipynb
   ../ipynb/jpn/read_jw.ipynb
   ../ipynb/jpn/total_search.ipynb
   ../ipynb/jpn/vec_make.ipynb

.. toctree::
   :maxdepth: 1
   :caption: デモプレイ

   ../ipynb/jpn/demo_use.ipynb