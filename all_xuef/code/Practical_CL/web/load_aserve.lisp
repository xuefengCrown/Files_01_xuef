

;(load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/Practical_CL/web/load_aserve.lisp")


;To check that ASDF is properly loaded, you can run this form:
(asdf:asdf-version)

;; 使用quickload 安装 aserve
;;; https://www.quicklisp.org/beta/
;;; 1. download quicklisp.lisp && load it
(load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/Practical_CL/quicklisp/quicklisp.lisp")
;;; 2. install ql 
;;; (only need install once, next time you just need ) 
;;; (load "C:/Users/moveb/quicklisp/setup.lisp")
(quicklisp-quickstart:install)
;;; 3. upgrade asdf (1st you need download >3.1asdf.lisp)
(load (compile-file #p"C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/Practical_CL/asdf/asdf.lisp"))
(load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/Practical_CL/asdf/asdf.fas")
;;; 4. install "aserve"
(ql:quickload "aserve")

;; test aserve
(net.aserve:start :port 8090 :listeners 0)


(load "C:/Users/moveb/quicklisp/setup.lisp")
(ql:quickload "aserve")
(net.aserve:start :port 8090 :listeners 0)



