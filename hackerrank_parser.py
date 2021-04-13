def getQualityCheckCount(cq_file):
  with open(cq_file) as fp:
      lines = fp.readlines()

  count = len(lines)
  return count

def generateQualitylines(n):
    cutoff = 10
    tot_testcases = 20
    testsuite_template = '<testsuite errors="{}" failures="{}" name="{}" skipped="0" tests="{}" time="0.339">\n'

    success_line = '<testcase classname="Test CheckStyle" name="Test CheckStyle"/>\n'
    failure_line = '''<testcase classname="CheckStyle Warnings" name="CheckStyle Warnings">
        <failure>
            <![CDATA[CheckStyle Warnings]]>
        </failure>
</testcase>
'''

    nf = int(round(n/cutoff,0))

    ns = tot_testcases - nf

    test_str = testsuite_template.format(0, nf, 'Code Quality TestSuite', tot_testcases)
    for i in range(ns):
        test_str += success_line
    for i in range(nf):
        test_str += failure_line

    test_str += '</testsuite>\n'
    #print(test_str)
    return test_str


def getStatementsCount(cv_file):
    with open(cv_file) as fp:
        lines = fp.readlines()

    line = lines[-1]

    nums = line.split()[1:3]
    if all([w.isdigit() for w in nums]):
        return [ int(n) for n in nums ]
    return (0, 0)

def generateCoveragelines(ntot, nmis):

     testsuite_template = '<testsuite errors="{}" failures="{}" name="{}" skipped="0" tests="{}" time="0.339">\n'
     success_line = '<testcase classname="Test Code Coverage" name="Test Coverage Success"/>\n'
     failure_line = '''<testcase classname="Missing Test Coverage" name="Missing Test Coverage">
        <failure>
            <![CDATA[Missing Test Coverage]]>
        </failure>
</testcase>
'''

     cov_str = testsuite_template.format(0, nmis, 'Code Coverage TestSuite', ntot)

     ns = ntot - nmis

     for i in range(nmis):
         cov_str += failure_line

     for i in range(ns):
         cov_str += success_line

     cov_str += '</testsuite>\n'
     #print(cov_str)
     return cov_str

def getTestcontents(testfile):
     with open(testfile) as fp:
         lines = fp.readlines()

     inxs = [ix for ix, line in enumerate(lines) if line.startswith('</testsuites>')]
     #print(inxs)
     inx = inxs[0]
     #print(''.join(lines[:inx]))
     return ''.join(lines[:inx])


if __name__ == '__main__':
   test_file = './unit.xml'
   test_contents = getTestcontents(test_file)

   codequality_file = './quality.txt'
   n_warnings = getQualityCheckCount(codequality_file)
   quality_contents = generateQualitylines(n_warnings)


   codecoverage_file = './coverage.txt'
   tot_st, miss_st = getStatementsCount(codecoverage_file)
   coverage_contents = generateCoveragelines(tot_st, miss_st)

   contents = test_contents + coverage_contents + quality_contents + '</testsuites>'

   with open('final.xml', 'w') as ofp:
       ofp.write(contents)
