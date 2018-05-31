;; (load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/ANSI_Common_Lisp/01_Run-length_encoding.lisp")

;; 游程编码
;; > (compress '(1 1 1 0 1 0 0 0 0 1))
;; ((3 1) 0 1 (4 0) 1)

(defun compress (x)
  (if (consp x)
      (compr (car x) 1 (cdr x)) ;; 开启扫描
      x))

	  
;; elt ， 上一个我们看过的元素 
;; n ，连续出现的次数以及 
;; lst ，我们还没检查过的部分列表
(defun compr (elt n lst)
	(if (null lst)
		(list (n-elts elt n))
		(let (
			(next (car lst))
			)
			(if (equal elt next)
				(compr elt (1+ n) (cdr lst))
				(cons (n-elts elt n) (compr next 1 (cdr lst)))))
	)
)


(defun n-elts (elt n)
  (if (> n 1)
      (list n elt)
      elt))