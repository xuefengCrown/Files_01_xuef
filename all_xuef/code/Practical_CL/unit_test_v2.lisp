;; building an unit test framewordk
; (load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/Practical_CL/unit_test_v2.lisp")
(load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/Practical_CL/pcl_util.lisp")

(defvar *test-name* nil)

(defun report-result (result form)
  (format t "~:[fail~;pass~] ... ~a: ~a~%" result *test-name* form)
  result)
	
;; combine results, equal to 'AND',but no short-circuiting
(defmacro combine-results (&body forms)
  (with-gensyms (result)
    `(let ((,result t))
      ,@(loop for f in forms collect `(unless ,f (setf ,result nil)))
      ,result)))	
;; (macroexpand-1 '(check a b c))
(defmacro check (&body forms)
  `(combine-results
    ,@(loop for f in forms collect `(report-result ,f ',f))))
	  
(defmacro deftest (func-name parameters &body body)
  `(defun ,func-name ,parameters
    (let ((*test-name* (append *test-name* (list ',func-name))))
	  ,@body)))
	
(deftest test-+_v2 ()
  (check
	(= (+ 1 2) 3)
	(= (+ 1 2 3) 7)
	(= (+ -1 -3) -4)))
(deftest test-*_v2 ()
  (check
	(= (* 2 3) 6)
	(= (* 4 3) 12)))		

(deftest test-arithmetic()
  (combine-results
    (test-+_v2)
	(test-*_v2)))	
	
(deftest test-math()
  (test-arithmetic))	
	
	
(defun range-h(n m nums)
  (cond 
    ((> n m) nums)
    (t (range-h n (1- m) (cons m nums)))))	
(defun range(n m)
  (range-h n m nil))
	