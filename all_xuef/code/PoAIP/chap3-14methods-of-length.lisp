;; (load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/PoAIP/chap3-14methods-of-length.lisp")

;;  14 versions of the function length,  which returns the number of elements in a list.

;;; 1,
(defun len-1 (lst)
  (let ((len 0))			;; start with LEN = 0
    (dolist (ele lst)		;; and on each iteration
	  (setf len (1+ len)))  ;; increment LEN by 1
	  len))					;; return LEN


(defun len-3 (lst)
  (do ((len 0 (1+ len)) 
       (l lst (rest l)))
	   ((null l) len)))

(defun len-4 (lst)
  (loop for ele in lst
    count t))

(defun len-5 (lst)
  (count-if #'true lst))
  
(defun len-6(lst)
  (if (null lst)
      0
	  (1+ (len-6 (rest lst)))
  ))