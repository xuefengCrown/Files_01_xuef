; (load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/Practical_CL/pcl_util.lisp")

(defmacro with-gensyms ((&rest names) &body body)
  `(let ,(loop for n in names collect `(,n (gensym)))
     ,@body))

