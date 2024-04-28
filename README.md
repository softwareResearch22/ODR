Optimized Design Refactoring (ODR)

Overview:
This repository contains the assets for testing the ODR novel methodology that enhances code optimization by integrating optimization heuristics directly into the artifact representation. 
This approach eliminates the need for a separate solution representation, thereby streamlining the refactoring process.

Repository Contents:
- AST and Graph Representations: Encoded using Python's ast library and networkx respectively, these representations are foundational for our empirical study.
- The Tested Python design
- The ODR complex vectors before and after optimization

Methodology:
For conducting the empirical study project employs a sequence-based approach (S = \{(c_i, a_i, c'_i)\}_{i=1}^{6}) for the AST-based and Graph-Based Approach where:

c_i: Identifier for the class holding the attribute/method.
a_i: Identifier for the method/attribute.
c'_i: Destination class identifier.
This approach restricts movements to only attributes or methods between classes, optimizing for factors like memory usage and execution time.

Please refer to the paper for more details about ODR methodology.



