
;; (load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/PoAIP/exercise-chap1.lisp")

(defun dot-product (vector-a vector-b)
  (apply #'+ (mapcar #'* vector-a vector-b)))



