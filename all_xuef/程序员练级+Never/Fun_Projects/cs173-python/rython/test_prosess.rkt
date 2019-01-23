#lang racket/base

(require racket/system racket/list)
(require (planet dherman/json:4:0))
(require racket/cmdline)

(define stdout (open-output-string "stdout"))
(define stderr (open-output-string "stderr"))

(define input-port (open-input-string "def f(a,b): pass"))
(define python-path "C:\\python36\\python")

(command-line
  #:once-each
  ("--i" "Interpret stdin as python"
              (define proc (process*/ports stdout (current-input-port) stderr
                                           python-path 'exact "python-parser.py"))
              ((fifth proc) 'wait)))