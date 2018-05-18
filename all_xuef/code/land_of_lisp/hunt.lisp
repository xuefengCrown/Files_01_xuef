;; (load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/land_of_lisp/hunt.lisp")

(defparameter *congestion-city-nodes* nil)
(defparameter *congestion-city-edges* nil)
(defparameter *visited-nodes* nil)
(defparameter *node-num* 30)
(defparameter *edge-num* 45)
(defparameter *worm-num* 3)
(defparameter *cop-odds* 15)

(defun random-node ()
  (1+ (random *node-num*)))
  
(defun edge-pair (a b)
  (unless (eql a b)
    (list (cons a b) (cons b a))))

(defun make-edge-list ()
  (apply #'append (loop repeat *edge-num*
                      collect (edge-pair (random-node) (random-node)))))
;; 节点node(9)直接发出的edge				  
(defun direct-edges (node edge-list)
  (remove-if-not (lambda (x)
                   (eql (car x) node))
                 edge-list))
				 
(defun get-connected (node edge-list)
  (let ((visited nil))
    (labels ((traverse (node)
			  (unless (member node visited)
				(push node visited)
				(mapc (lambda (edge)
						(traverse (cdr edge)))
					  (direct-edges node edge-list)))))
		(traverse node))
	visited))