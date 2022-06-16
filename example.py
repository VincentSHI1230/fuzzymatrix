# 以作业 4 第 2 题为例
import fuzzymatrix as fm
x = fm.FuzzyMatrix([1, 0.7, 0.3, 0, 0])
y = fm.FuzzyMatrix([0, 0, 0.4, 0.7, 1])
x1 = fm.FuzzyMatrix([1, 0.6, 0.4, 0.2, 0])
r1 = fm.mandani(x, y)
r2 = fm.zadeh(x, y)
fm.printFuzzyMatrix(fm.o(x1, r1))
fm.printFuzzyMatrix(fm.o(x1, r2))
