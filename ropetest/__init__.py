import sys
import unittest

import ropetest.advanced_oi_test
import ropetest.builtinstest
import ropetest.codeanalyzetest
import ropetest.contrib
import ropetest.historytest
import ropetest.objectdbtest
import ropetest.objectinfertest
import ropetest.projecttest
import ropetest.pycoretest
import ropetest.pyscopestest
import ropetest.refactor
import ropetest.runmodtest
import ropetest.simplifytest


def suite():
    result = unittest.TestSuite()
    result.addTests(ropetest.projecttest.suite())
    result.addTests(ropetest.codeanalyzetest.suite())
    result.addTests(ropetest.pycoretest.suite())
    result.addTests(ropetest.pyscopestest.suite())
    result.addTests(ropetest.objectinfertest.suite())
    result.addTests(ropetest.objectdbtest.suite())
    result.addTests(ropetest.advanced_oi_test.suite())
    result.addTests(ropetest.runmodtest.suite())
    result.addTests(ropetest.builtinstest.suite())
    result.addTests(ropetest.historytest.suite())
    result.addTests(ropetest.simplifytest.suite())

    result.addTests(ropetest.refactor.suite())
    result.addTests(ropetest.contrib.suite())

    return result


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    result = runner.run(suite())
    sys.exit(not result.wasSuccessful())
