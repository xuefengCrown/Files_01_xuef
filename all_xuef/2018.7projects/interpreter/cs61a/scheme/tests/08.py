test = {
  'name': 'Problem 8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> eval_all(Pair(2, nil), env)
          2b7cdec3904f986982cbd24a0bc12887
          # locked
          # choice: 2
          # choice: SchemeError
          >>> eval_all(Pair(4, Pair(5, nil)), env)
          b33c0f7206201b4aaeae595493888600
          # locked
          # choice: 4
          # choice: 5
          # choice: (4 5)
          # choice: SchemeError
          >>> eval_all(nil, env) # return None (meaning undefined)
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> lst = Pair(1, Pair(2, Pair(3, Pair(4, Pair(5, nil)))))
          >>> eval_all(lst, env)
          b33c0f7206201b4aaeae595493888600
          # locked
          >>> lst     # The list should not be mutated!
          1eaef3f003cb87dd6bcf6efaf16d1254
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> eval_all(Pair(Pair('-', Pair(10, Pair(5, nil))), nil), env)
          b33c0f7206201b4aaeae595493888600
          # locked
          >>> call_expr = Pair('+', Pair(1, Pair(2, nil)))
          >>> print_expr = Pair('print', Pair(10, nil))
          >>> if_expr = Pair('if', Pair(3, Pair(4, Pair(5, nil))))
          >>> exprs = Pair(call_expr, Pair(print_expr, Pair(if_expr, nil)))
          >>> eval_all(exprs, env)
          4bc2fb48972a5d1ec1201b01e766a044
          46beb7deeeb5e9af1c8d785b12558317
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> env = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (begin (+ 2 3) (+ 5 6))
          20169e9f217f8370ba4f37a3cf0cc2b3
          # locked
          scm> (begin (define x 3) x)
          3c7e8a3a2176a696c3a66418f78dff6b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (begin 30 '(+ 2 2))
          85d97cf58c044cc51a6a7d4315b4ad71
          # locked
          # choice: (+ 2 2)
          # choice: '(+ 2 2)
          # choice: 4
          # choice: 30
          scm> (define x 0)
          38ba916dc1f41eb239567ee41a251ecd
          # locked
          scm> (begin 42 (define x (+ x 1)))
          38ba916dc1f41eb239567ee41a251ecd
          # locked
          scm> x
          eb892a26497f936d1f6cae54aacc5f51
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (begin 30 'hello)
          hello
          scm> (begin (define x 3) (cons x '(y z)))
          (3 y z)
          scm> (begin (define x 3) (cons x '(x z)))
          (3 x z)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (begin (define x (+ x 1))
          ....        (define x (+ x 10))
          ....        (define x (+ x 100))
          ....        (define x (+ x 1000)))
          x
          scm> x
          1111
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
