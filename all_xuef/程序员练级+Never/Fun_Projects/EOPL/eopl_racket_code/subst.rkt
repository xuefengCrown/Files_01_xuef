;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname subst) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t write repeating-decimal #f #t none #f () #f)))
(define subst
  (lambda (new old s-list)
    (cond ((null? s-list) '())
          ((list? (car s-list))
              (cons (subst new old (car s-list)) (subst new old (cdr s-list))))
          (else 
              (if (eqv? old (car s-list))
                  (cons new (subst new old (cdr s-list)))
                  (cons (car s-list) (subst new old (cdr s-list)))))
          )))

;;(subst new old s-list)
(subst 'a 'b '((b c) (b () d)))
;;((a c) (a () d))