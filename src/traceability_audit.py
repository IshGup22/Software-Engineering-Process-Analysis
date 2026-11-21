"""Audit references in the business-process case study (standard library only).
Run from the repository root: python src/traceability_audit.py
Coverage means explicit requirement reference in a written test scenario,
not a passed test or production traceability guarantee.
"""
from pathlib import Path
import re, csv, json
ROOT = Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs';OUT.mkdir(exist_ok=True)
read=lambda p:(ROOT/p).read_text(encoding='utf-8-sig')
ids={}
for kind,path in [('BR','requirements/business-requirements.md'),('FR','requirements/functional-requirements.md'),('US','agile/user-stories.md'),('AC','agile/acceptance-criteria.md'),('TS','testing/test-scenarios.md')]:
 ids[kind]=set(re.findall(r'(?m)^#{2,3}\s+('+kind+r'-\d+(?:\.\d+)?)\b',read(path)))
test_chunks=re.split(r'(?m)^##\s+(TS-\d+)\s+[^\n]+\n',read('testing/test-scenarios.md'))
links={}
for i in range(1,len(test_chunks),2):
 links[test_chunks[i]]={kind:sorted(set(re.findall(r'\b'+kind+r'-\d+(?:\.\d+)?\b',test_chunks[i+1]))) for kind in ['BR','FR','US','AC']}
invalid=[(test,ref) for test,lk in links.items() for kind,vals in lk.items() for ref in vals if ref not in ids[kind]]
coverage={kind:{rid:sorted([ts for ts,refs in links.items() if rid in refs[kind]]) for rid in sorted(ids[kind])} for kind in ['BR','FR']}
with (OUT/'requirements_test_coverage.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['requirement_id','test_scenarios','coverage_status'])
 for kind in coverage:
  for rid,tests in coverage[kind].items():w.writerow([rid,'; '.join(tests),'Referenced' if tests else 'No explicit test reference'])
rows=list(csv.DictReader((ROOT/'agile/jira-backlog.csv').open()))
summary={'business_requirements':len(ids['BR']),'functional_requirements':len(ids['FR']),'user_stories':len(ids['US']),'acceptance_criteria':len(ids['AC']),'test_scenarios':len(ids['TS']),'backlog_stories':len(rows),'backlog_story_points':sum(int(r['Story Points']) for r in rows),'test_referenced_business_requirements':sum(bool(t) for t in coverage['BR'].values()),'test_referenced_functional_requirements':sum(bool(t) for t in coverage['FR'].values()),'invalid_test_references':len(invalid)}
(OUT/'traceability_summary.json').write_text(json.dumps({'summary':summary,'missing_or_invalid_test_references':invalid,'coverage':coverage},indent=2))
print(json.dumps(summary,indent=2))
assert len(invalid)==0, f'Found invalid test IDs: {invalid}'
