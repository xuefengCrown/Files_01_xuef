;; (load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/ANSI_Common_Lisp/01_Run-length_encoding.lisp")



(defun compress (x)
  (if (consp x)
      (compr (car x) 1 (cdr x))
      x))

	  

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